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

def n_doors_algorithm(n): # function to implement n doors algorithm

    ##### initialize variables #####

    doors = [False] * n # create a list of closed n doors

    ##### loop through however many n times #####

    for round in range(1, n + 1): # loop through each round

        ##### adjust each door #####

        for i in range(1, n + 1): # toggle every round door

            for j in range(round, n + 1, round): # j starts from round and then goes in steps

                doors[j - 1] = not doors[j - 1] # toggle door at position j - 1

                print(f"i: {round}; j: {j}; step size: {round}. Toggling door number {j}.") # print step

    print("Algorithm has finished.\n") # algorithm termination statement

    ##### print each door #####

    for i in range(n): # loop through all doors this time

        if doors[i]: # if a door is true...

            print(f"Door number {i + 1} remains open.") # print that the door is open

        else: # if a door is false...

            print(f"Door number {i + 1} remains closed.") # print that the door is closed


########## RUN ALGORITHM ##########

##### run algorithm #####

n = int(input("Enter the number of Doors (N): ")) # ask user for number of doors

print(n_doors_algorithm(n)) # run n doors algorithm