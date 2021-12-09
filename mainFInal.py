""" A smart Grocery List program, takes your input and builds a list """
__author__ = "Joseph Gerl"

print("Welcome to my Smart list program")
name = input("What is your name? ")


def main():
    """The Entry point to this program"""
    print('Welcome', name, '\nThis is the main menu')

    keep_running = True
    while keep_running:
        try:
            print('Please select an option between 1 - 3')
            print('1: Tutorial')
            print('2: Grocery List')
            print('3: I am Finished for today!')
            menu_choice = int(input('What is your selection? '))
            if menu_choice == 1:
                print('Great Selection! Lets Learn together!')
                tutorial()  # opens the function for basic operations
            elif menu_choice == 2:
                print('Good Choice, Lets work!')
                make_list()
            elif menu_choice == 3:
                print('Have a nice day!')
                keep_running = False
            else:
                # noinspection PyStatementEffect
                0 >= menu_choice > 3
                print('Invalid input, Please try again!')
        except ValueError:
            print('Invalid input, Please try again!')


def tutorial():
    """A tutorial For the basic functions of math and how to add items"""

    print("Before we get too far, lets learn how this system works.")
    print("Basic operations")
    """addition"""
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    print("addition")
    total = num1 + num2
    print(total)
    """ subtraction """
    print("Subtraction")
    difference = num1 - num2
    print(difference)
    """ multiplication """
    print('multiplication')
    product = num1 * num2
    print(product)
    """ division """
    print('division')
    quotient = num1 / num2
    print(quotient)
    """ Floor division """
    print('Floor Division')
    floor_division = num1 // num2
    print(floor_division)
    """ modulus """
    print('remainder')
    remainder = num1 % num2
    print(remainder)
    print('Now for the actual tutorial')
    """ Practice for the actual list generation"""
    print('Simple: Tell me what you need from the grocery store, and i will '
          'make note of it')
    print('If you do not know the details, that is fine, save it for next '
          'time.')
    print('lets try one together')
    grocery_practice()


print("Please input item, cost, quantity and store for your list.")
items = []
costs = []
quantities = []
stores = []


# a simple practice function to see it in action, doesnt record responses
def grocery_practice():
    """Practice at learning how the program collects data."""
    print('This will not be added to your list!')
    item = input("What was this item?  ", )
    price = input('What was the price of the item? ', )
    quantity = input('How many did you buy?  ', )
    store = input('What store did you buy it from?  ', )
    print('Item', 'price', 'quantity', 'store')
    print(item, price, quantity, store)
    print('Now you try!')
    make_list()


def make_list():
    """This is where you will make your list"""
    item = input("Which item do you want?")
    items.append(item)
    cost = input("What is the price?")
    costs.append(cost)
    quantity = input("How many do you want?")
    quantities.append(quantity)
    store = input("Which store does it come from?")
    stores.append(store)
    add_list = True
    while add_list:
        try:
            choices = input("would you like to 1: Add an Item "
                            "2: Delete an item" "3: Print list or 4: Exit?")
            if str(choices) == "1":
                make_list()
            elif str(choices) == "2":
                remove_item()
            elif str(choices) == "3":
                print_list()
            else:
                add_list = False
                print("Have a nice day!")
        except ValueError:
            print('Please Try again.')
        item = input("Which item do you want?")
        items.append(item)
        cost = input("What is the price?")
        costs.append(cost)
        quantity = input("How many do you want?")
        quantities.append(quantity)
        store = input("Which store does it come from?")
        stores.append(store)


def print_list():
    """This is the item to print your list"""
    print("#     item      cost      quantity      store")
    for i in range(len(items)):
        print(" " + str(i) + " " + items[i] + " " + costs[i] + " " +
              quantities[i] + " " + stores[i])


def remove_item():
    """This will help you remove items from the list(BETA FUNCTION)"""
    print("# item cost quantity store")
    for i in range(len(items)):
        print(" " + str(i) + " " + items[i] + " " + costs[i] + " " +
              quantities[i] + " " + stores[i])
    rem_item = int(input("Enter the row number you wish to remove."))
    try:
        rem_item = items.pop(rem_item)
        rem_item = costs.pop(rem_item)
        rem_item = quantities.pop(rem_item)
        rem_item = stores.pop(rem_item)
        print("# item cost quantity store")
        for i in range(len(items)):
            print(
                " " + str(i) + " " + items[i] + " " + costs[i] + " " +
                quantities[i] + " " + stores[i])
    except ValueError:
        print('Value does not exist.')
    except TypeError:
        print('Success')
    except NameError:
        print('Invalid input')
    except IndexError:
        print('please try again')


main()
