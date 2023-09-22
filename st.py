import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="a82bde1f830f474f9d32e6c9198600ed",
                                                           client_secret="2cca93f817604733b39d013064db68de"))

print(sp.featured_playlists()['playlists'][0])
print(sp.tra)
exit()
results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])