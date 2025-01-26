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

def n_doors_algorithm(n):

    doors = [False] * n

    for i in range(n):
        for j in range(i, n, i + 1):
            doors[j] = not doors[j]

    open_doors = []
    for i in range(n):
        if doors[i]:
            open_doors.append(i + 1)

    return open_doors


########## RUN ALGORITHM ##########

##### call n doors function to run the algorithm #####

print(n_doors_algorithm(10)) # can work with any n doors