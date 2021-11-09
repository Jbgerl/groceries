# Joseph Gerl
# A list that will serve as a smart list for groceries
print("Welcome to my Smart list program")
name = input("What is your name? ")


def main_menu():  # introduction of the program
    print('Welcome', name, '\nThis is the main menu')
    print('Please select an option between 1 - 3')
    print('1: Tutorial')
    print('2: Grocery List')
    print('3: I am Finished for today!')
    keep_running = True
    while keep_running:
        try:
            menu_choice = int(input('What is your selection? '))
            if menu_choice == 1:
                print('Great Selection! Lets Learn together!')
                tutorial()  # opens the function for basic operations
            elif menu_choice == 2:
                print('Good Choice, Lets work!')
                grocery_list()  # creates the grocery list
            elif menu_choice == 3:
                print('Have a nice day!')
                keep_running = False
            else:
                # noinspection PyStatementEffect
                0 >= menu_choice > 3
                print('You are better than this, Lets try again!')
                print('I believe in you!')  # Good old positive reinforcement!
                print('Please select an option between 1 - 3')
        except ValueError:
            print('You are better than this, Lets try again!')
            print('I believe in you!')  # Good old positive reinforcement!


def tutorial():  # Defining the tutorial. Not my favorite part of this
    # program
    """
This is defining the tutorial function
    """
    print("Before we get too far, lets learn how this system works.")
    print("Basic operations")
    # addition
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    print("addition")
    sum = num1 + num2
    print(sum)
    # subtraction
    print("Subtraction")
    difference = num1 - num2
    print(difference)
    # multiplication
    print('multiplication')
    product = num1 * num2
    print(product)
    # division
    print('division')
    quotient = num1 / num2
    print(quotient)
    # Floor division
    print('Floor Division')
    floor_division = num1 // num2
    print(floor_division)
    # modulus
    print('remainder')
    remainder = num1 % num2
    print(remainder)
    print('Now for the actual tutorial')  # this is going to be the core of
    # the system
    print('Simple: Tell me what you need from the grocery store, and i will '
          'make note of it')
    print('If you do not know the details, that is fine, save it for next '
          'time.')
    print('lets try one together')
    grocery_practice()


# a simple practice function to see it in action, doesnt record responses
def grocery_practice():
    item = input("What was this item?  ", )
    price = input('What was the price of the item? ', )
    quantity = input('How many did you buy?  ', )
    store = input('What store did you buy it from?  ', )
    print('Item', 'price', 'quantity', 'store')
    print(item, price, quantity, store)
    print('Now you try!')
    grocery_list()


# main functionality within the program to make the list
def grocery_list():
    print('item', 'price', 'quantity', 'store')
    item = input("What was this item?  ", )
    price = input('What was the price of the item? ')
    quantity = input('How many did you buy?  ', )
    store = input('What store did you buy it from?  ')
    print(item, price, quantity, store)
    print('is there anything else for you today?', '\nY/N')
    user_input = input()
    try:
        if str(user_input) == 'y':
            grocery_list()
        else:
            main_menu()
    except str(ValueError):
        print('Please input a valid answer. Y/N')


main_menu()
