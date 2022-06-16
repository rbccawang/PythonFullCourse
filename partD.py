try:
    val = 10/0
    num = int(input("Enter a number: "))
    print(num)
except ZeroDivisionError as e:
    print(e)
except ValueError:
    print("Invalid Input")