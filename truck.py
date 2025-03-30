class Truck:
    def __init__(self, id):
        self.id = id
        self.driver = None
        self.distanceTravelled = 0
        self.packages = []
        self.status = "at the hub"

    def __str__(self):
        return "Truck %s is %s, loaded packages: %s, distance travelled: %.1f miles." % (self.id, self.status, self.packages, self.distanceTravelled)
    
    def loadPackages(self, p):
        self.packages.append(p)

    def getPackages(self):
        return self.packages