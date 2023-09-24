import os
import spotipy
import json
import random

from django.shortcuts import render
from django.http import HttpResponse
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

# Spotify calls

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_artist_image(str):
    artist_results = spotify.search(q="artist:" + str, type="artist")
    artist_details = artist_results["artists"]["items"]
    if len(artist_details) > 0:
        return artist_details[0]["images"][0]


# Views


def index(request):
    # List of rappers to choose from
    with open("sixdegreesgame/data/rappers.json", "r") as rappers_file:
        rappers = json.load(rappers_file)

    # Choose two out of the list
    two_random_rappers = random.sample(rappers, 2)
    rapper_1 = two_random_rappers[0]
    rapper_2 = two_random_rappers[1]
    rapper_1_image = get_artist_image(rapper_1)
    rapper_2_image = get_artist_image(rapper_2)

    context = {
        "rapper_1": {
            "name": rapper_1,
            "image": rapper_1_image,
        },
        "rapper_2": {
            "name": rapper_2,
            "image": rapper_2_image,
        },
    }
    return render(request, "sixdegreesgame/index.html", context)


def help(request):
    return render(request, "sixdegreesgame/help.html")
