num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
diff = num1 - num2
diff2 = num2 - num1

if num1 < num2:
    print(f"The difference of both numbers is: {diff2}")
else:
    print(f"The difference of both numbers is: {diff}")