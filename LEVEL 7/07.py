n = int(input("Enter number:"))

for i in range(1, n + 1):
    print(" "*(n - i))
    print("*" * (2 * i - 1))
    print(" ")
