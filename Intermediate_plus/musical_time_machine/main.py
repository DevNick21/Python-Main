from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import pprint
from datetime import datetime as dt

load_dotenv()
pp = pprint.PrettyPrinter(indent=4)
CLIENT_ID = os.getenv("spotify_client_id")
CLIENT_SECRET = os.getenv("spotify_client_secret")
REDIRECT_URI = os.getenv("REDIRECT_URI")
SCOPE = "user-library-read <etc>"

now = dt.now()


class MtimeMachine:
    def __init__(self):
        print("What time you would like to go to")
        self.year = int(input("What Year? in YYYY: "))
        while self.year > int(now.strftime("%Y")):
            self.year = int(input("Enter a valid Year? in YYYY: "))

        self.month = int(input("What Month? in MM: "))
        while self.month > 12:
            self.month = int(input("Enter a valid Year? in YYYY: "))
        self.day = int(input("What Day? in DD: "))
        if self.month == 2:
            while self.day > 29:
                self.day = int(input("Input a valid Day? in DD: "))
        elif self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
            while self.day > 30:
                self.day = int(input("Input a valid Day? in DD: "))
        else:
            while self.day > 31:
                self.day = int(input("Input a valid Day? in DD: "))
        if self.month < 10:
            self.month = "0" + str(self.month)
        if self.day < 10:
            self.day = "0" + str(self.day)
        self.year = str(self.year)
        self.month = str(self.month)
        self.day = str(self.day)
        self.url = f"https://www.billboard.com/charts/hot-100/{self.year}-{self.month}-{self.day}"
        self.sp = self.spotify_auth()
        self.user_id = self.sp.current_user()["id"]
        self.titles = self.generate_hot_100()
        self.create_and_add_playlist()

    def generate_hot_100(self):
        res = requests.get(self.url)
        webpage = res.text
        soup = BeautifulSoup(webpage, "html.parser")
        songs = soup.select(".o-chart-results-list__item h3")
        titles = [song.get_text().strip() for song in songs]
        return titles

    def spotify_auth(self):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private", redirect_uri=REDIRECT_URI,
                                                       client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       show_dialog=True,
                                                       cache_path=".cache",
                                                       )
                             )
        return sp

    def create_and_add_playlist(self):
        song_uris = []
        for title in self.titles:
            results = self.sp.search(f"track:{title} year:{self.year}")
            try:
                uri = results['tracks']['items'][0]['uri']
                song_uris.append(uri)
            except IndexError:
                print(f"{title} doesn't exist in Spotify. Skipped.")
                pass

        playlist = self.sp.user_playlist_create(
            user=self.user_id, name=f"{self.year}-{self.month}-{self.day} Billboard Top 100 on Spotify", public=False)
        self.sp.user_playlist_add_tracks(
            user=self.user_id, playlist_id=playlist["id"], tracks=song_uris)
        print(playlist)


MtimeMachine()
