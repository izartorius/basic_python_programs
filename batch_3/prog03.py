inputs = []

while True:
    try:
        num = float(input("Enter a number: "))

        if num in inputs:
            print("Duplicate")
        else:
            print("Unique")
            inputs.append(num)