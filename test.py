from  Spotify_Secrets import *
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
from spotipy.oauth2 import SpotifyOAuth 
import pandas as pd
import requests



# Spotify App credentials
cid = app_id
secret = app_secret 

# Access to general Spotify data. If user doesn't authorize app to access profile this will allow user to still access some features 
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
spot = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


#Authorization from user to access profile specific information
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid,
    client_secret=secret,
    redirect_uri="http://localhost:8080",
    scope="user-library-read"))


# Get Spotify catalog information about albums, artists, tracks that match keyword string
def search_artist ():
    pass 

def search_track():
    pass

def search_albums():
    pass 


print('wow') 