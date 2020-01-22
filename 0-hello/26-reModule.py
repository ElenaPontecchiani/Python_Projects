import re
#programma che individua una mail in una stringa composta da testo casuale prima e dopo la mail
random_text_string= "random text. MynameMysurname123@website.com other random text"

#dove:
#[a-zA-Z0-9]: tutte minuscole/maiuscole/numeri
#[a-zA-Z0-9]: tutte minuscole/maiuscole
#\.: al punto serve carattere di escape
#+ : concatenazione stringa
#+ finale: serve per prendere tutto pezzo che soddidisfa, non solo il primo caratettre
pattern = re.compile("[a-zA-Z0-9\.\-\_\(\)]+@+[a-zA-Z0-9]+\.+[a-zA-Z]+")
result = pattern.search(random_text_string)
print(result)

#ma se avessi due email nella stringa casuale di testo?
random_text_string2= "random text. MynameMysurname123@website.com other random text. YourName888@company.net"
pattern = re.compile("[a-zA-Z0-9]+@+[a-zA-Z0-9]+\.+[a-zA-Z09]")
result = pattern.findall(random_text_string2)
print(result)