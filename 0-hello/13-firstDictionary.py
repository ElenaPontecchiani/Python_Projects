monthConverter = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"
}

print(monthConverter["Jan"])
print(monthConverter.get("Mar"))
print(monthConverter.get("luv", "Not a valid key"))

#dictionary possono essere con tipi diversi tra chiave/valore
monthAbbr = {
    1 : "January",
    2 : "February",
    3 : "March",
    4 : "April",
    5 : "May",
    6 : "June",
    7 : "July",
    8 : "August",
    9 : "September",
    10 : "October",
    11 : "November",
    12 : "December"
}

print(monthAbbr.items())
print(list(monthAbbr.items()))
monthAbbr.pop(12)
print(list(monthAbbr.items()))

#attenzione che stampa l'el che vado a togliere!!
print(monthAbbr.popitem())