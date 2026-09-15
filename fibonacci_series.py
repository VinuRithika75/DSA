
try:
    n = int(input("Enter a positive integer: "))

    if n <= 0:
        print("Invalid input")
    else:
        a = 0
        b = 1

        for i in range(n):
            print(a, end=" ")
            c = a + b
            a = b
            b = c

except ValueError:
    print("Invalid input")