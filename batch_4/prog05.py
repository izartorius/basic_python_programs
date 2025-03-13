inputs = []

while True:
    try:
        num = float(input("Enter a number: "))
        inputs.append(num)

    except ValueError:
        if inputs:
            total = sum(inputs)
            count = len(inputs)
            ave = total / count

            print(f"The average of the inputs is {ave}")
            break