from datetime import datetime, timedelta as td

import package

class Truck:
    def __init__(self, id):
        self.id = id
        self.distance_travelled = 0
        self.packages = []
        self.return_time = None
        self.status = "at the hub"

    def __str__(self):
        return "Truck %s is %s, loaded packages: %s, distance travelled: %.1f miles." % (self.id, self.status, self.packages, self.distance_travelled)
    
    def loadPackages(self, p):
        self.packages.append(p)
        p.status = "en route"

    def getPackages(self):
        return self.packages
    
    #Nearest neighbor algorithm
    def begin_delivery(self, distances, time):
        truck_time = time
        self.status = "out on delivery"
        current_node = 0
        nearest_node = float("inf")
        distance_travelled = 0

        while self.packages:
            for pkg in self.packages:
                if truck_time > datetime(2025, 3, 8, 10, 20):
                    new_address = package.myHashTable.search(9)
                    new_address.address = "410 S State St"
                if distances[current_node][pkg.node_index] < nearest_node:
                    nearest_node = distances[current_node][pkg.node_index]
                    next_node = pkg.node_index
                    package_delivered = pkg

            #Tasks after each package delivery
            miles = distances[current_node][next_node]
            truck_time += td(minutes=miles / 18 * 60)
            #Check to update package
            distance_travelled += miles
            self.packages.remove(package_delivered)
            current_node = next_node
            package_delivered.status = "delivered"
            package_delivered.time_delivered = truck_time
            print(f"Package #{package_delivered.id} delivered to {package_delivered.address} by Truck {self.id} at {package_delivered.time_delivered} | {package_delivered.deadline}")
            nearest_node = float("inf")

        #Return to hub
        last_package = package.myHashTable.search(11)
        #Leave truck 3 on the street
        if last_package.status == "delivered":
            pass
        else:
            next_node = 0
            miles = distances[current_node][next_node]
            truck_time += td(minutes=miles / 18 * 60)
            distance_travelled += miles
        self.distance_travelled += distance_travelled
        self.status = "at the hub"
        self.return_time = truck_time
        
    def time_update(miles):
        return(miles / 18 * 60)