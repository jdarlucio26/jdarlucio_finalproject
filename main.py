# Created by: Joshua Darlucio
'''
Sources:
https://medium.com/analytics-vidhya/how-to-scrape-a-table-from-website-using-python-ce90d0cfb607
https://automatetheboringstuff.com/2e/chapter12/
https://www.geeksforgeeks.org/scrape-tables-from-any-website-using-python/
https://realpython.com/python-web-scraping-practical-introduction/
https://www.youtube.com/watch?v=z1nN5pvhdA8
https://www.geeksforgeeks.org/create-first-gui-application-using-python-tkinter/
https://platforuma.medium.com/web-scraping-using-python-gui-31c6c00dd235

GOALS:
1) Screen Scrape Data from website to print in terminal ✔️
2) Have code ask user what their favorite ride is ✔️
3) Have code use the favorite ride and bring up the current wait time ✔️

Reach Goals:
- Have the data recommend order of rides for the day, based on favorite ride. 
'''
# Libraries
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import * 

# Screen scraper to find wait time and ride name through the website. 
def get_wait_time():
    url = "https://www.laughingplace.com/w/p/disneyland-current-wait-times/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    ride_table = soup.find("table", {"class": "lp_attraction"})
    ride_rows = ride_table.find_all("tr")[1:]
    ride_data = {}
    for row in ride_rows:
        columns = row.find_all("td")
        if len(columns) > 1:
            ride_name = columns[0].text.strip()
            wait_time = columns[1].text.strip()
            ride_data[ride_name] = wait_time
# Show data of ride time and names.
    return ride_data

# To show the wait time. Will help pull the wait time and show user the wait time for the ride that they want.
# Links used: https://realpython.com/python-f-strings/#:~:text=Also%20called%20%E2%80%9Cformatted%20string%20literals,be%20replaced%20with%20their%20values.
# Other link: https://coderslegacy.com/python/tkinter-config/
def display_wait_time():
    ride_data = get_wait_time()
    ride_name = entry.get()
    if ride_name in ride_data:
        wait_time = ride_data[ride_name]
        result.config( text=f"The current wait time for {ride_name} is {wait_time}.")
    else:
        result.config(text=f"Sorry, {ride_name} is not found in the ride list.")


# Link used: https://platforuma.medium.com/web-scraping-using-python-gui-31c6c00dd235
# Creates a screen that asks user favorite ride and returns with current wait time

# Name of Screen
root = Tk()
root.title("Disneyland Ride Wait Times")
root.geometry("600x300")

# First Title 
label1 = Label(root, text="Disneyland Current Wait Times", font=('arial',23), fg="purple")
label1.place(x=98,y=15)

# Second title of screen, asks favorite ride
label2 = Label(root, text="Enter your favorite ride:", font=('arial',20), fg="blue")
label2.place(x=138,y=50)

# Provides a box that allows user to type in response. *Reponse must match website name of ride*
entry = Entry(root, width=40)
entry.place(x=170,y=90)

# Button on screen that submits user response
button = Button(root, width=10, text="Get Wait Time", command=display_wait_time)
button.place(x=250, y=130)

# Shows result of current wait time in red font, under button
result = tk.Label(root, text="", fg="red")
result.place(x=35, y=175)

# Loop the program, repeat it over again
root.mainloop()
