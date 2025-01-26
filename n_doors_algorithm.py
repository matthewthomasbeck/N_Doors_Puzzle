################################################################################
# This code and its associated files were created at the instruction of        #
# professors at the University of Texas at San Antonio during my time as a     #
# student at the university. I, as a student, was not responsible for the idea #
# behind this code (i.e. project guidelines, functionality, and end purpose),  #
# but I, Matthew Thomas Beck, can confirm that myself and any project partners #
# (if applicable) were the ones responsible for writing it.                    #
################################################################################





#################################################
############### N DOORS ALGORITHM ###############
#################################################


########## N DOORS FUNCTION ##########

def n_doors_algorithm(n): # function to implement the n doors algorithm

    ##### initialize variables #####

    doors = [False] * n # create a list of n doors, all closed

    ##### loop through each door #####

    for i in range(n): # iterate through the doors and open them

        doors[i] = not doors[i]

    ##### loop through each 2nd door #####

    for i in range(1, n, 2): # iterate through every 2nd door and open them

        doors[i] = not doors[i]

    ##### loop through each 3rd door #####

    for i in range(2, n, 3): # iterate through every 3rd door and open them

        doors[i] = not doors[i]

    ##### loop through each 4th door #####

    for i in range(3, n, 4): # iterate through every 4th door and open them

        doors[i] = not doors[i]

    ##### loop through each 5th door #####

    for i in range(4, n, 5): # iterate through every 5th door and open them

        doors[i] = not doors[i]

    ##### loop through each 6th door #####

    for i in range(5, n, 6): # iterate through every 6th door and open them

        doors[i] = not doors[i]

    ##### loop through each nth door #####

    for i in range(n-1, n, n): # iterate through every nth door and open them

        doors[i] = not doors[i]

    return doors


########## RUN ALGORITHM ##########

##### call n doors function to run the algorithm #####

print(n_doors_algorithm(10)) # can work with any n doors