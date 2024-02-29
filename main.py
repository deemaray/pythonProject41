# Nesting Homework

a = float(input("Give me a value for a: "))
b = float(input("Give me a value for b: "))
c = float(input("Give me a value for c: "))

# Calculate the discriminant
d = b**2 - 4*a*c

# Check the number of roots
if d > 0:
    root1 = (-b + d**0.5) / (2*a)
    root2 = (-b - d**0.5) / (2*a)
    print("There are 2 roots:", root1, "and", root2)
elif d == 0:
    root = -b / (2*a)
    print("There is 1 root:", root)
else:
    print("There are no real roots.")

quit()











