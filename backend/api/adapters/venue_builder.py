from api.models.venue import Venue

class VenueBuilder:

    def __init__(self, response_venue):
        self._response_venue = response_venue

    @property
    def response_venue(self):
        return self._response_venue

    @response_venue.setter
    def response_venue(self, response_venue):
        self._response_venue = response_venue

    def venue(self, **kwargs):
        venue_dict = self.select_attributes()

        return Venue(**venue_dict)

    def select_attributes(self):
        venue_dict = {}

        # extract menu item from delivery and add it to the kwargs
        venue_dict['foursquare_id'] = \
                self.response_venue['id']
        venue_dict['name'] = \
                self.response_venue['name']
        venue_dict['price'] = \
                self.response_venue['price']['tier']
        venue_dict['likes'] = \
                self.response_venue['likes']['count']
        venue_dict['menu_url'] = \
                self.response_venue['delivery']['url'].split('?')[0]

        return venue_dict

    def run(self):
        return self.venue(**self.response_venue)

