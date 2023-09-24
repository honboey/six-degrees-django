import os
import spotipy
import json

from django.shortcuts import render
from django.http import HttpResponse
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()


# Spotify credentials

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Views


def index(request):
    birdy_uri = "spotify:artist:2WX2uTcsvV5OnS0inACecP"
    context = {"results": spotify.artist_albums(birdy_uri, album_type="album")}
    print(json.dumps(context, indent=2))
    return render(request, "sixdegreesgame/index.html", context)


def help(request):
    return render(request, "sixdegreesgame/help.html")
