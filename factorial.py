factorial = input("Enter a whole number: ")


def listFactors(n):
    validInput = False
    while validInput == False:
        try:
            num = int(n)
            validInput = True
        except Exception as err:
            print("invaild integer")
            n = input("Enter a whole number: ")

    count = 1
    while count <= num:
        if num % count == 0:
            print(count)
        count = count + 1
    pass

listFactors(factorial)
