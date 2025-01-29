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

    for i in range(1, n + 1): # toggle every round door

        for j, door in enumerate(range(i - 1, n, i), start=1): # toggle every ith door

            doors[door] = not doors[door] # toggle door

            print(f"i: {i}; j:{door + 1}; step size: {i}. Toggling door number {door + 1}.") # print door toggling

    print("Algorithm has finished.\n") # algorithm termination statement

    ##### print each door #####

    for i, door in enumerate(doors, start=1): # print each door using enumerate starting at 1

        state = "open" if door else "closed" # determine door state

        print(f"Door number {i} remains {state}.") # print door state


########## RUN ALGORITHM ##########

##### run algorithm #####

n = int(input("Enter the number of Doors (N): ")) # ask user for number of doors

print(n_doors_algorithm(n)) # run n doors algorithm