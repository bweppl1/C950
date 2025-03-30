#Brent Weppler
#Student ID# 012456940
#Western Governors University

#imports
import sys
import package
import distances
import truck

def main():
    #User Interface
    runProgram = True
    while(runProgram):
        print("+++++++++++++++++++++++++++++++++")
        print("1. Placeholder")
        print("2. Display package status")
        print("3. Display status of trucks")
        print("4. Begin Delivery")
        print("5. Exit program")
        print("+++++++++++++++++++++++++++++++++")
        ui_option = int(input("Choose an option(1, 2, 3, 4 or 5): "))

        if ui_option == 1:
            pass
        elif ui_option == 2:
            pID = int(input("Enter a package ID: "))
            print(package.myHashTable.search(pID))
        elif ui_option == 3:
            print(truck1)
        elif ui_option == 4:
            #Starts delivery
            truck1.begin_delivery(distance_array, address_list)
        elif ui_option == 5:
            runProgram = False
            print("Exiting program.")
            sys.exit()

#loading CSV data
package.loadPackageData("packages.csv")
distance_array = distances.loadDistances("distances.csv")
address_list = distances.loadAddresses("addresses.csv")

#Create and load trucks
#TRUCK 1
truck1 = truck.Truck(1)
truck1_packages_to_load = [1, 2, 3]
for i in truck1_packages_to_load:
    truck1.loadPackages(package.myHashTable.search(i))

#TRUCK 2
truck2 = truck.Truck(2)

#TRUCK 3
truck3 = truck.Truck(3)



#Testing print functions
#print (package.myHashTable.table)

if __name__ == "__main__":
    main()