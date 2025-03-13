inputs = []

while True:
    try:

        num = int(input("Enter a number: "))

        if num in inputs:
            inputs[num] += 1
        else:
            inputs[num] = 1


