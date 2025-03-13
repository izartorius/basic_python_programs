inputs = []

while True:
    try:
        num = float(input("Enter a number: "))
        inputs.append(num)
        inputs.sort()

    except ValueError:
        print(inputs)
        break