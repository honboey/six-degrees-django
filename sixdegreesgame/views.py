import os
import spotipy
import json
import random

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
    # List of rappers to choose from
    with open("sixdegreesgame/data/rappers.json", "r") as rappers_file:
        rappers = json.load(rappers_file)

    # Choose two out of the list
    random_rappers = random.sample(rappers, 2)

    context = {"random_rappers": random_rappers}
    return render(request, "sixdegreesgame/index.html", context)


def help(request):
    return render(request, "sixdegreesgame/help.html")
