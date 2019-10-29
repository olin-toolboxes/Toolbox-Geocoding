"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.
"""

from urllib.request import urlopen
import json


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"
""" The demo key does not work, hence I will finsh my code after I get the key"""

# A little bit of scaffolding if you want to use it

def get_json(url):
    """Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    JSON_object = urlopen(url)
    response_text = JSON_object.read()
    response_data = json.loads(str(response_text, "utf-8"))
    return response_data

def get_lat_long(place_name):
    """Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    place_word = place_name.split()
    JSON_BASE_URL = GMAPS_BASE_URL + "?address="

    index = 0
    for word in place_word:
        if index == 0:
            temp_URL = JSON_BASE_URL + word
            index = 1
        else:
            temp_URL = temp_URL + "%20" + word

    place_data = get_json(temp_URL)
    return place_data['results'][0]['geometry']['location']['lat'],place_data['results'][0]['geometry']['location']['lng']

def get_nearest_station(latitude, longitude):
    """Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    location_URL = MBTA_BASE_URL + "?api key=" + MBTA_DEMO_API_KEY + "&lat=" + str(latitude) + "&lon=" + str(longitude) + "&format=json"
    station_data = get_json(location_URL)
    station_name = station_data["stop"][0]["stop_name"]
    distance = station_data["stop"][0]["distance"]

    return station_name, distance

def find_stop_near(place_name):
    """Given a place name or address, print the nearest MBTA stop and the
    distance from the given place to that stop.
    """
    lat, lon = get_lat_long(place_name)
    name, dist = get_nearest_station(lat,lon)
    return name, dist

print(find_stop_near(Olin College of Engineering))
