import datetime
from typing_extensions import Self
from  Spotify_Secrets import *
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
from spotipy.oauth2 import SpotifyOAuth 
from datetime import datetime as dt 
import datetime 
import pandas as pd


# Spotify App credentials
cid = app_id
secret = app_secret 

# Access to general Spotify data. If user doesn't authorize app to access profile this will allow user to still access some features 
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
spot = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


#Authorization from user to access profile specific information
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid,
    client_secret=secret,
    redirect_uri='http://localhost:8080',
    scope='user-library-read'))

artist_name = []
album_name = []
album_id = []
album_release=[]
years_old = []



# Get Spotify catalog information about albums, artists, tracks that match keyword string
# def search_artist_uri():
#     pass
# def unfollow_artist():
#     pass

def search_artist_name():

    prompt0 = input('Enter a artist: ')
    response = 'artist:'+ prompt0

    #artist_name = []
    popularity = []
    artist_id = []
    artist_genres =[]
    for i in range(0,10,10):
        track_results = spot.search(q=response, type='artist', limit=5,offset=i)
        for i, t in enumerate(track_results['artists']['items']):
            #artist_name.append(t['artists'][0]['name'])
            #track_name.append(t['name'])
            artist_id.append(t['id'])
            popularity.append(t['popularity'])
            artist_genres.append(t['genres'])

    track_dataframe = pd.DataFrame({ 'artist_id' : artist_id,'artist_genres':artist_genres, 'popularity' : popularity})
    print(track_dataframe)
    track_dataframe.head()
#search_artist_name()
    
def search_track():

    prompt1 = input('Enter a track: ')
    response = 'track:'+ prompt1

    artist_name = []
    track_name = []
    track_id = []
    popularity = []
    
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
 # artist_name = []
   
def search_albums():
        prompt2 = input('Enter a Album: ')
        response = 'album:'+ prompt2
    # album_name = []
    # album_id = []
    # album_release=[]

   
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
    #return artist_name,album_name,album_id,album_id,album_release
#search_albums() 
  

def album_age( ):
    datetime_object= [dt.strptime(date, "%Y-%m-%d").date() for date in album_release]
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


def start_menu():
    print('What do you want to search? ')
    print()
    options= input("""Enter the letter that corresponds with your choice.  
    A) Artists 
    B) Tracks
    C) Albums
    D) Quit
    Enter Selection: """) 
    if options == 'A' or options =='a':
        search_artist_name()
    elif options == 'B' or options =='b':
        search_track()
    elif options=='C' or options=='c':
        search_albums()
        album_age()
    elif options=='D' or options=='d':
        quit()
    else:

        print('Oops. invalid entry. Enter a corresponding letter ')
        print('Please try again')
        start_menu() #Send user bake to menu options    
start_menu()    

def end():
    return_menu= input('Do want to search something else (yes/no): ') 
    try:
        if return_menu == 'yes' or return_menu =='Yes':
            start_menu()
        elif return_menu == 'No' or return_menu =='no':
            print('BYE BYE')
        else:
            raise
    except:
        print('invalid entry. Try again.') 
        start_menu()
end()

print('wow')