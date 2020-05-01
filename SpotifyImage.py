from PIL import Image
import requests
import json
from io import BytesIO

imgurls = []

token = input("Token: ")
offset = input("Offset: ")
term = input("short, medium, or long Term: ")
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token,
}
params = {
    'time_range': term + '_term',
    'limit': '45',
    'offset': str(offset),
}
topsongs = requests.get('https://api.spotify.com/v1/me/top/tracks', headers=headers, params=params)
topsongs = json.loads(topsongs.text)
for x in range(0, len(topsongs["items"])):
    imgurls.append(topsongs["items"][x]["album"]["images"][1]["url"])
songimg = Image.new('RGB', (1920, 1080), color = "white")
xpos = 15
ypos = 15
for x in range(0, len(imgurls)):
    albumurl = requests.get(imgurls[x])
    albumurl = Image.open(BytesIO(albumurl.content))
    albumurl = albumurl.resize((210,210))
    songimg.paste(albumurl, (xpos,ypos))
    xpos += 210
    if(xpos == 1905):
        xpos = 15
        ypos += 210
songimg.save('finalspot.png')