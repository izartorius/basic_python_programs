num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
num3 = float(input("Enter the 3rd number: "))
total = num1 + num2 + num3

for i in range(4, 11):
    num = float(input(f"Enter the {i}th number: "))
    total += num

print(f"The sum of all numbers is {total}")