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
        #Set departure times, and update the status of trucks/packages
        truck_time = time
        self.status = "out on delivery"
        current_node = 0
        nearest_node = float("inf")
        distance_travelled = 0
        for p in self.packages:
            p.time_departed = truck_time

        while self.packages:
            for pkg in self.packages:
                #Handle the wrong address on package #9
                if truck_time > datetime(2025, 3, 8, 10, 20):
                    new_address = package.myHashTable.search(9)
                    new_address.address = "410 S State St"
                if distances[current_node][pkg.node_index] < nearest_node:
                    nearest_node = distances[current_node][pkg.node_index]
                    next_node = pkg.node_index 
                    package_delivered = pkg

            #Tasks after each package delivery
            miles = distances[current_node][next_node] #Set miles travelled each delivery
            truck_time += td(minutes=miles / 18 * 60) #Updating clock
            distance_travelled += miles #Increment total miles travelled
            self.packages.remove(package_delivered) #Remove package from truck
            current_node = next_node #Update current location
            package_delivered.status = "delivered" #Update package status
            package_delivered.time_delivered = truck_time #Set time package was delivered
            print(f"Truck {self.id} | Package #{package_delivered.id} delivered to {package_delivered.address} at {package_delivered.time_delivered} | Deadline: {package_delivered.deadline}")
            nearest_node = float("inf") #Reset nearest_node value to infinity

        #Return truck 1 + 2 to hub, abandon truck 3
        if self.id == 3:
            self.status = "abandoned"
        else:
            next_node = 0
            miles = distances[current_node][next_node]
            truck_time += td(minutes=miles / 18 * 60)
            distance_travelled += miles
            self.status = "at the hub"
        self.distance_travelled += distance_travelled
        self.return_time = truck_time