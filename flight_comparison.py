#Task 1: Flight Route Comparison Imagine you work for an airline and need to compare 
# the flight routes of your airline with a competitor.
#  You have two sets of flight destinations, one for each airline.
# 
#  Write a Python program to find out:

#1. Destinations that both airlines fly to.

#2. Destinations unique to your airline.

#3. Whether there are any destinations that neither airline shares.

#Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

#Dest. both airlines fly to
def shared_destinations():
    shared = our_routes.intersection(competitor_routes)
    print(f'Both our airline and our competitors fly to: {shared}')


#Dest. unique to our airline
def our_destinations():
    difference = our_routes.difference(competitor_routes)
    print(f'Only our airline flys to: {difference}')


#Destination not in either

def neither_airline():
    destination = input("Enter the airport code for the destination. ")
    if destination not in our_routes and competitor_routes:
        print(f'Neither our airline nor our competitors fly to {destination}')
    elif destination in our_routes:
        print(f'Our airline flys to {destination}, but our competitors do not.')
    elif destination in competitor_routes:
        print(f'Our airline does not fly to:{destination}, but our competitors do.')
    elif destination in competitor_routes and our_routes:
        print(f'Our airline and our competitors fly to : {destination}.')
    else:
        print("Please check your entry, only enter 3 digit code.")

while True:
    try:
        print("Welcome to CT Airlines Flight Checker")
        print("Menu:")
        print("_____________")

        print("1. Find destinations shared with competitors. ")
        print("2. Find destinations unique to CT Airlines. ")
        print("3. Find destinations neither airline flys to.")
        print("4. Quit")

        choice = int(input("Please make your choice. (1-4) "))

        if choice == 1:
            shared_destinations()
        elif choice == 2:
            our_destinations()
        elif choice == 3:
            neither_airline()
        else:
            print("Thank you for using CTA Flight Checker!")
            break

    except ValueError:
        print(ValueError)