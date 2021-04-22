from bs4 import BeautifulSoup
import requests
import spotipy
import os
import pprint
CLIENT_ID = os.environ['SPOTIFY_ID']
CLIENT_SECRET = os.environ["SPOTIFY_SECRET"]
songlist = []
artistlist = []
destination_time =input("What year would you like to travel to? YYYY-MM-DD\n")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{destination_time}")
billboard_site = response.text
soup= BeautifulSoup(billboard_site, 'html.parser')
hundred_songs= soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
hundred_artists = soup.find_all(name='span', class_="chart-element__information__artist text--truncate color--secondary")
song_artist= {}
for position in range(len(hundred_songs)):
    song = hundred_songs[position].getText()
    artist = hundred_artists[position].getText().replace("Featuring", ",")
    song_artist[song]=[artist]
    print(song_artist)
print(song_artist)
for song in hundred_songs:
    songlist.append(song.getText())
for artist in hundred_artists:
    artistlist.append(artist)

sp = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(client_id="0473d7dbbb2d4814b559ef5470a47661", client_secret="c87fafa668ac43c0b5751c77d876d378",
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private playlist-modify-public",
                                                              show_dialog=True,
                                                              cache_path='token.txt'))
user = sp.current_user()
user_id=sp.current_user()['id']
print(user_id)
song_uris= []
year=destination_time.split("-")[0]
spotify_song_list =[]
for song in songlist:
    if "," not in song_artist[song]:
        result = sp.search(q=f'track:{song} artist:{song_artist[song]}', type="track")
        try:
            uri=result['tracks']['items'][0]['uri']
            song_uris.append(uri)
        except IndexError:
            print(f"{song} isn't in spotify. Skipped")
    else:
        result = sp.search(q=f'track:{song}{" "}feat. artist:{song_artist[song]}', type="track")
        try:
            uri=result['tracks']['items'][0]['uri']
            song_uris.append(uri)
        except IndexError:
            print(f"{song} isn't in spotify. Skipped")
playlist = sp.user_playlist_create(user=user_id, name=f"Billboard Top 100 week of {destination_time}", public=True, description="The billboard top 100")
sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)


