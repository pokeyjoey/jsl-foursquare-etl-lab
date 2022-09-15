class Venue:
    columns = ['foursquare_id', 'name', 'rating', 'likes', 'menu_url']

    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)
