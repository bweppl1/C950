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
    current_node = addresses[0]
    next_node = None
    unvisited_nodes = []
    
    for package in packages:
        for i in range(len(addresses)):
            if package[1] == addresses[i]:
                unvisited_nodes.append(i)

    while len(unvisited_nodes) > 0:
        for node in unvisited_nodes:
            if distances[current_node][node] < next_node or next_node == None:
                next_node = node

        distance_traveled += distances[current_node][next_node]
        current_node = next_node
        next_node = None
