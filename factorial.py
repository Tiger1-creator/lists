def factorial():
    num = int(input("Enter any number you want: "))
    if num == 0 or num == 1:
        print(1)
    else:
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        print(fact)

factorial()