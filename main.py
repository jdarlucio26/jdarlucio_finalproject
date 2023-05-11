# File created by Joshua Darlucio
'''
Sources: 
- https://automatetheboringstuff.com/2e/chapter12/
- 
'''
'''
Goals:
1) Pull ride names out of website
2) List wait times from shortest to longest

If time: Create 

'''
import requests
from bs4 import BeautifulSoup 

# URL for Disneyland wait times
url = ('https://queue-times.com/en-US/parks/16/queue_times')
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
wait_times = soup.find_all("div", class_="has-text-weight-normal")