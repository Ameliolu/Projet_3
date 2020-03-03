from random import shuffle, randrange

from classes import *
from constantes import *

def test_make_maze():
    """test qui vérifie qu'une chemin vers la sortie existe pour 10 générations"""
    
    for i in range(1,10):
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
    
def test_creation():
    """vérfie que le tableau généré est conforme (nb, taille et contenu des éléments)"""
    array = []
    Labyrinthe.creation(array)
    
    compteur_perso = 0
    compteur_garde = 0
    
    for elt in array:
    
        #on vérifie que les elt du tableau contiennent au moins une paire de coordonnées
        assert len(elt) > 1
        
        for i in elt:
            if type(i) is int:
                #on vérifie que les coordonnées sont composées de la taille de base des élt à l'affichage
                assert i % TAILLE_SPRITE == 0
            
            if i == "PERSO":
                compteur_perso += 1
                
            if i == "GUARD":
                compteur_garde += 1
    
    #on vérifie qu'il n'y a bien qu'un seul garde et un seul perso dans le tableau
    assert compteur_garde == 1
    assert compteur_perso == 1
    #on vérifie que le tableau comprend bien 225 élt
    assert len(array) == 225