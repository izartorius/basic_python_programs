numbers = []

for i in range(1, 11):
    num = float(input(f"Enter number {i}: "))
    numbers.append(num)

num1 = numbers[0]

for i in range(1, 10):
    diff = num1 - numbers[i]
