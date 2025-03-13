inputs = []

while True:
    try:
        num = float(input("Enter a number: "))
        inputs.append(num)

    except ValueError:
        print(f"The lowest input is {min(inputs)}.")
        break