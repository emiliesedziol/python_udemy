# lottery app
# user can pick 6 numbers
# lottery calculates 6 random numbers between 1 and 20)
# Then we match the user numbers to the lottery numbers
# Calculate the winnings based on how many numbers the user matches

import random

def menu():
    user_numbers =get_player_numbers()
    lottery_numbers = create_lottery_numbers()
    intersect_numbers = user_numbers.intersection(lottery_numbers)
    print("User Numbers {} ".format(user_numbers))
    print("Lottery Numbers {} ".format(lottery_numbers))
    print("Matches {} ".format(intersect_numbers))
    print("You one ${}!".format(100 ** len(intersect_numbers)))


def create_lottery_numbers():
    values = set()  # cannot initialise like so: {}
    # for index in range (6):  if the number is generated more than once it will not  be added to set
    while len(values) < 6:
        values.add(random.randint(1, 20))
    return values

def get_player_numbers():
    number_csv = input("Enter your 6 numbers, seperated by commas: ")
    # create a set of integer from this number_csv
    number_list = number_csv.split(",")
    integer_set = {int(number) for number in number_list}
    return integer_set

 # print(get_player_numbers())  #verify this works

# print(create_lottery_numbers())

menu()