number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(len(number_grid)) #numero righe
print(len(number_grid[0])) #lunghezza prima riga

#loop annidati per accedere a ogni el della lista
#VERSIONE 1
for i in range (len(number_grid)):
    for j in range (len(number_grid[i])):
        print(number_grid[i][j])


#VERSIONE 2
for row in number_grid:
    for col in row:
        print(col)