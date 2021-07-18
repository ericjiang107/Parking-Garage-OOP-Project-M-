# Your assignment for today is to create a parking garage class to get more familiar with Object Oriented Programming(OOP).

# Your parking gargage class should have the following methods:

# takeTicket
    # This should decrease the amount of tickets available by 1
    # This should decrease the amount of parkingSpaces available by 1
# payForParking
    # Display an input that waits for an amount from the user and store it in a variable
    # If the payment variable is not empty then -> display a message to the user that their ticket has been paid and they have 15mins to leave
    # This should update the "currentTicket" dictionary key "paid" to True
# leaveGarage
    # If the ticket has been paid, display a message of "Thank You, have a nice day"
    # If the ticket has not been paid, display an input prompt for payment
        # Once paid, display message "Thank you, have a nice day!"
    # Update parkingSpaces list to increase by 1
    # Update tickets list to increase by 1
# You will need a few attributes as well:

# tickets -> list
# parkingSpaces -> list
# currentTicket -> dictionary

#________________________________________________________________________________________________________________________________________________________#

import random


class ParkingGarage():
    def __init__(self, tickets, parkingSpaces, paidTickets):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.paidTickets = paidTickets
 
    def takeTickets(self):
        park_space = input('Please enter parking space: ')
        rand_ticket = random.choice(self.tickets)
        if park_space.upper() in self.parkingSpaces and rand_ticket in self.tickets:
            self.parkingSpaces.remove(park_space.upper())
            self.tickets.remove(rand_ticket)
            print(f'Your ticket number is {rand_ticket} and your parking space is {park_space.upper()}')
        else:             
            print(f'Error, parking space {park_space.upper()} is occupied. Please try again')
        return (rand_ticket, park_space)
        
            
# # ParkingGarage([1,2,3,4,5], ['A','B','C','D','E'], {})
# checkspace.takeTicket(['A','B','C','D','E'])


    def payForParking(self, park_space):
        cell = "pay" # --> Testing for pay
        if cell.lower() == "pay":
            num = input("Please enter parking space given: ")
            if num.upper() == park_space.upper():
                self.paidTickets[park_space.upper()] = 'paid'
                print(f'Thank you, your ticket has been paid: {self.paidTickets}')
            else: 
                print("Invalid.")
        else:
            print("Error: please enter valid response")
            
    def leaveGarage(self, rand_ticket, park_space):
        if "paid" in self.paidTickets.values():
            print('You have 15 minutes to leave. Have a nice day!')
            self.parkingSpaces.append(park_space.upper())
            self.tickets.append(rand_ticket)
        else:
            print("Wee woo Wee woo Wee woo, the cops are coming!")
            
            
    def availability(self):
        if self.parkingSpaces == []:
            print("Garage full")
        else:
            print(f'Available parking spaces: {self.parkingSpaces}')

            
# res=ParkingGarage([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ["A", 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', J'], {})      
# x, y = res.takeTickets()
# res.payForParking(y) # passing x from function takeTickets to other functions 
# res.leaveGarage(x, y)


# Assuming this is a machine
def runGarage():
    res = ParkingGarage([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ["A", 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], {})
    x = 0 # 0 is a placeholder --> x needs to be declared
    y = '' # empty string is a placeholder --> y needs to be declared
    
    while True:
        cell = input("Please enter what you would like to do: 'park', 'show', 'pay', 'leave' ")
        if cell.lower() == "park":
            x, y = res.takeTickets()
        elif cell.lower() == "show":
            res.availability()
        elif cell.lower() == "pay":
            res.payForParking(y)
        elif cell.lower() == "leave":
            res.leaveGarage(x, y)
            break
            
runGarage() 