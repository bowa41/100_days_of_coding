from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_ID = "93556e4d37064d2fb85352c600d20a42"
SPOTIFY_SECRET = "2f144f7c99b04f1b9a78611800826f02"
SPOTIFY_EP = ("https://api.spotify.com/v1/search")
USERNAME = "jaffe.maya@gmail.com"

# OAuth:
# Spotify uses OAuth to allow third-party applications. OAuth is not an API or a service:
# it’s an open standard for authorization and anyone can implement it.

# Create a Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",
                                               redirect_uri="http://localhost:4304/auth/spotify/callback",
                                               client_id=SPOTIFY_ID,
                                               client_secret=SPOTIFY_SECRET,
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               # username=USERNAME,
    )
)

# Get user ID
USER_ID = sp.current_user()["id"]



date_in_history = input("What year do you want to travel to?  Type the date in this format YYYY-MM-DD:")
URL = f"https://www.billboard.com/charts/hot-100/{date_in_history}/"
year = date_in_history[0:4]

response = requests.get(URL)
billboard_100 = response.text
soup = BeautifulSoup(billboard_100, "html.parser")
# print(soup.prettify())
song = soup.find_all(class_="o-chart-results-list-row-container")
song_titles = [songs.find("h3").getText().strip() for songs in song]
print(song_titles)

uris = [sp.search(song)['tracks']['items'][0]['uri'] for song in song_titles]

PLAYLIST_ID = sp.user_playlist_create(user=USER_ID,public=False,name=f"{year} BillBoard-100")['id']
# sp.user_playlist_add_tracks(playlist_id=PLAYLIST_ID,tracks=uris,user=USER_ID)
sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=uris)