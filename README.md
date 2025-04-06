# C950 Task 2 PA - Package delivery algorithm

This program was created for the Task 2 PA of C950 Data Structures and Algorithms at Western Governors University.

Project designed by: Brent Weppler, Student ID# 012456940

## Project Summary
The project requires a python program designed using a hash table data structure and an algorithm that will deliver 40 packages under a set of constraints. The program can use 3 delivery trucks and 2 delivery drivers. The trucks must travel less than 140 miles. Some packages have delivery deadlines, constraints on when they can leave the hub, which truck they can be delivered by and which packages they must be loaded with.

## Function
The program takes 2 datasets:
- One with 40 packages, with delivery deadlines and constraints
- The other is a 2D array of distance vectors between each address

These datasets were converted into .csv files and read into the python program.

The package information was organized into a manually created python chaining hash table, and the distance vectors were formatted into a 2D matrix.

The program offers a simple command line interface offering:
#### 1. Begin Delivery
Triggers the main algorithm of the program. Using the Nearest Neighbour Algorithm the packages are delivered based on the project contraints.

#### 2. Display Status of all Packages
Requests a user input time value, and will display the status of all packages at that time.

#### 3. Display Status of all Trucks
This will display that current status of all trucks, the packages they have loaded, and the total distance(miles) they have travelled. 

#### 4. Exit Program
This will exit the program with confirmation

## Program Conclusion
- Algorithm: Nearest Neighbour
- Data Structure: Chaining Hash Table
- Total Miles: 115.7