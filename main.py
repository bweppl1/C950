#Brent Weppler
#Student ID# 012456940
#Western Governors University

#imports
import sys
import package

def main():
    #User Interface
    runProgram = True
    while(runProgram):
        print("+++++++++++++++++++++++++++++++++")
        print("1. Placeholder")
        print("2. Display package status")
        print("3. Placeholder")
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
            pass
        elif ui_option == 4:
            #begin_delivery
            pass
        elif ui_option == 5:
            runProgram = False
            print("Exiting program.")
            sys.exit()

package.loadPackageData("packages.csv")

#print (package.myHashTable.table)

if __name__ == "__main__":
    main()