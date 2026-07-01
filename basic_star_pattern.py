n = int(input("Enter n to print a nxn star pattern: "))
for i in range(n):
    star = ""
    for j in range(n):
        star += " * "
    print(star)