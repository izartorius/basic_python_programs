inputs = {}

while True:
    try:

        num = int(input("Enter a number: "))

        if num in inputs:
            inputs[num] += 1
        else:
            inputs[num] = 1

    except ValueError:
        if inputs:
            most_duplicate = max(inputs, key=inputs.get)
            print(f"The number with the most duplicates is: {most_duplicate}")

