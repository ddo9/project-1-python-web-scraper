import pymongo


def ageStatistics():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["NBAstats"]
    collection = db["players"]

    # Filter out players with unrealistic ages (over 100)
    # collection.delete_many({"$expr": {"$gt": [{"$toInt": "$age"}, 100]}})

    # Find the youngest age
    youngest_age = collection.aggregate([
        {"$group": {"_id": None, "minAge": {"$min": {"$toInt": "$age"}}}}
    ]).next()["minAge"]

    # Find all players with the youngest age
    youngest_players = list(collection.find({"age": str(youngest_age)}))

    # Find the oldest age
    oldest_age = collection.aggregate([
        {"$group": {"_id": None, "maxAge": {"$max": {"$toInt": "$age"}}}}
    ]).next()["maxAge"]

    # Find all players with the oldest age
    oldest_players = list(collection.find({"age": str(oldest_age)}))

    # Calculate and print average age
    total_age = sum([int(player.get('age', '0'))
                    for player in collection.find()])
    num_of_players = collection.count_documents({})
    avg_age = round(total_age / num_of_players, 2)

    print("\nThe average age out of {} players in the NBA is {}.\n".format(
        num_of_players, avg_age))

    # Print youngest player(s)
    print("The youngest player(s) in the NBA at the age of {}:".format(youngest_age))
    for player in youngest_players:
        print("- {}".format(player.get('name', '')))

    # Print oldest player(s)
    print("\nThe oldest player(s) in the NBA at the age of {}:".format(oldest_age))
    for player in oldest_players:
        print("- {}".format(player.get('name', '')))


    # Calculate average age for each team
    average_age_by_team = collection.aggregate([
        {"$group": {"_id": "$team", "avgAge": {"$avg": {"$toInt": "$age"}}}}
    ])
    # Convert CommandCursor to list and sort
    average_age_by_team = list(average_age_by_team)
    oldest_team = max(average_age_by_team, key=lambda x: x["avgAge"])
    youngest_team = min(average_age_by_team, key=lambda x: x["avgAge"])

    print("\nThe team with the oldest average players is {} with an average age of {:.2f}.\n".format(
        oldest_team["_id"], oldest_team["avgAge"]))
    print("The team with the youngest average players is {} with an average age of {:.2f}.\n".format(
        youngest_team["_id"], youngest_team["avgAge"]))
