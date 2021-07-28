from bs4 import BeautifulSoup
import requests
import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import credentials

user_date = input("Please enter your birthdate in DD-MM-YYYY format: ")
date = datetime.datetime(int(user_date.split("-")[2]), int(user_date.split("-")[1]), int(user_date.split("-")[0]))
date = date.strftime("%Y-%m-%d")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{str(date)}")

data = response.text
soup = BeautifulSoup(data, "html.parser")

all_songs = []
for element in soup.find_all(class_="chart-element__wrapper"):
    title = element.find(class_="chart-element__information__song").getText()
    all_songs.append(title)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",
                                               redirect_uri=credentials.redirect_url,
                                               client_id=credentials.client_ID,
                                               client_secret=credentials.client_SECRET,
                                               show_dialog=True,
                                               cache_path="token.txt"))

user_id = sp.current_user()["id"]
song_uris = []
year = date.split("-")[0]
for song in all_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
