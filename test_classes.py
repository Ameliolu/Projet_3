from random import shuffle, randrange

from classes import *

def test_make_maze():

    s = Labyrinthe.make_maze()

    #partie test
    chemin = False
    # la première possibilité est le "o" toujours situé juste après "m" sur la 2e ligne, attention au - 1 du fait de la liste
    possibilite = [16]
    # lsite destinée à accueillir les possibilités déjà testées afin de ne pas les retester
    deja_vu = []

    while len(possibilite) > 0:
        #print(s[possibilite[0]])
       
        if s[possibilite[0] + 1] == "g":
            chemin = True
            break
       
        if s[possibilite[0] + 1] == "o":
            if possibilite[0] + 1 not in deja_vu:
                possibilite.append(possibilite[0] + 1)
               
        if s[possibilite[0] - 1] == "o":
            if possibilite[0] - 1 not in deja_vu:
                possibilite.append(possibilite[0] - 1)

        if s[possibilite[0] + 15] == "o":
            if possibilite[0] + 15 not in deja_vu:
                possibilite.append(possibilite[0] + 15)
                  
        if s[possibilite[0] - 15] == "o":
            if possibilite[0] - 15 not in deja_vu:
                possibilite.append(possibilite[0] - 15)

        deja_vu.append(possibilite[0])
        del possibilite[0]
        
    assert chemin == True
    assert len(s) == 225