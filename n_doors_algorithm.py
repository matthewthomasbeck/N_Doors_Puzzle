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

        for i in range(round - 1, n, round): # toggle every round door starting from round - 1 index

            doors[i] = not doors[i] # toggle door

    return doors # return list of doors


########## RUN ALGORITHM ##########

##### call n doors function to run the algorithm #####

print(n_doors_algorithm(100)) # can work with any n doors