import itertools

all_combinations = []

# Generating permutations of 4 to 8 digits from 0 to 9
for r in range(4, 9):
    for combination in itertools.permutations(range(10), r):
        wps_str = ''.join(map(str, combination))
        all_combinations.append(wps_str)

# Writing all combinations to file
with open("WPS_List.txt", "w") as file:
    for combination in all_combinations:
        file.write(combination + "\n")

