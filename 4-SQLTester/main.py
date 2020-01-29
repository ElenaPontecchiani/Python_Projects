import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="testdb"
)
#verifico se ha creato connessione!
print(mydb)

#inizializzazione cursor
mycursor =mydb.cursor()

#ESECUZIONE QUERY SQL ATTRAVERSO OGGETTO CURSOR
#creazione db
#mycursor.execute("CREATE DATABASE testdb")
#far vedere database che ci sono
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)

#creazione tabella
#mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")
#vedere se tab creata correttamente
mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)

#inserimento dati nelle tab in 4 step: creazione formula con parametri, creazione dati in tuple, eseguire formula inserendo dati, salvataggio modifiche
#1
sqlInsertStudentFormula = "INSERT INTO students(name,age) VALUES (%s, %s)"
#2
student1 =("Rachel", 22)
#3
mycursor.execute(sqlInsertStudentFormula, student1)
#4
mydb.commit()

#inserimento di più valori alla volta
students1 =[
    ("Bob", 17),
    ("Tim", 21),
    ("Tom", 26),
    ("Jay", 16),
    ("Kim", 34),
    ("Ann", 9)
]
mycursor.executemany(sqlInsertStudentFormula, students1)
mydb.commit()

#select and getting data
mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

#se voglio selezionare solo l'eta
mycursor.execute("SELECT age FROM students")
myresult2 = mycursor.fetchall()
for row in myresult2:
    print(row)

#query avanzate con where
sqlAdvanced1 = "SELECT * FROM students WHERE age=17"
mycursor.execute(sqlAdvanced1)
myresult3 = mycursor.fetchall()
for result in myresult3:
    print(result)

#query avanzate con anche wildcard
sqlAdvanced2 = "SELECT * FROM students WHERE name LIKE '%im'"
mycursor.execute(sqlAdvanced2)
myresult4 = mycursor.fetchall()
for result in myresult4:
    print(result)

#aggiornare dati
updateFormula = "UPDATE students SET age = 13 WHERE name='Tim'"
mycursor.execute(updateFormula)
mydb.commit()


#limitare i risultati
limitFormula = "SELECT * FROM students LIMIT 5"
mycursor.execute(limitFormula)
myresult5 = mycursor.fetchall()
for result in myresult5:
    print(result)

#ordinare i risultati in base a una colonna
orderNameFormula = "SELECT * FROM students ORDER BY name"
mycursor.execute(orderNameFormula)
myresult6 = mycursor.fetchall()
for result in myresult6:
    print(result)


orderAgeReverseFormula = "SELECT * FROM students ORDER BY age DESC"
mycursor.execute(orderAgeReverseFormula)
myresult7 = mycursor.fetchall()
for result in myresult7:
    print(result)

#eliminare righe
deleteFormula = "DELETE FROM students WHERE name='Tim'"
mycursor.execute(deleteFormula)
mydb.commit()

#eliminare tabella
#formula = "DROP TABLE IF EXSIST students"