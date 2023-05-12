# Created by: Joshua Darlucio
'''
Sources:
https://medium.com/analytics-vidhya/how-to-scrape-a-table-from-website-using-python-ce90d0cfb607
https://automatetheboringstuff.com/2e/chapter12/
https://www.geeksforgeeks.org/scrape-tables-from-any-website-using-python/
https://realpython.com/python-web-scraping-practical-introduction/

GOALS:
1) Screen Scrape Data from website to print in terminal ✔️
2) Get screen scraped data into a data table
3) Have terminal ask user what their favorite ride is
4) Have code use the favorite ride and bring up the current wait time

Reach Goals:
- Have the data recommend order of rides for the day. 
'''
# Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Show URL and request python to go to the URL
url = "https://www.laughingplace.com/w/p/disneyland-current-wait-times/"
response = requests.get(url)

# Allow python to screen scrape fromt the website. 
soup = BeautifulSoup(response.content, "html.parser")

# Find the things I am screen scraing. Telling it to pull data from table that follows rule of <tr>
ride_table = soup.find("table", {"class": "lp_attraction"})
ride_rows = ride_table.find_all("tr")[1:]

# Creating a list for ride names and wait times
ride_names = [ride_table]
wait_times = [ride_rows]

# Defining what each column will contain. 
for row in ride_rows:
    columns = row.find_all("tr")
    ride_names.append(columns[1].text.strip())
    wait_times.append(columns[1].text.strip())

# Convert data into a data frame on the screen.
df = pd.DataFrame({'Ride Name': ride_names, 'Wait Time': wait_times})


