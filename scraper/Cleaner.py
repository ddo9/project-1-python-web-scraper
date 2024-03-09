import re
from bs4 import BeautifulSoup

def isCoach(rawStat):
    """isCoach
    Checks if the record is a coach

    Args:
        rawStat (str): The unformatted player stat

    Returns:
        bool: True if the record is a coach, False otherwise
    """
    return "Head Coach" in rawStat or "Assistant Coach" in rawStat or "Trainer" in rawStat

def cleanNBAPlayerStat(playerStatRaw):
    """cleanNBAPlayerStats
    Cleans a dictionary of a players stats from an entry in the list returned from extractNBATeamStats(). 

    Args:
        playerStatRaw (str): The unformatted player stat

    Returns:
        formatted_record (dict): A dictionary of cleaned player stats
    """
    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(playerStatRaw, 'html.parser')
    
    # Extract text content from all non-tag elements into list
    text_content = list(soup.stripped_strings)
    
    # Convert to dictionary
    formatted_record = {}
    
    formatted_record["Name"] = text_content[0]
    formatted_record["Number"] = text_content[1]
    formatted_record["Position"] = text_content[2]
    formatted_record["Height"] = text_content[3]
    formatted_record["Weight"] = text_content[4]
    formatted_record["Date of Birth"] = text_content[5]
    formatted_record["Age"] = text_content[6]
    formatted_record["Experience"] = text_content[7]
    formatted_record["School"] = text_content[8]
      
    return formatted_record
    
def cleanNBAPlayerAverageStats(playerStatsRaw):
    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(playerStatsRaw, 'html.parser')

    # Extract text content from all non-tag elements into list
    text_content = list(soup.stripped_strings)
    
    print("Name: " + text_content[0])
    print("Contents: " + str(text_content))
    
    return text_content
    

def cleanNBACoachStat(coachStatRaw):
    """cleanNBACoachStat
    Returns a dictionary of cleaned coach stats from an entry in the list returned from extractNBATeamStats() that is confirmed to be a coach

    Args:
        coachStatRaw (str): The unformatted coach stat

    Returns:
        formatted_record (dict): A dictionary of cleaned coach stats
    """
    
    cleaned = re.sub(r'<[^>]+>', ' ', coachStatRaw) # remove html tags and classes
    
    components = cleaned.split() # split into list by spaces
    
    if len(components) >= 2: # if there are 2 or more components
        formattedRecord = {
            "First Name": components[-2],
            "Last Name": components[-1],
            "Role": " ".join(components[:-2]),
        }
        # Console logging
        # print("Success: " + str(formattedRecord))
        return formattedRecord
    
    print("Error: " + coachStatRaw) # if there are less than 2 components
    return None
    
def cleanNBAStat(playerOrCoachStatRaw):
    """cleanNBAStat
    Returns a dictionary of cleaned player or coach stats from an entry in the list returned from extractNBATeamStats()

    Args:
        playerOrCoachStatRaw (str): The unformatted player or coach stat

    Returns:
        formatted_record (dict): A dictionary of cleaned player or coach stats
    """
    
    if isCoach(playerOrCoachStatRaw): # if the record is a coach
        return cleanNBACoachStat(playerOrCoachStatRaw)
    else: # if the record is a player
        return cleanNBAPlayerStat(playerOrCoachStatRaw)
    
    
    
    
    
    
    
    
    