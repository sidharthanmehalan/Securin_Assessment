# Initial regular dice
a = [1, 2, 3, 4, 5, 6]
b = [1, 2, 3, 4, 5, 6]

#These tuples gives the possible number of dots on each face on first and second dice
possible_a = (1, 2, 3, 4)
possible_b = (1, 2, 3, 4, 5, 6, 7, 8)


# Dictionary to store frequency of sums of dice faces
freq = {}

# Dictionary to store frequency of sums of new dice faces
new_freq = {}


# Function to check combinations of dice A
def primary_build(combin_a, indexA):

    if indexA == 5:
        # print(combin_a)
        secondary_build(combin_a, [1, 0, 0, 0, 0, 8], 1)
        return
    for i in possible_a:
        combin_a[indexA] = i
        primary_build(combin_a, indexA + 1)

# Function to check combinations of dice B
def secondary_build(combin_a, combin_b, index):
    if index == 5:
        valid(combin_a, combin_b)
        return
    for i in possible_b:
        combin_b[index] = i
        # print(combin_b,combin_b)
        secondary_build(combin_a, combin_b, index + 1)

# Function to check and compare combination of new dice
def valid(combin_a, combin_b):
    new_freq.clear()
    for i in combin_a:
        for j in combin_b:
            new_freq[i + j] = new_freq.get(i + j, 0) + 1

        if new_freq == freq:

            print("die_a", combin_a)
            print("die_B:", combin_b, "\n")
            exit()


freq = dict()
for i in a:
    for j in b:
        total_sum = i + j
        freq[total_sum] = freq.get(total_sum, 0) + 1

combin_a = [1, 0, 0, 0, 0, 4]
primary_build(combin_a, 1)


