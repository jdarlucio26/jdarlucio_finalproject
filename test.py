import requests
from bs4 import BeautifulSoup

url = "https://www.laughingplace.com/w/p/disneyland-current-wait-times/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

ride_table = soup.find("table", {"class": "lp_attraction"})
ride_rows = ride_table.find_all("tr")[1:]

for row in ride_rows:
    columns = row.find_all("td")
    ride_name = columns[0].text.strip()
    wait_time = columns[1].text.strip()
    print(f"{ride_name}: {wait_time}")
