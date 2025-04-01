#Brent Weppler
#Student ID# 012456940
#Western Governors University

#imports
from datetime import datetime, timedelta
import sys
import package
import distances
import truck

def main():
    #User Interface
    runProgram = True
    while(runProgram):
        print("+++++++++++++++++++++++++++++++++")
        print("1. Display status of all packages")
        print("2. Display package status at specific time")
        print("3. Display status of trucks")
        print("4. Begin Delivery")
        print("5. Exit program")
        print("+++++++++++++++++++++++++++++++++")
        ui_option = int(input("Choose an option(1, 2, 3, 4 or 5): "))

        if ui_option == 1:
            for i in range(1, 41):
                print(package.myHashTable.search(i))
        elif ui_option == 2:
            pID = int(input("Enter a package ID: "))
            requested_time = input("Enter time HH:MM").strip()
            requested_package = package.myHashTable.search(pID)
            ###### Have to fix below.. needs to reference requested_time
            if requested_package.time_delivered == None and requested_package.time_departed == None:
                print(f"Package #{requested_package.id} is {requested_package.status}")
            elif requested_package.time_delivered == None and requested_package.time_departed:
                print(f"Package #{requested_package.id} is {requested_package.status}")
        elif ui_option == 3:
            print(truck1)
            print(truck2)
            print(truck3)
            total_mileage = truck1.distance_travelled + truck2.distance_travelled + truck3.distance_travelled
            print(f"Total mileage: {total_mileage:.1f} miles.")
        elif ui_option == 4:
            #Create and load trucks
            #TRUCK 1
            truck1_packages_to_load = [2, 4, 5, 6, 7, 1, 9, 10, 24, 26, 25, 28, 40, 32, 33]
            for i in truck1_packages_to_load:
                truck1.loadPackages(package.myHashTable.search(i))

            #TRUCK 2
            truck2_packages_to_load = [8, 3, 13, 14, 15, 16, 18, 19, 20, 30, 31, 34, 36, 37, 38, 29]
            for i in truck2_packages_to_load:
                truck2.loadPackages(package.myHashTable.search(i))

            #TRUCK 3
            truck3_packages_to_load = [22, 23, 11, 27, 35, 12, 17, 21, 39]
            for i in truck3_packages_to_load:
                truck3.loadPackages(package.myHashTable.search(i))

            #Departure times
            truck1_departure_time = datetime(2025, 3, 8, 8, 0) + timedelta(minutes=65)
            truck2_departure_time = datetime(2025, 3, 8, 8, 0)
            
            #Starts delivery, updates package status
            truck1.begin_delivery(distance_array, truck1_departure_time)
            for pkg in truck1.packages:
                pkg.departure_time = truck1_departure_time
            truck2.begin_delivery(distance_array, truck2_departure_time)
            for pkg in truck2.packages:
                pkg.departure_time = truck2_departure_time
            truck3.begin_delivery(distance_array, truck2.return_time)
            for pkg in truck3.packages:
                pkg.departure_time = truck2.return_time
        elif ui_option == 5:
            runProgram = False
            print("Exiting program.")
            sys.exit()

#loading CSV data
package.loadPackageData("packages.csv")
distance_array = distances.loadDistances("distances.csv")
address_list = distances.loadAddresses("addresses.csv")


truck1 = truck.Truck(1)
truck2 = truck.Truck(2)
truck3 = truck.Truck(3)

#fglobal_time = global_time.strftime("%B %d, %Y %I:%M %p")

if __name__ == "__main__":
    main()