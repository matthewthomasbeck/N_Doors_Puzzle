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

        for i in range(round - 1, n, round): # toggle every round door starting from round - 1 index

            if n % i == 0:

                doors[i] = not doors[i] # toggle door

                print(f"i: {i}; j: PLACEHOLDER; step size: {n % i}. Toggling door number {i}.")

        ##### print each door #####

        for i in range(round - 1, n, round): # toggle every round door starting from round - 1 index

            doors[i] = not doors[i] # toggle door

            if doors[i] == True:

                print(f"Door number {i + 1} remains open.")

            else:

                print(f"Door number {i + 1} remains closed.")


########## RUN ALGORITHM ##########

##### run algorithm #####

n = int(input("Enter the number of Doors (N): ")) # ask user for number of doors

print(n_doors_algorithm(n)) # run n doors algorithm