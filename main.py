# YummySpot
# A simple Yandex.Music playlist to Spotify Playlist converter.
# Usage: python main.py https://yandex.music.playlist.URL SpotifyPlaylistName 0/1(Is spotify playlist private/public)
# For private Yandex.music playlists, you can authorize using "python auth.py". 

import json # Include JSON library to decode info from API
import sys # Include SYS library to access argv and argc variables
from config import sp_redir_uri,sp_scope,sp_client_id,sp_client_secret # Include Spotify app configuration
from ym_playlistparser import ymparser # Include Yandex.Music playlist parser
import spotipy # Include Spotify unofficial API library
from spotipy.oauth2 import SpotifyOAuth # Include Spotify unofficial API library

auth_manager = SpotifyOAuth(client_id=sp_client_id,client_secret=sp_client_secret,redirect_uri=sp_redir_uri,scope=sp_scope) # Creating Auth Manager object 
sp = spotipy.Spotify(auth_manager=auth_manager) # Creating and initializing Spotify Client object
if False == (len(sys.argv) == 4): # if no url was provided
	print("Not enough arguments.")
	sys.exit(1); # DIE
print("Executing STEP 1..")
playlist = ymparser(sys.argv[1]) # parsing playlist
playlist = json.loads(playlist)['playlist'] # loading playlist data
tracks = [] # define empty var
print("OK")
print("Executing STEP 2..")
for track in playlist['tracks']: # for each track..
	if 'artists' in track and 'title' in track: # if it has right properties..
		artists = "" # define empty var
		fullTrackName ="" # define empty var
		for artist in track['artists']: # construct track's artists
			if 'name' in artist: # if a valid artist
				artists+=artist['name']+" " # add it
				pass
			pass
		pass
		fullTrackName = artists+" "+track['title'] # construct full name 
		tracks.append(fullTrackName) # and add
print(str(len(tracks))+" tracks total found in playlist.")
print("OK")
print("Executing STEP 3..")
sp_tracks = [] # define empty var
for track in tracks: # For each track
	res = sp.search(q=track,type='track') # Search it in spotify
	if(('tracks' in res) and ('items' in res['tracks']) and (len(res['tracks']['items'])>=1)): # And if it's a track
		sp_tracks.append(res['tracks']['items'][0]) # Add it
print(str(len(sp_tracks))+"/"+str(len(tracks))+" tracks from playlist found in Spotify")
print("OK")
print("Executing STEP 4..")
current_id = sp.current_user()['id'] # Get current user ID
new_playlist_ID = (sp.user_playlist_create(current_id,str(sys.argv[2]),bool(int(sys.argv[3])),False,"This playlist was transferred from Yandex.Music with YummySpot"))['id'] # Create playlist and make get it's ID
sp_track_uris = [] # Define empty var
for track in sp_tracks: # for each track
	sp_track_uris.append(track['id']) # get it's id and add to list
sp.user_playlist_add_tracks(current_id,new_playlist_ID,sp_track_uris)
print("Done! You can view playlist by link: https://open.spotify.com/playlist/"+str(new_playlist_ID)+"\nThanks for using YummySpot!\nYummySpot made with love, by MrCheatEugene")