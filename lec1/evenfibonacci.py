a = 1
b = 2
total = 0
while b < 4_000_000:
    a, b = b, a + b
    if a % 2 == 0:
        total += a
print(total)
