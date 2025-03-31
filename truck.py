import package

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
    
    def begin_delivery(self, distances):
        current_node = 0
        nearest_node = float("inf")
        distance_travelled = 0

        while self.packages:
            for package in self.packages:
                if distances[current_node][package.node_index] < nearest_node:
                    nearest_node = distances[current_node][package.node_index]
                    next_node = package.node_index
                    package_delivered = package

            distance_travelled += distances[current_node][next_node]
            self.packages.remove(package_delivered)
            current_node = next_node
            print(f"Package #{package_delivered.id} delivered to {package_delivered.address}")
            nearest_node = float("inf")
            

#Old Algo
    """
    def begin_delivery(self, distances, addresses):
        current_node = 0
        nearest_node = 100
        unvisited_nodes = []
        self.status = "out for delivery"

        
        for package in self.packages:
            for i in range(len(addresses)):
                if package.address == addresses[i]:
                    unvisited_nodes.append(i)
                    package.status = "en route"

        while len(unvisited_nodes) > 0:
            for node in unvisited_nodes:
                edge_weight = distances[current_node][node]
                if edge_weight < nearest_node:
                    nearest_node = edge_weight
                    next_node = node

            print(f"Package delivered to {addresses[next_node]}")
            #remove package from truck
            #change package status to delivered
            unvisited_nodes.remove(next_node)
            self.distanceTravelled += distances[current_node][next_node]
            current_node = next_node
            nearest_node = 100
"""
        ###Check if all packages are delivered
        #if len(package.undelivered_packages) > 0:
            #Return home if there is packages to deliver
        #  next_node = 0
        #  distance_traveled += distances[current_node][next_node]
            #Truck.status = "at the Hub"?#