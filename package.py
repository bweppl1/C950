class Packages:
    def __init__(self, id, address, city, state, zipcode, deadline, weight, note, status = "At the hub"):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.note = note
        self.status = status

class PackageHashThable:
    def __init__(self, size = 6):
        self.size = size
        self.map = [None] * size

    def insert() 