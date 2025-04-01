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

def get_node_index(address):
    address_list = loadAddresses("addresses.csv")
    for i in range(len(address_list)):
        if address == address_list[i]:
            return i