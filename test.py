import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
from spotipy.oauth2 import SpotifyOAuth 
import pandas as pd
import requests

from  Spotify_Secrets import *

# Spotify App credentials 
cid = app_id
secret = app_secret 

#Authorization from user to access profile specific information
spot = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid,
    client_secret=secret,
    redirect_uri="http://localhost:8080",
    scope="user-library-read"))
# Access to general Spotify data. If user doesn't authorize app to access profile this will allow user to still access some features 
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


print('end of program')