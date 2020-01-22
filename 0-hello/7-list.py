#SINTASSI GENERALE
general_list=["Kevin", 2, True]
friends=["Kevin", "Tim", "Tom"]
print(friends)
print(friends[1])
print(friends[-1])
print(friends[1:])
friends[2]= "Karen"
print(friends)
letters=["a", "b", "c", "d", "e", "f"]
print(letters[1:3])


#FUNZIONI CON LE LISTE
lucky_numbers= [12,4,6,8,10]
letters.extend(lucky_numbers)
print(letters)
#non so perchè fare cosi non funziona e dice che la lista è vuota: print(letters.append(lucky_numbers))
friends.append("Hellen")
print(friends)
friends.insert(3, "Kelly")
print(friends)
friends.remove("Kelly")
print(friends)
letters.clear()
print(letters)
friends.pop()
print(friends)
print(friends.index("Tim"))
#print(friends.index("Hanna")) -->lancia errore perchè hanna non è in lista
friends.append("Kim")
friends.append("Tim")
print(friends.count("Tim"))
friends.sort()
print(friends)
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
friends2= friends.copy()
print(friends2)