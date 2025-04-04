#Brent Weppler, Student ID# 012456940
#Western Governors University

from datetime import datetime
import sys
import package
import distances
import truck

#Loading CSV data
package.loadPackageData("packages.csv")
distance_array = distances.loadDistances("distances.csv")
address_list = distances.loadAddresses("addresses.csv")

#Creating truck instances
truck1 = truck.Truck(1)
truck2 = truck.Truck(2)
truck3 = truck.Truck(3)

def main():
    #User Interface
    runProgram = True
    while(runProgram):
        print("=" * 50)
        print(" 1. Begin delivery")
        print(" 2. Display status of all packages")
        print(" 3. Display status of all trucks")
        print(" 4. Exit Program")
        print("=" * 50)
        ui_option = int(input("Choose an option(1, 2, 3 or 4): "))

        if ui_option == 1:
            start_delivery()

        elif ui_option == 2:
            while True:
                requested_time = input("Enter a time (HH:MM AM/PM): ").strip()
                try: #Account for incorrect time formatting
                    user_time = datetime.strptime(requested_time, "%I:%M %p").time()
                    break
                except ValueError:
                    print("Not a valid time input.")

            for i in range(1, 41):
                pkg = package.myHashTable.search(i)

                departure_time = pkg.time_departed
                delivery_time = pkg.time_delivered

                print(check_status(pkg, user_time, departure_time, delivery_time))

        elif ui_option == 3:
            #Printing all trucks status'
            print("*" * 50)
            print(truck1)
            print(truck2)
            print(truck3)
            total_mileage = truck1.distance_travelled + truck2.distance_travelled + truck3.distance_travelled
            print(f"Total mileage: {total_mileage:.1f} miles")
            print("*" * 50)

        elif ui_option == 4:
            #Exiting program with confirmation
            confirm = input("Are you sure you want to exit? 'Y' to confirm: ")
            if confirm.lower() == "y":
                runProgram = False
                print("Exiting program.")
                sys.exit()

#Function to check the status of packages at user specified time
def check_status(requested_package, user_time, departure_time, delivery_time):
    if departure_time == None:
        return(f"At {user_time.strftime('%-I:%M %p')} Package #{requested_package.id} is at the hub on Truck {requested_package.assigned_truck}. To be delivered to {requested_package.address}, {requested_package.city} {requested_package.state}. Deadline: {requested_package.deadline}")

    departure_time = requested_package.time_departed.time() #Dropping the date

    if delivery_time == None and user_time >= departure_time:
        return(f"At {user_time.strftime('%-I:%M %p')} Package #{requested_package.id} is en route to be delivered to {requested_package.address}, {requested_package.city} {requested_package.state} on Truck {requested_package.assigned_truck}. Deadline: {requested_package.deadline}")
    elif user_time < departure_time:
        return(f"At {user_time.strftime('%-I:%M %p')} Package #{requested_package.id} was at the hub on Truck {requested_package.assigned_truck}. To be delivered to {requested_package.address}, {requested_package.city} {requested_package.state}. Deadline: {requested_package.deadline}")

    delivery_time = requested_package.time_delivered.time() #Dropping the date

    if user_time >= delivery_time:
        return(f"Package #{requested_package.id} was delivered to {requested_package.address}, {requested_package.city} {requested_package.state} at {requested_package.time_delivered.strftime('%-I:%M %p')} by Truck {requested_package.assigned_truck}. Deadline: {requested_package.deadline}")
    elif user_time > departure_time:
        return(f"At {user_time.strftime('%-I:%M %p')} Package #{requested_package.id} was en route to be delivered to {requested_package.address}, {requested_package.city} {requested_package.state} on Truck {requested_package.assigned_truck}. Deadline: {requested_package.deadline}")
    else:
        return(f"At {user_time.strftime('%-I:%M %p')} Package #{requested_package.id} was at the hub on Truck {requested_package.assigned_truck}. To be delivered to {requested_package.address}, {requested_package.city} {requested_package.state}. Deadline: {requested_package.deadline}")

#Starts the delivery
def start_delivery():
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

    #Departure times, truck 3 departs when truck 2 returns
    truck1_departure_time = datetime(2025, 3, 8, 9, 5)
    truck2_departure_time = datetime(2025, 3, 8, 8, 0)
    
    #Starts delivery, updates package status
    truck1.begin_delivery(distance_array, truck1_departure_time)
    truck2.begin_delivery(distance_array, truck2_departure_time)
    truck3.begin_delivery(distance_array, truck2.return_time)

if __name__ == "__main__":
    main()