import json


class Business(object):
    businesses = {
        'IceCream Sellers': {
            'location': 'Kampala',
            'services': 'Selling and delivering ice cream'
        },
        'Retail Shop': {
            'location': 'Nairobi',
            'services': 'Merchandary selling'
        }
    }

    def __init__(self):
        pass

    def register_business(self, name, location, services):
        self.businesses[name] = {
            'location': location,
            'services': services
        }

    def update_business(self, name, location, services):
        self.businesses[name] = {
            'location': location,
            'services': services
        }

    def delete_business(self, name):
        del self.businesses[name]

    def getOne(self):
    	return self.businesses['IceCream Sellers']

    def getAll(self):
        return self.businesses
    # return {"name": self.name, "location": self.location, "services": self.services}
