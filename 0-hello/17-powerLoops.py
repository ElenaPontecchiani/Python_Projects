base = float(input("Enter the base: "))
pow = int(input("Enter the power: "))


#versione 1
def power (base, pow):
    i=0
    result = 1
    while i<pow:
        result=result*base
        i+=1

    return result

print(power(base, pow))


#versione 2
def power2 (base, pow):
    result = 1
    for i in range(pow): #range(INTERO), se lo faccio con float non va
        result = result * base
    return result

print(power2(base, pow))