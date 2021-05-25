
#Assigning values to the variables that will have a constant value
budget = 500
economy = 750
vip = 2000
bag_cost = 200
meal_cost = 150
#Assigning values to the variables that will be changed later on depending on the input
ticket_cost = 0
bag = 0
meal = 0
option = 0

#Printing out the ticket names and prices on the screen
print('Ticket types:')
print('1. Budget:', format(budget, '10'), 'kr')
print('2. Economy:', format(economy, '9'), 'kr')
print('3. VIP: ', format(vip, '12'), 'kr\n')

#Asking the user to choose the type of the ticket. Depending on which number the user chooses the price will be added to the ticket_cost.
ticket_type = int(input('Input ticket type here>>'))
if ticket_type == 1:
    ticket_cost = budget

elif ticket_type == 2:
    ticket_cost = economy

elif ticket_type == 3:
    ticket_cost = vip

#This loop will continue until the user chooses to finalize their ticket. That means that if the user presses the wrong number or changes his/hers mind they can just change it.
while option !=5:
    print('\nCurrently you have:\n'
        ,bag,' bag(s) registered\n'
        ,meal,' meal(s) registered\n')

    print('Here are your options:\n',
    '1. Add bag (max 1)\n',
    '2. Add meal (max 1)\n',
    '3. Remove bag\n',
    '4. Remove meal\n',
    '5. Finalize ticket\n')

    #Asking the user to write the number of the option which will be saved in a variable called option.
    option = int(input('Input option type here>>'))
    if option == 1:
        bag = 1

    elif option == 2:
        meal = 1

    elif option == 3:
        bag = 0

    elif option == 4:
        meal = 0

    #Prints out the reciept for the costumer stating all his/hers costs and the total
    elif option == 5:
        print('Receipt:')
        print('Ticket:', format(ticket_cost, '10')+'kr')
        print('Bag:', format(bag*bag_cost, '13')+'kr')
        print('Meal:', format(meal*meal_cost, '12')+'kr')
        print('\t\t---------')
        print('Total:', format(ticket_cost + bag_cost + meal_cost,'11')+'kr')
      