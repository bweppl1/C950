import csv
import distances

class Package:
    def __init__(self, id, address, city, state, zipcode, deadline, weight, note, status, node_index):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.note = note
        self.status = status
        self.node_index = node_index
        self.time_departed = None
        self.time_delivered = None
        self.assigned_truck = "Loading Dock"

    def __str__(self):
        return (f"Package #{self.id} status: {self.status} | Destination: {self.city} {self.state}, {self.address}")
    
class PackageHashTable:
    def __init__(self, size = 10):
        self.size = size
        self.table = []
        for i in range(size):
            self.table.append([])

    def __str__(self):
        return (str(line) for line in self.table)
    
    #Inserts a new key value pair - or updates value if key exists
    def insert(self, key, value):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for keyValue in bucket_list:
            if keyValue[0] == key:
                #Update value data if key exists
                keyValue[1] = value
                return True
            
        key_Value = [key, value]
        bucket_list.append(key_Value)
        return True

    #Search hash table for a package
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for keyValue in bucket_list:
            if keyValue[0] == key:
                return keyValue[1]
            
        return None

#Read in package data from CSV file        
def loadPackageData(fileName):
    with open(fileName, mode="r") as packageData:
        packages = csv.reader(packageData)
        for package in packages:
            id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zipcode = package[4]
            deadline = package[5]
            weight = package[6]
            note = package[7]
            status = "at the hub"
            node_index = distances.get_node_index(package[1])

            #Creating an instance of the package
            package = Package(id, address, city, state, zipcode, deadline, weight, note, status, node_index)

            #Loading package data into the hash table
            myHashTable.insert(id, package)

myHashTable = PackageHashTable()