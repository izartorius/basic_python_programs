odd = []

for i in range(10):
    num = float(input("Enter a number: "))
    if num % 2 != 0:
        odd.append(num)

print(f"There are {len(odd)} odd numbers, {odd}")