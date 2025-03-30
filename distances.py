import csv

#Reading in addresses CSV
def loadAddresses(fileName):
    with open(fileName, mode="r") as file:
        reader = csv.reader(file)
        addresses = []
        for address in reader:
            addresses.append(address[0])

    return addresses

#Reading in distances CSV
def loadDistances(fileName):
    with open(fileName, mode="r") as file:
        reader = csv.reader(file)
        #2d array for node distances
        #converting distance values to float, and setting empty values to 'None'
        distances = [[float(distance) if distance.strip() else None for distance in row] for row in reader]

    #Mirroring the dataset, may be unneccesary, but doing it anyways
    for i in range(len(distances)):
        for j in range(len(distances)):
            if distances[i][j] == None:
                distances[i][j] = distances[j][i]

    return distances

def nearest_node(packages, distances, addresses):
    distance_traveled = 0
    current_node = 0
    next_node = 100
    unvisited_nodes = []
    #Update truck status?
    
    for package in packages:
        for i in range(len(addresses)):
            if package.address == addresses[i]:
                unvisited_nodes.append(i)

    while len(unvisited_nodes) > 0:
        for node in unvisited_nodes:
            if distances[current_node][node] < next_node:
                next_node = node

                
        print(f"Package delivered to {addresses[next_node]}")
        #remove package from truck
        #change package status to delivered
        unvisited_nodes.remove(next_node)
        distance_traveled += distances[current_node][next_node]
        current_node = next_node
        next_node = 100

    ###Check if all packages are delivered
    #if len(package.undelivered_packages) > 0:
        #Return home if there is packages to deliver
      #  next_node = 0
      #  distance_traveled += distances[current_node][next_node]
        #Truck.status = "at the Hub"?#