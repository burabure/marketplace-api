from flask import Flask, request
import MarketplaceScraper
import Database

API = Flask(__name__)

Database.init()
# Database.all_seen()

# NOTE: keep requests under 200 per hour

QUERIES = [
    'pvm',
    'monitor pvm',
    'sony pvm',
    'bvm',
    'monitor bvm',
    'sony bvm',
    'monitor crt',
    'vga crt',
    'JVC H1950CG',
    'sony 20L5',
    'sony 20L4',
    'sony fw9000',
    'sony w900',
]

LOCATIONS = [
    # --- Chile
    [-18.4732, -70.3036],      # Arica
    [-20.2415, -70.1342],      # Iquique
    [-23.6436, -70.3884],      # Antofagasta
    [-27.3667, -70.3333],      # Copiapo
    [-29.9, -71.25],           # La Serena
    [-33.4498, -70.6671],      # Santiago
    [-37.4667, -72.35],        # Los Angeles
    [-41.4717, -72.9369],      # Puerto Montt
    [-45.402265, -72.690097],  # Puerto Aisen
    [-47.8333, -73.5667],      # Tortel
    [-51.72941, -72.50168],    # Puerto Natales
    [-53.1667, -70.9333],      # Punta Arenas
    [-54.935515, -67.610562],  # Puerto Williams
]


@ API.route("/listings", methods=["GET"])
def listings():
    response = {}
    response["listings"] = Database.all_listings()
    return response


@ API.route("/locations", methods=["GET"])
def locations():
    response = {}

    # Required parameters provided by the user
    locationQuery = request.args.get("locationQuery")

    if (locationQuery):
        status, error, data = MarketplaceScraper.getLocations(
            locationQuery=locationQuery)
    else:
        status = "Failure"
        error["source"] = "User"
        error["message"] = "Missing required parameter"
        data = {}

    response["status"] = status
    response["error"] = error
    response["data"] = data

    return response


@ API.route("/search", methods=["GET"])
def search():
    response = {}

    # Required parameters provided by user
    locationLatitude = request.args.get("locationLatitude")
    locationLongitude = request.args.get("locationLongitude")
    listingQuery = request.args.get("listingQuery")

    if (locationLatitude and locationLongitude and listingQuery):
        status, error, data = MarketplaceScraper.getListings(
            locationLatitude=locationLatitude, locationLongitude=locationLongitude, listingQuery=listingQuery)
    else:
        status = "Failure"
        error["source"] = "User"
        error["message"] = "Missing required parameter(s)"
        data = {}

    response["status"] = status
    response["error"] = error
    response["data"] = data

    return response


@ API.route("/search_all", methods=["GET"])
def search_all():
    response = {}

    for [locationLatitude, locationLongitude] in LOCATIONS:
        for listingQuery in QUERIES:
            if (locationLatitude and locationLongitude and listingQuery):
                print("")
                status, error, data = MarketplaceScraper.getListings(
                    locationLatitude=locationLatitude, locationLongitude=locationLongitude, listingQuery=listingQuery)
            else:
                status = "Failure"
                error["source"] = "User"
                error["message"] = "Missing required parameter(s)"
                data = {}

            response["status"] = status
            response["error"] = error

            if ("data" in response):
                if ("listings" in data):
                    response["data"]["listings"] = response["data"]["listings"] + \
                        data["listings"]
            else:
                response["data"] = data

    return response


# /search?locationLatitude=-33.43179&locationLongitude=-70.6094&listingQuery=pvm
