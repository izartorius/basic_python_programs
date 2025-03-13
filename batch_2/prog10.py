num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num = []

if num1 > num2:
    for i in range(num2 + 1, num1):
        num.append(i)
    print(f"The numbers between {num1} and {num2} is {num}")
elif num1 < num2:
    for i in range(num1 +1, num2):
        num.append(i)
    print(f"The numbers between {num1} and {num2} is {num}")
else:
    print("Both inputs are equal, there are no numbers between them.")