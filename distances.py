import csv

#Assigning the csv files to variables
addressFile = "addresses.csv"
distanceFile = "distances.csv"

#Reading in addresses CSV
def loadAddresses(fileName):
    with open(fileName, mode="r") as file:
        reader = csv.reader(file)
        #2D array for addresses
        addresses = [address for address in reader]

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

#Printing for testing
print(loadAddresses(addressFile))
print(loadDistances(distanceFile))

