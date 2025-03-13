inputs = []

for i in range(1, 11):
    num = float(input(f"Enter number {i}: "))
    inputs.append(num)

done = []

for num in inputs:
    if num not in done:
        done.append(num)

print(done)