class Truck:
    def __init__(self, id):
        self.id = id
        self.driver = None
        self.distanceTravelled = 0
        self.packages = []
        self.status = "At the hub"

    def __str__(self):
        return "Truck: %s, is %s, Distance Travelled: %f" % (self.id, self.status self.distanceTravelled)
    
    def loadPackages(self, p):
        self.packages.append(p)