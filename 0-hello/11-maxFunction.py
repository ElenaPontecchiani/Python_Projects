def max (n1,n2,n3):
    if n1>=n2 and n1>=n3:
        return n1
    elif n2>=n1 and n2>=n3:
        return n2
    else:
        return n3

n1=float(input("First number: "))
n2=float(input("Second number: "))
n3=float(input("Third number: "))
max=max(n1,n2,n3)
print(max)