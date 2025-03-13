inputs = []

for i in range(1, 11):
    num = float(input(f"Enter number {i}: "))
    inputs.append(num)

dupes = []

for num in inputs:
    if inputs.count(num) > 1:
        dupes.append(num)

print("The inputs that have duplicates are:")
for num in dupes:
    print(num)