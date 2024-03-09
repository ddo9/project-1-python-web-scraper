import pymongo
import matplotlib.pyplot as plt
import heapq

def heightStatistics():

    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["NBAstats"]
    collection = db["players"]

    # Retrieve data
    data = collection.find()

    # Extract height data
    player_data = {}

    for document in data:
        
        height_str = document.get('height')
        height_str_split = height_str.split("-")
        
        if (len(height_str_split) > 1):
            
            feet_str = height_str_split[0]
            inch_str = height_str_split[1]
            
            if (feet_str.isnumeric() and inch_str.isnumeric()):
                height_inches = int(height_str_split[0]) * 12 + int(height_str_split[1])
                
                player_name = f"{document.get('first_name')} {document.get('last_name')}"
                player_data[player_name] = height_inches

    # Find the tallest players
    num_of_players = 20
    tallest_players = heapq.nlargest(num_of_players, player_data, key=player_data.get)
    tallest_heights = [player_data[player] for player in tallest_players]
    print(tallest_players)
    print(tallest_heights)


    # Display the tallest players
    plt.figure(figsize=(10, 6))
    plt.bar(tallest_players, tallest_heights)
    plt.xlabel('Player')
    plt.ylabel('Height (inches)')
    plt.title('Tallest NBA Players')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()