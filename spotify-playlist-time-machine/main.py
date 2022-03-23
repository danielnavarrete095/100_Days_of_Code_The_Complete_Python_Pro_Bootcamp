from bs4 import BeautifulSoup
import requests
from secret import *
import spotipy
from spotipy.oauth2 import SpotifyOAuth

BILLBOARD_URL = 'https://www.billboard.com/charts/hot-100/'

selected_date = input("Select a date to go back in time (YYYY-MM-DD): ")

# Get top 100 songs from the web
url = f'{BILLBOARD_URL}/{selected_date}'
response = requests.get(url)
web_page = response.text
# print(web_page)
soup = BeautifulSoup(web_page, 'html.parser')
# Get the song name and artist for each song
song_names = [title.get_text().strip() for title in soup.select('li ul li h3')]
artist_names = [title.findNext('span').get_text().strip() for title in soup.select('li ul li h3')]

# Auth to Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="https://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"))
user = sp.current_user()["id"]
# print(user)

# Create Spotify playlist
playlist_name = f"Time-travel-to-{selected_date}"
playlist = sp.user_playlist_create(user, playlist_name, public=False, description='Test')

spotify_song_list = []
for idx, song in enumerate(song_names):
    artist = artist_names[idx] if "Featuring" not in artist_names[idx] else artist_names[idx].split("Featuring")[0].strip()
    print(f"{song} - {artist}")
    results = sp.search(q=f'track:{song} artist:{artist}', limit=20)
    if results['tracks']['items']:
        print(results['tracks']['items'][0]['uri'])
        # if song found in spotify, add URI to list
        spotify_song_list.append(results['tracks']['items'][0]['uri'])
# Add list of songs to the playlist
result = sp.user_playlist_add_tracks(user, playlist['id'], spotify_song_list, position=None)
print(playlist['uri'])
print(result)