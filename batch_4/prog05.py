inputs = []

while True:
    try:
        num = float(input("Enter a number: "))
        inputs.append(num)

        total = sum(inputs)
        count = len(inputs)
        average = total / count