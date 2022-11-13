# YummySpot - Yandex.Music playlist info parser
import requests # Include requests library, to do HTTP requests
f = open(".cookies","w+",encoding="utf-8") # Open Yandex.Music Cookies file
cookies = f.read(); # Read cookie
f.close()# Close cookie file
def ymparser(url):
	header = { # Additional headers, to bypass Yandex.Music captcha protection
    	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    	'referer':'https://music.yandex.ru',
    	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    	'Accept-Encoding': 'gzip, deflate, br',
    	'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    	'Cache-Control': 'no-cache',
    	'Connection':'keep-alive',
    	'Host':'music.yandex.ru',
    	'Pragma':'no-cache',
    	'Cookie':cookies
	}
	if url.startswith("https://music.yandex.ru/"): # Format URL a little
		url = url.replace("https://music.yandex.ru/","") # Format URL a little
	spliturl = 	url.split("/") # Split formatted url
	owner = "" # Define empty var
	playlist = "" # Define empty var
	if(len(spliturl)==4 and spliturl[0] == "users" and spliturl[2] == "playlists"): # If we have the required data in the URL, then
		owner = spliturl[1] # Set variable
		playlist = spliturl[3]  # Set variable
	else: # .. or, if we do not
		return False # then fail
	session = requests.Session() # get current session
	res = session.get("https://music.yandex.ru/handlers/playlist.jsx?owner="+requests.utils.quote(owner)+"&kinds="+requests.utils.quote(playlist)+"&light=true&madeFor=&withLikesCount=true&forceLogin=true&lang=ru&external-domain=music.yandex.ru&overembed=false",headers=header) # Make a request to Yandex.Music API
	return (res.text) # Return response from Yandex.Music API