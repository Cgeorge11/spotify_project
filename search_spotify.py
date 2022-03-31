import datetime
from  Spotify_Secrets import * #Getting client credentials that are being hidden from user 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
from spotipy.oauth2 import SpotifyOAuth 
from datetime import datetime as dt 
import datetime 
import pandas as pd
from generate_logging import *


# Spotify App credentials
cid = app_id
secret = app_secret 

# Using for phase 1: Access to general Spotify data. If user doesn't authorize app to access profile this will allow user to still access some features 
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
spot = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


#Leverage for phase 2: Authorization from user to access profile specific information. 
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid,
    client_secret=secret,
    redirect_uri='http://localhost:8080',
    scope='user-library-read'))

artist_name = []
album_name = []
album_id = []
album_release=[]
years_old = []
track_name = []
track_id = []
popularity = []
artist_genres =[]
artist_id = []


def search_artist_name():# Get Spotify catalog information about albums, artists, tracks that match keyword string
    clear_arrays()
    prompt0 = input('Enter a artist name: ')
    response = 'artist:'+ prompt0
    for i in range(0,10,10):
        track_results = spot.search(q=response, type='artist', limit=5,offset=i) #query (q=) based on user input given in prompt
        for i, t in enumerate(track_results['artists']['items']): #appending the results to the array for each item returned
            artist_name.append(t['name'])
            artist_id.append(t['id'])
            popularity.append(t['popularity'])
            artist_genres.append(t['genres'])

    artist_dataframe = pd.DataFrame({ 'artist_name':artist_name, 'artist_id' : artist_id,'artist_genres':artist_genres, 'popularity' : popularity,})
    print(artist_dataframe)
    artist_dataframe.head()
#search_artist_name()


def search_track_name():
    clear_arrays()
    prompt1 = input('Enter a track: ')
    response = 'track:'+ prompt1
    for i in range(0,10,10):
        track_results = spot.search(q=response, type='track', limit=5,offset=i)
        for i, t in enumerate(track_results['tracks']['items']):
            artist_name.append(t['artists'][0]['name'])
            track_name.append(t['name'])
            track_id.append(t['id'])
            popularity.append(t['popularity'])

    track_dataframe = pd.DataFrame({'artist_name' : artist_name, 'track_name' : track_name, 'track_id' : track_id, 'popularity' : popularity})
    print(track_dataframe)
    track_dataframe.head()    
#search_track()


def search_album_name():
    clear_arrays()
    prompt2 = input('Enter a Album: ')
    response = 'album:'+ prompt2
    for i in range(0,10,10):
        track_results = spot.search(q=response, type='album', limit=5,offset=i)
        for i, t in enumerate(track_results['albums']['items']):
            artist_name.append(t['artists'][0]['name'])
            album_name.append(t['name'])
            album_id.append(t['id'])
            album_release.append(t['release_date'])
            #popularity.append(t['popularity'])
    
    # track_dataframe = pd.DataFrame({'artist_name' : artist_name, 'album_name' : album_name, 'album_id' : album_id, 'album_release':album_release})
    # print(track_dataframe)
    # track_dataframe.head()
#search_albums() 


def album_age( ):
    datetime_object= [dt.strptime(date, "%Y-%m-%d").date() for date in album_release] #album_release array is populated through the search_album_name function 
    today = datetime.date.today()
    for date in datetime_object:
        #print(date)
        age= today.year - date.year 
        #print(age)
        years_old.append(age )
    
    album_dataframe = pd.DataFrame({'artist_name' : artist_name, 'album_name' : album_name, 'album_id' : album_id,'album_release':album_release,'years_old':years_old})
    print(album_dataframe)
    album_dataframe.head()    
#album_age() 


def clear_arrays():
    artist_name.clear()
    album_name.clear()
    album_id.clear()
    album_release.clear()
    years_old.clear()
    track_name.clear()
    track_id.clear()
    popularity.clear()
    artist_genres.clear()
    artist_id.clear()


def end():
    return_menu= input('Do want to search something else (yes/no): ') 
    try:
        if return_menu == 'yes' or return_menu =='Yes':
            start_menu()
            clear_arrays()
        elif return_menu == 'No' or return_menu =='no':
            print('BYE BYE')
            quit()
        else:
            raise
    except:
        print('invalid entry. Try again.') 
        #start_menu()
#end()

def start_menu():    
    print('What do you want to search? ')
    print()
    ep_options= input("""Enter the letter that corresponds with your choice.  
    A) Artists 
    B) Tracks
    C) Albums
    D) Quit
    Enter Selection: """) 
                         
    if ep_options == 'A' or ep_options =='a':
        search_artist_name()
        end()
    elif ep_options == 'B' or ep_options =='b':
        search_track_name()
        end()
    elif ep_options=='C' or ep_options=='c':
        search_album_name()
        album_age()
        end()
    elif ep_options=='D' or ep_options=='d':
        quit()
    elif ep_options:
        print('Oops,Please try again. invalid entry. Enter a corresponding letter to begin search ')
        print()
        start_menu() #Send user back to menu options   
    else:
        quit()
start_menu()


print('hit the bottom of program')