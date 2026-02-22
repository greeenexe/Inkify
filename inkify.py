import os
import time
import sys
import spotipy
import requests
from io import BytesIO
from spotipy.oauth2 import SpotifyOAuth
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
from waveshare_epd import epd4in2_V2
from PIL import Image, ImageDraw


 #Initialization of EInk Display
epd = epd4in2_V2.EPD()
epd.init()
epd.Clear()
    
#Spotify API
    
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
client_id="REPLACEME",
client_secret="REPLACEME",
redirect_uri="REPLACEME", 
scope="user-read-currently-playing"
))


try:
    last_song_id = None
    print("Starting Spotify monitor (3s intervals)...")
    while True:
        track = sp.current_user_playing_track()
        if track and track['is_playing']:
            current_id = track['item']['id']
            if current_id != last_song_id:
                print("New Song Detected")
                # Extract the URL for the album art
                images = track['item']['album']['images']
                image_url = images[0]['url']  # The first one is usually the highest resolution
                
                # Download the image into memory
                response = requests.get(image_url)
                img = Image.open(BytesIO(response.content))
                
                # This matches the image to your screen's exact size
                img = img.resize((epd.width, epd.height))
                
                # This converts it to 1-bit Black and White with dithering
                img = img.convert('1')
                
                # Push to the screen
                epd.display(epd.getbuffer(img))
                print(f"Displaying art for: {track['item']['name']}")
                time.sleep(2)
                
                last_song_id = current_id

        else:
            print("Nothing playing-clearing screen to save power.")
            epd.Clear()
            time.sleep(2)

            
except KeyboardInterrupt:
    print("Stopping script...")
    epd.Clear()
    epd.sleep()
