elements = [2, 1, 5, 2, 4, 3, 1, 4]

solution_dict = {}

for e in elements:
    solution_dict[e] = solution_dict.setdefault(e, 0) + 1

print([key for key, value in solution_dict.items() if value == 1])
