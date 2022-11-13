import json,pyperclip # Import JSON and Pyperclip libraries
command = "function copyTextToClipboard(e){var t=document.createElement(\"textarea\");t.style.position=\"fixed\",t.style.top=0,t.style.left=0,t.style.width=\"2em\",t.style.height=\"2em\",t.style.padding=0,t.style.border=\"none\",t.style.outline=\"none\",t.style.boxShadow=\"none\",t.style.background=\"transparent\",t.value=e,document.body.appendChild(t),t.focus(),t.select();try{var o=document.execCommand(\"copy\");console.log(\"Copying text command was \"+(o?\"successful\":\"unsuccessful\"))}catch(l){console.log(\"Oops, unable to copy\")} document.body.removeChild(t)}cookieStore.getAll().then(res=>{copyTextToClipboard(JSON.stringify(res));});" # Define JS code that gets cookies and copies them to the keyboard
input("This is an Yandex.Music authorization script for YummySpot. It will overwrite your clipboard's contents. If you have some important data in it, please save it. If you're ready, press Enter.\n")
print("1. Go to https://music.yandex.ru")
print("2. Log in with your Yandex account")
print("3. Open DevTools, select Console tab, hit CTRL+V, and press enter(We copied command to your clipboard).\n")
pyperclip.copy(command) # Insert JS code that copies the cookies to the clipboard
cookies = input("4. Go back to this window,press CTRL+V to paste cookies from your clipboard. \n")
print("Writing cookies..")
cookiesTxt = "" # Define empty var
f = open('.cookies',"w+",encoding='utf-8') # Open file
for cookie in json.loads(cookies): # Process JSON cookies
	cookiesTxt+=cookie['name']+"="+cookie['value']+";" # Convert them to Header-like cookies
	pass
cookiesTxt = cookiesTxt[:-1]# Strip semilicon at the end
f.write(cookiesTxt) # Write final cookies
f.close() # Close file
print("Done. Now you're authorized in Yandex.Music.")