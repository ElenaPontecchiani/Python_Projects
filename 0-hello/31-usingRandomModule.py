import random
'''RISOLUZIONE DEL PROBLEMA DEL CAMMINO RANDOM CON MONTECARLO'''

def random_walk(n):
    '''Return coordinates after n block random walk'''
    #posizione identificata con coordinate x,y inizialmente =0
    x, y = 0, 0
    for i in range(n):
        '''Nord= incremento y, x invariata = (0,1)
           Sud= decremento y, x invariata = (0,-1)
           Est= y invariata, incremento x = (1,0)
           Ovest= y invariata, decremento x = (-1,0)
        '''
        (dx,dy) = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
        x += dx
        y += dy
    return (x,y)

number_of_walks = 10000 #numero di cammini che analizziamo

for walk_length in range(1,31):
    no_transport = 0 #numero di cammini distanti <=4 blocchi da casa
    for i in range(number_of_walks):
        (x,y) = random_walk(walk_length)
        distance = abs(x) + abs(y)
        if distance<=4:
            no_transport += 1
    no_transport_percentage = float(no_transport) / number_of_walks
    print("Walk size= ", walk_length, "& % of no transport", no_transport_percentage * 100)

