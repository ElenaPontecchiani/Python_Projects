employee_file = open("employee.txt", "r")
#buona prassi verificare prima di tutto che il file sia leggibile
print(employee_file.readable())
#print(employee_file.read()) #legge tutto il file
print(employee_file.readline())
#per le rimanenti righe scorro ogni riga e stampo ogni valore per riga
for employee in employee_file.readlines():
    print(employee)
employee_file.close()


#aggiungere employee alla fine
employee_file = open("employee.txt", "a")

employee_file.write("\nToby - Human resources" )

employee_file.close()