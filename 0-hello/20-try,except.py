try:
    letter= input("Digit the letter: ")
    if letter=="a":
        num=int(input("Insert the number: "))
    else:
        num=10/0
except ZeroDivisionError:
    print("non si può dividere per zero")
except ValueError:
    print("Number idiot")