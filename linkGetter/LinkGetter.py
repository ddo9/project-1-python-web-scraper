import re
import sys
sys.path.append("..")
from scraper import Scraper

def getNBATeams(url): 
    """getNBATeams
    Returns a list of links to team stat pages

    Args:
        url (str): The url of the page to scrape

    Returns:
        list: A list of links to team stat pages
    """
    page = Scraper.scrapePage(url) # returns entire html of page at url as a string
    
    pattern = r'href="/stats/team/(\d+)"' # regex pattern
        
    teams = re.findall(pattern, page) # find all matches
    
    return teams
