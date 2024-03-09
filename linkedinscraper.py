from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import re

def loginLinkedIn():
    
    loginUrl = "https://www.linkedin.com/login"
    jobSearchUrl = "https://www.linkedin.com/jobs/search"
    
    jobs = []
    driver = webdriver.Chrome()
    
    driver.get(loginUrl)
    
    driver.find_element(By.ID, 'username').send_keys('linkedinbtp405@outlook.com')
    driver.find_element(By.ID, 'password').send_keys('btp405')
     
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    driver.get(jobSearchUrl)
    
    retries = 0
    max_retries = 5
    while retries < max_retries:
        response = requests.get(jobSearchUrl, headers = {'User-agent': 'MyScraper/1.0'})
        if response.status_code == 429:
            retry_after = int(response.headers.get('Retry-After', '1'))
            print(f"Rate limited. Retrying after {retry_after} seconds...")
            time.sleep(retry_after)
            retries += 1
            continue
        elif response.status_code != 200:
            print(f"Request failed with status code {response.status_code}")
            return None
        else:
            print(response)
            soup = BeautifulSoup(response.content, 'html.parser')
            job_listings = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')

            # with open('job_listings.txt', 'w', encoding='utf-8') as file:
            #     for job in job_listings:
            #         file.write(str(job) + '\n\n')
                    
            for job in job_listings:
                title_elem = job.find('h3', class_="base-search-card__title")
                company_elem = job.find('h4', class_="base-search-card__subtitle")
                location_elem = job.find('span', class_="job-search-card__location")
                salary_elem = job.find('span', class_="job-search-card__salary-info")
                
                if title_elem:
                    cleanedTitle = title_elem.text.strip()
                else:
                    cleanedTitle = "N/A"
                
                if company_elem:
                    cleanedCompany = company_elem.text.strip()
                else:
                    cleanedCompany = "N/A"
                
                if location_elem:
                    cleanedLocation = location_elem.text.strip()
                else:
                    cleanedLocation = "N/A"

                if salary_elem:
                    cleaned_salary = re.sub(r'\s+', '', salary_elem)
                else:
                    cleanedSalary = "N/A"

                formattedJob = {
                    "Job Title": cleanedTitle,
                    "Job Company": cleanedCompany,
                    "Job Location": cleanedLocation,
                    "Job Salary": cleanedSalary
                }
                
                jobs.append(formattedJob)
                
                print(jobs)
                
            driver.quit()
            return None
        
    driver.quit()
    
def main():
    loginLinkedIn()

if __name__ == "__main__":
    main()
