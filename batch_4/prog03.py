inputs = []

while True:
    try:
        num = float(input("Enter a number: "))
        inputs.append(num)

    except ValueError:
        print(f"The highest input is {max(inputs)}.")
        break