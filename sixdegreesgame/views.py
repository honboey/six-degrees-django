import os
import spotipy
import json
import random
import pprint

from django.shortcuts import render
from django.http import HttpResponse
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Song

load_dotenv()

# Spotify calls

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Initialise rappers

def initialise_rappers():
    """
    Grab two random rappers from a list and create a dict for each rapper. Put these dicts in a tuple.
    """
    # List of rappers to choose from
    with open("sixdegreesgame/data/rappers.json", "r") as rappers_file:
        rappers = json.load(rappers_file)

    two_random_rappers = random.sample(rappers, 2)
    return (
        {
            "name": two_random_rappers[0],
            "image": get_rapper_image(two_random_rappers[0]),
        },
        {
            "name": two_random_rappers[1],
            "image": get_rapper_image(two_random_rappers[1]),
        },
    )


# Str -> Dict
def get_rapper_image(str):
    """
    When given an artist name, search the Spotify API and return an image dict for the artist
    """
    rapper_results = spotify.search(q="artist:" + str, type="artist")
    rapper_details = rapper_results["artists"]["items"]
    if len(rapper_details) > 0:
        return rapper_details[0]["images"][0]


# Views

def index(request):
    rappers = initialise_rappers()
    rapper_1 = rappers[0]
    rapper_2 = rappers[1]
    song_1 = Song()
    song_2 = Song()
    
    # Handle the form
    if request.method == "POST":
        if request.POST.get("form-id") == "song-1":
            song_1 = Song(name=request.POST.get("song-name"))
        if request.POST.get("form-id") == "song-2":
            song_2 = Song(name=request.POST.get("song-name"))
        # Delete all songs when user hits "reset"
        if request.POST.get("form-id") == "reset":
            Song.objects.all().delete()
    

    context = {
        "rapper_1": rapper_1,
        "rapper_2": rapper_2,
        "song_1": song_1,
        "song_2": song_2,
    }

    # Check if it's an AJAX request (HTMX request)
    if request.headers.get("HX-Request") == "true":
        # Render the song list template as a string
        song_list_html = render_to_string("sixdegreesgame/includes/song-list.html", context, request)
        pprint.PrettyPrinter(indent=1).pprint(context)

        # Return the updated content as JSON
        return JsonResponse({"html": song_list_html})

    pprint.PrettyPrinter(indent=1).pprint(context)
    return render(request, "sixdegreesgame/index.html", context)


def help(request):
    return render(request, "sixdegreesgame/help.html")
