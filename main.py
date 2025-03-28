#imports
import sys

def main():
    #User Interface
    runProgram = True
    while(runProgram):
        print("+++++++++++++++++++++++++++++++++")
        print("1. Display package status")
        print("2. Display truck status")
        print("3. Display driver status")
        print("4. Begin Delivery")
        print("5. Exit program")
        print("+++++++++++++++++++++++++++++++++")
        ui_option = input("Choose an option(1, 2, 3, 4 or 5): ")

        if ui_option == 1:
            package_id = input("Enter package ID: ")
            package.getPackage(package_id)
        elif ui_option == 2:
            truck_id = input("Enter truck #(1, 2 or 3): ")
            truck.getStatus(truck_id)
        elif ui_option == 3:
            pass
        elif ui_option == 4:
            #begin_delivery
            pass
        elif ui_option == 5:
            runProgram = False
            print("Exiting program.")
            sys.exit()

if __name__ == "__main__":
    main()