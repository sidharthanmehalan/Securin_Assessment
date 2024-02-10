# Calculate total combinations
die_faces = [1, 2, 3, 4, 5, 6]
total_combinations = 0

# The total number of combinations will be number of faces is (die_a X die_b)
for face1 in die_faces:
    for face2 in die_faces:
        total_combinations += 1
print("Total combinations:", total_combinations)

# frequency calculation
frequency = {i: 0 for i in range(2, 13)}
for face1 in die_faces:
    for face2 in die_faces:
        frequency[face1 + face2] += 1

for key, value in frequency.items():
    print(f"Sum = {key}{''if (key>9) else ' '}: {'* ' * value} {'  ' * (6-value)}{value}")

# Calculate sum probabilities
probabilities = {}
for face1 in die_faces:
    for face2 in die_faces:
        sum_val = face1 + face2
        if sum_val in probabilities:
            probabilities[sum_val] += 1
        else:
            probabilities[sum_val] = 1
for key in probabilities:
    probabilities[key] /= total_combinations
print("Probability of all Possible Sums:")
for key, value in probabilities.items():
    print(f"P(Sum = {key}) = {value:.2f}")
