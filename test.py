import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.laughingplace.com/w/p/disneyland-current-wait-times/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

ride_table = soup.find("table", {"class": "lp_attraction"})
ride_rows = ride_table.find_all("tr")[1:]

for row in ride_rows:
    columns = row.find_all("td")
    ride_name = columns[0].text.strip()
    wait_time = columns[1].text.strip()

df = pd.DataFrame({'Ride Name': ride_name, 'Wait Time': wait_time})
df.to_excel('Disneyland Wait Times.xlsx', index=False)

#     print(f"{ride_name}: {wait_time}")


# data = [ride_name, wait_time]

# df = pd.DataFrame(data, columns=['Ride Name', 'Current Wait Time'])

df