from bs4 import BeautifulSoup
import requests
import datetime

user_date = input("Please enter your birthdate in DD-MM-YYYY format: ")
date = datetime.datetime(int(user_date.split("-")[2]), int(user_date.split("-")[1]), int(user_date.split("-")[0]))
date = date.strftime("%Y-%m-%d")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{str(date)}")

data = response.text
soup = BeautifulSoup(data, "html.parser")

all_songs = []
for element in soup.find_all(class_="chart-element__wrapper"):
    rank = element.find(class_="chart-element__rank__number").getText()
    title = element.find(class_="chart-element__information__song").getText()
    artist = element.find(class_="chart-element__information__artist").getText()

    new_dict = {
        "rank": rank,
        "title": title,
        "artist": artist
    }

    all_songs.append(new_dict)

with open(f"my_list_{user_date}.txt", "w") as file:
    file.write("Here's the list of Top 100 Songs of your Birth Week on Billboard\n")
    for key in all_songs:
        file.write(f"{key['rank']}. {key['title']} By {key['artist']}\n")
