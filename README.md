# Python Web Scraper

### A webscraper for scraping specialized data

There are plenty of sources of data online, but despite the data being readily available, many of the sites don't provide any way of comparing and analyzing the data.

Our goal is to create a specialized web scraper for extracting and analyzing data from popular sources.

From [NBA.com](https://www.nba.com/), we can view player and team data year by year, but have no way to compare or analyze the data. A buzzword in basketball is "impact": the amount of impact a player has on the outcome of a game or season. Currently, there is no way to compare or analyze impact on their site. We aim to create a web scraper that allows us to extract and analyze the data, giving us a way to track the performance and "impact" a player has on a team, particularly after transferring.

## Table of Contents

- [Python Web Scraper](#python-web-scraper)
  - [A webscraper for scraping specialized data](#a-webscraper-for-scraping-specialized-data)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Installing libraries](#installing-libraries)
    - [Basic usage](#basic-usage)
  - [Sources of data](#sources-of-data)
  - [Features](#features)
    - [Web scraping and extraction](#web-scraping-and-extraction)
    - [Data cleaning](#data-cleaning)
    - [Load data into database](#load-data-into-database)
    - [Data analysis and visualization](#data-analysis-and-visualization)
  - [Team](#team)
  - [Testing](#testing)
  - [Roadmap](#roadmap)

## Getting Started

### Installing libraries

This library is written in Python version 3.11.5.

To use this library, you will need to install the following libraries:

- `selenium`
- `beautifulsoup4`
- `requests`
- `matplotlib`
- `pymongo`

Or alternatively, you can run "setup.py" to install the libraries. [TO DO]

### Basic usage

[TO DO: Implement year selector for team stats so that the user can choose a year to extract data from.]

## Sources of data

Currently, we have a limited number of sources of data available. We have scraped data from [NBA.com](https://www.nba.com/) for each team. [TO DO: add more sources; ]

## Features

The following features are currently implemented:

### Web scraping and extraction

Currently, we are scraping player and team data from [NBA.com/teams](https://www.nba.com/teams) via a generalized method. For static pages, we use the `urllib` module, and for dynamic pages, we use the `selenium` module. Both of these methods extracts the entire html of the page as a string, which contains the data that we want to extract, along with a lot of data that we don't.

To extract specific data, we implemented functions for each source of data in order to read and find HTML elements, of which our data is contained in.

### Data cleaning

The data that is scraped contains the entire webpage, which then needs to be sanitised and formatted. This is done using the `Cleaner` module, which takes advantage of a combination of regex and string manipulation to find and clean the data.

### Load data into database

Currently, we are using [MongoDB](https://www.mongodb.com/) as our database. This is because we wanted to take advantage of a NoSQL database, which helps mitigate the strict nature of relational databases. While this makes data loading simpler, it is also not as robust as relational databases. We viewed this as a compromise; we prioritized our development time over reliability. In the future, data may be moved from a NoSQL database to a relational database.

The loading is done through a module called `Load`, which uses the `pymongo` module to connect to the database. Specialized functions are then used for loading data from each source, such as `load_player_to_db` and `load_coach_to_db`.

### Data analysis and visualization

[TO DO]

## Team

Allen Clark - 124888223

Danny Do -

Daniel Fu -

## Testing

[TO DO]

## Roadmap

- Re-organize file structure; each folder is a feature

  -

  ```
  Python-Web-Scraper
  |- NBA
  ||- Cleaner
  |||- Cleaner.py
  ||- LinkGetter
  |||- LinkGetter.py
  ||- Load
  |||- Load.py
  |
  |- LinkedIn
  ||- Cleaner
  |||- Cleaner.py
  |
  |- Scraper
  ||- Scraper.py
  |
  |- main.py
  |- README.md
  ```

- ## Implement viewer for DB
  - Select and display data from DB
- ## Implement LinkedIn scraper
- ## Modify scraper to use memoization (stored on DB)
  - To avoid scraping pages already scraped
- ## Scrape individual player stats
  - e.g. [https://www.nba.com/stats/team/1610612755/players-traditional?Season=2022-23&SeasonType=Regular+Season&SeasonSegment=Post+All-Star](https://www.nba.com/stats/team/1610612755/players-traditional?Season=2022-23&SeasonType=Regular+Season&SeasonSegment=Post+All-Star)
  - `players-traditional` is the type of data we want to scrape
  - `Season=2022-23` is the year we want to scrape data from; can be any year
  - `SeasonType=Regular Season` is the type of season we want to scrape data from; can be one of the following:
    - `Pre+Season`
    - `Regular+Season`
    - `Playoffs`
  - `SeasonSegment=Post+All-Star` is the segment of the season we want to scrape data from; can be one of the following:
    - `SeasonSegment=Pre+All-Star`
    - `SeasonSegment=Post+All-Star`
    - `Month=1` is the month we want to scrape data from; 1 = October, 7 = April
