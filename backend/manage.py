from api.models.venue import Venue
from api.adapters.client import Client
from api.adapters.venue_builder import VenueBuilder

def run():
    venues = []
    client = Client()
    venue_responses = client.request_venues()
    for venue_response in venue_responses:
        venue_response = client.request_venue(venue_response['id'])
        builder = VenueBuilder(venue_response)
        venue = builder.run()
        venues.append(venue)
    return venues

