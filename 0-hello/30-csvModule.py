import csv
from datetime import datetime
path = "C:\\Users\\elepo\\PycharmProjects\\0-hello\\google_stock_data.csv"
file = open(path, newline="")
reader = csv.reader(file)

#estraggo prima linea che non contiene dati importanti, ma solo l'header
header = next(reader)

#estraggo rimanenti dati, FACENDO ATTENZIONE A METTERE IL TIPO DI DATO GIUSTO, SE NON LO FACESSI SAREBBERO TRATTATI COME STRINGHE!
data = []
for row in reader:
    # row= [Date, Open, High, Low, Close, Volume, Adj.Close
    #    datetime, float, float, float, float, integer, float
    date = datetime.strptime(row[0], "%m%d%Y")
    open_price = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])
    data.append([date, open_price, high, low, close,volume, adj_close])

#vogliamo scrivere sul file le nostre elaborazioni
return_path = "C:\\Users\\elepo\\PycharmProjects\\0-hello\\google_stock_data.csv"
file = open(return_path, "w")
writer = csv.writer(file)
writer.writerow(["Date", "Return"])
#scrittura vera e propria dei dati parte dalla seconda riga
for i in range(len(data)-1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
   