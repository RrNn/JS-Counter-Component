import json


class Business(object):

    def __init__(self, name, location, services):
        self.name = name
        self.location = location
        self.services = services

    def getAll(self):
        return {"name": self.name, "location": self.location, "services": self.services}
