n1 = float(input("First number: "))
n2 = float(input("Second number: "))
operator = input("Digit the operator: ")


def calculatorV2 (n1, n2, operator):
    if operator == '+':
        return n1+n2
    elif operator == '-':
        return n1-n2
    elif operator == '*':
        return n1*n2
    elif operator == '/':
        return n1/n2
    else:
        print("Error, operator not valid")
        return 0


result = calculatorV2(n1, n2, operator)
print(result)

