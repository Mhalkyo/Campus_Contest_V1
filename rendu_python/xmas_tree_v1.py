# This program prints a simple Christmas Tree.


'''
Generating top branches module, input = number of blank space, number of starting "stars" (top of the module),
number of branches (row of stars).
'''


def top_branches():

    nb_spaces = 15
    stars_top = 1
    nb_branches = 4

    for i in range(nb_branches):
        print(" " * nb_spaces, "*" * stars_top)
        nb_spaces -= 1
        stars_top += 2


'''
Generating middle branches module, input = number of blank space, number of starting "stars" (top of the module),
number of branches (row of stars). 
'''


def mid_branches():

    nb_spaces = 14
    stars_top = 3
    nb_branches = 4

    for i in range(nb_branches):
        print(" " * nb_spaces, "*" * stars_top)
        nb_spaces -= 2
        stars_top += 4


'''
Generating bottom branches module, input = number of blank space, number of starting "stars" (top of the module),
number of branches (row of stars). 
'''


def bot_branches():

    nb_spaces = 13
    stars_top = 5
    nb_branches = 4

    for i in range(nb_branches):
        print(" " * nb_spaces, "*" * stars_top)
        nb_spaces -= 3
        stars_top += 6


'''
function that call the other functions
'''


def main():
    top_branches()
    mid_branches()
    bot_branches()


main()
