inputs = []

for i in range(1, 11):
    num = float(input(f"Enter number {i}: "))
    inputs.append(num)

unique = []

for num in inputs:
    if inputs.count(num) == 1:
        unique.append(num)

print("The numbers that have no duplicates are:")
for num in unique:
    print(num)