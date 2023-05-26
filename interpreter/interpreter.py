x,y,z = input("Expression: ").split(" ")
x = int(x)
z = int(z)
if y == "+":
    print(f"{float(x+z):.1f}")
elif y == "-":
    print(f"{float(x-z):.1f}")
elif y == "*":
    print(f"{float(x*z):.1f}")
else:
    print(f"{float(x/z):.1f}")