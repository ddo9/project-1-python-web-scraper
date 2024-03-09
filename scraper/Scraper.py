from urllib.request import urlopen # for static web scraping
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

def scrapePage(url):
    """scrapePage
    returns entire html of page at url

    Args:
        url (str): The url of the page to scrape

    Returns:
        str: The html of the page
    """
    page = urlopen(url)
    
    htmlPage = page.read()
    htmlDecoded = htmlPage.decode("utf-8")
    
    return htmlDecoded

def scrapeDynamicPage(url, waitTag):
    """scrapeDynamicPage
    returns html of page at url after waiting for "waitTag" to load. Used for pages with client side javascript. Uses selenium webdriver to emulate browser.

    Args:
        url (str): The url of the page to scrape
        waitTag (str): The html tag to wait for to load before scraping

    Returns:
        str: The html of the page
    """
    
    # TODO: "quietly" open the browser
    
    driver = webdriver.Chrome()
    driver.get(url)
    
    tag = "//" + waitTag
    
    try: 
        # wait for tag to load
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, tag))
        )

        return driver.page_source
        
    except Exception as e:
        print("Error: " + str(e))
        
    finally:
        driver.quit()
        
def extractNBATeamName(teamURL):
    """extractNBATeamName
    Extracts the NBA team name from the team URL

    Args:
        teamURL (str): The url of the NBA team

    Returns:
        str: The name of the NBA team
    """
    page = scrapePage(teamURL)
    
    pattern = r'<title>(.*?)Team Info and News | NBA.com</title>'
    
    teamName = re.search(pattern, page)
    
    if teamName:
        # Console logging
        # print("Success: " + str(teamName.group(1)))
        return teamName.group(1)
    else:
        # Console logging
        # print("No team name found")
        return None
        
def extractNBATeamStats(teamURL):
    """extractNBATeamStats
    Returns a list of cleaned team stats from the NBA team stats page

    Args:
        teamURL (str): The url of the NBA team stats page

    Returns:
        list: A list of cleaned team stats. Formatted as `<First Name> <Last Name> "#"<Number>, <Position>, <Height> <Weight in lbs> "lbs" <Date of birth as 'MMM DD, YYYY'> <Age> <Experience> <School> <How Aquired>`
    """
    
    # Console logging
    # print(teamURL)
    teamHTML = scrapeDynamicPage(teamURL, 'table') # return html of team stats
    
    # scrape each <tr> to </tr> tag using regex
    pattern = r'<tr>(.*?)</tr>'
    teamStats = re.findall(pattern, teamHTML, re.DOTALL) # find all matches and store in list
    
    return teamStats

def scrapePage(url):
    """scrapePage
    returns entire html of page at url

    Args:
        url (str): The url of the page to scrape

    Returns:
        str: The html of the page
    """
    page = urlopen(url)
    
    htmlPage = page.read()
    htmlDecoded = htmlPage.decode("utf-8")
    
    return htmlDecoded

def scrapeDynamicPageByClassName(url, className):
    
    # TODO: "quietly" open the browser
    
    driver = webdriver.Chrome()
    driver.get(url)
    
    try: 
        # wait for tag to load
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, className))
        )

        return driver.page_source
        
    except Exception as e:
        print("Error: " + str(e))
        
    finally:
        driver.quit()

def extractNBAPlayerStats(teamURL):
    
    # Wait for Crom_body__UYOcU to load
    teamHTML = scrapeDynamicPageByClassName(teamURL, 'Crom_body__UYOcU') 
    
    # scrape each <tr> to </tr> tag using regex
    pattern = r'<tr>(.*?)</tr>'
    teamStats = re.findall(pattern, teamHTML, re.DOTALL) # find all matches and store in list
    
    return teamStats
        

