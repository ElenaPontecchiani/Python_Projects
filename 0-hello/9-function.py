def say_hi(name, age):
    print("Hello " +name)
    print("You're "+age)

name_input=input("Insert the name to say hi to: ")
age_input=input("Insert age: ")
say_hi(name_input, age_input)

def cube (base):
    return base*base*base
    #dopo lo statement di return si ritorna al flusso normale del programma e non viene più processata alcuna istruzione
    #se per esempio mettessi un print qua non servirebbe a niente

base_input=input("Insert the base: ")
result= cube(float(base_input))
print(result)