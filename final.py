import requests
from bs4 import BeautifulSoup

page = requests.get('https://queue-times.com/en-US/parks/16/queue_times')

soup = BeautifulSoup(page.text, 'html.parser')

wait = soup.find(class_="column is-half")

wait_list = wait.find_all(class_='panel-block')

print(len(wait_list))

for wait in wait_list:
    # find the first <a> tag and get the text. Split the text using '/' to get an array with developer name and repo name
    full_wait_name = wait.find('a').text.split('/')
    # extract the developer name at index 0
    developer = full_wait_name[0].strip()
    # extract the repo name at index 1
    wait_name = full_wait_name[1].strip()
    # find the first occurance of class octicon octicon-star and get the text from the parent (which is the number of stars)
    
    # strip() all to remove leading and traling white spaces
    print('name', wait_name)
