
from pymongo import MongoClient

def connect_to_db():
    """
    Create MongoDB connection.

    Returns:
        pymongo.database.Database: The MongoDB database name.
    """
    client = MongoClient("mongodb://localhost:27017")
    return client.NBAstats  # use NBAstats database

def load_player_to_db(player_data, team_name):
    """
    Insert or update player data in MongoDB to avoid duplicates.

    Args:
        player_data (dict): A dictionary containing player data.
        team_name (str): The name of the team.

    Returns:
        None
    """
    # TODO: Move to hosted DB
    db = connect_to_db()

    try:
        # filters through first_name and last_name to avoid duplicates
        filter_query = {"name": player_data["Name"]}
        update_query = {
            "$set": {
                "number": player_data["Number"],
                "position": player_data["Position"],
                "height": player_data["Height"],
                "weight": player_data["Weight"],
                "date_of_birth": player_data["Date of Birth"],
                "age": int(player_data["Age"]),
                "experience": player_data["Experience"],
                "team": team_name
            }
        }

        db.players.update_one(filter_query, update_query, upsert=True)
        # Console logging
        # print("Player data loaded to MongoDB successfully")
        
    except Exception as e:
        print(f"Error loading player data to MongoDB: {e}")

def load_coach_to_db(coach_data, team_name):
    """
    Insert or update coach data in MongoDB to avoid duplicates.

    Args:
        coach_data (dict): A dictionary containing coach data.
        team_name (str): The name of the team.

    Returns:
        None
    """
    db = connect_to_db()

    try:
        # filters through first_name and last_name to avoid duplicates
        filter_query = {"first_name": coach_data["First Name"], "last_name": coach_data["Last Name"]}
        update_query = {
            "$set": {
                "role": coach_data["Role"],
                "team": team_name
            }
        }

        db.coaches.update_one(filter_query, update_query, upsert=True)
        
        # Console logging
        # print("Coach data loaded to MongoDB successfully")

    except Exception as e:
        print(f"Error loading coach data to MongoDB: {e}")
