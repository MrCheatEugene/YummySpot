# YummySpot
YummySpot is an Yandex.Music to Spotify playlist transfer app.

## Installation
1. Clone the repo
2. Install `spotipy` library via PIP.
3. This step is not required, but recommended. Execute `python auth.py` and follow the instructions.
4. Edit `config.py` and fill out sp_client_id, sp_client_secret, sp_redir_uri with Spotify Client Id, Spotify Client Secret, Spotify Redirect URI of an application. <br>
You can create it on (https://developer.spotify.com)[https://developer.spotify.com].
5. Done.

## Running
1. Copy URL to a Yandex.Music playlist
2. Run `python main.py [Yandex. Music Playlist URL] [Spotify playlist name] [0/1 for private playlist, and for public playlist(in that order)]`.
3. In the process, it might open a Spotify OAuth request in browser, accept it, copy the URL after redirect, paste it in terminal and hit enter. 
4. Wait.
5. It should be done, if it fails on STEP 1, then it most likely Yandex.Music API issue, that thinks you're a robot. This might happen if you're not authorized, or you're executing YummySpot too fast. Wait 5 minutes and retry. If it fails again, file an issue with all debug info you can provide.

## Donate
If you want to support me, you can do it (here)[https://donationalerts.com/r/mrcheatt].
Thanks!
