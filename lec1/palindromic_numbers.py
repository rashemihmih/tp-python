print(max(i * j for i in range(1, 1000) for j in range(1, 1000) if str(i * j) == str(i * j)[::-1]))
