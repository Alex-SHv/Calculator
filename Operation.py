def Calc(num1, num2, opp):
    if opp == "+":
        return num1 + num2
    elif opp == "-":
        return num1 - num2
    elif opp == "*":
        return num1 * num2
    elif opp == "/":
        if num2 == 0:
            return "Error, /0"
        else:
            return num1 / num2
    else:
        return "Invalid operation"