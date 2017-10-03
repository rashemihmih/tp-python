year = int(input("год: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"год {year} високосный")
else:
    print(f"год {year} не високосный")
