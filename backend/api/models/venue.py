class Venue:
    columns = ['foursquare_id', 'name', 'price', 'likes', 'menu_url']

    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            if k in self.columns:
                setattr(self, k, v)
