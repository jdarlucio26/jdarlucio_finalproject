# File created by Joshua Darlucio
'''
Sources: 
'''
'''
Goals:
1) Pull ride names out of website
2) Ask user their favorite type of ride
3) Use favorite ride to build a list of what rides to ride, based on wait times

'''
import requests
from bs4 import BeautifulSoup

# URL for Disneyland wait times
url = 'https://www.thrill-data.com/waits/park/dlr/disneyland/'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Find all the ride names and wait times
rides = soup.find_all('div', class_='plot-container plotly')
ride_data = {}
for ride in rides:
    name = ride.find('div', class_='col-sm-8 ride-name').text.strip()
    wait_time = ride.find('div', class_='col-sm-4 ride-wait-time').text.strip()
    ride_data[name] = int(wait_time)

