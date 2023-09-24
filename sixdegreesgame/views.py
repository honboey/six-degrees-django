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
    two_random_rappers = random.sample(rappers, 2)
    rapper_1 = two_random_rappers[0]
    rapper_2 = two_random_rappers[1]
    rapper_1_image = spotipy.search(q="artist:" + rapper_1, type="artist")

    context = {
        "rapper_1": rapper_1,
        "rapper_2": rapper_2,
    }
    return render(request, "sixdegreesgame/index.html", context)


def help(request):
    return render(request, "sixdegreesgame/help.html")
