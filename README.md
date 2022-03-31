# Search Spotify 
This program will allow the user to select the type of item they would like to search for within Spotify. Depending on the users selection they will be returned a table with data related to the users search. This README was written assuming you already know the basics for running a python. If this is your first time running a a Python script start [here](https://realpython.com/run-python-scripts/#using-the-python-command). Then come back. 

## Running program 
This project was built using Python 3.10.1. To run program from command prompt user will need to install [spotipy libary](https://spotipy.readthedocs.io/en/2.19.0/#installation). 

`pip install spotipy --upgrade`

Once you download this repo you will be able to start program from command line using [script file name](https://realpython.com/run-python-scripts/#using-the-script-filename). 


Run search_spotify.py from command line. 
Don't know what this does but you're going to need it pip install typing-extensions
## Feature Requirement 
**Category 1** 

`def album_age( )` use the `album_release = []` array that is appended in def `search_album_name()` with the album release dates. Then it subtracts that date from the current date using datetime module to return  `age` in year. 

**Category 2** 

Connecting to [spotify API ](https://developer.spotify.com/documentation/web-api/reference/#/operations/search). This program is currently using Spotify Client Credentials code flow but has the set up to access Authorization Code Flow for get user authorization for future development. 

**Category 3** 

Program uses `pandas.Dataframe()` to structure returned data in a table.


![Table example](images\Example_table_output.JPG) 

**Category 4** 

https://realpython.com/python-pep8/