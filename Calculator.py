from init import Init
from Operation import Calc

num1, num2 = Init()
while True:
    opp = input("Enter a operator (+)(-)(*)(/) to exit (Q): ")

    if opp == "q" or opp == "Q":
        print("Exit to calculator")
        break
    result = Calc(num1, num2, opp)
    if result == "Error, /0":
        print("Error, /0")
        break
    elif result == "Invalid operation":
        print("Invalid operation")
        break
    else:
        print(result)