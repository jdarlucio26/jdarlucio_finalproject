import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.laughingplace.com/w/p/disneyland-current-wait-times/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

ride_table = soup.find("table", {"class": "lp_attraction"})
ride_rows = ride_table.find_all("tr")[1:]

ride_names = []
wait_times = []

for row in ride_rows:
    columns = row.find_all("t")
    ride_names.append(columns[0].text.strip())
    wait_times.append(columns[1].text.strip())

df = pd.DataFrame({'Ride Name': ride_names, 'Wait Time': wait_times})
df.to_excel('Disneyland Wait Times.xlsx', index=False)
