inputs = []

while True:
    try:
        num = float(input("Enter a number: "))
        inputs.append(num)
        inputs.sort(reverse=True)

    except ValueError:
        print(inputs)
        break