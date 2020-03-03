#!/usr/bin/python3
# -*- coding: Utf-8 -*


"""Modules Load Part File"""

import random
import pygame

from pygame.locals import *
from constantes import *
from classes import *

def main():

    """Initialisation du programme labyrinthe"""

    #initialisation de l'ensemble des modules pygame
    pygame.init()

    #création de la fenêtre
    window = pygame.display.set_mode((COTE_WINDOW, COTE_WINDOW))

    #Titre de la fenêtre
    pygame.display.set_caption("Mac Gyver : The Labyrinth")

    #Images des différents éléments
    BACKGROUND = pygame.image.load("images/background.jpg").convert()
    PERSO = pygame.image.load("images/MacGyver.png").convert_alpha()
    BRICK = pygame.image.load("images/brick.png").convert()
    GUARD = pygame.image.load("images/guard.png").convert_alpha()
    SYRINGE_IMAGE = pygame.image.load("images/syringe.png").convert_alpha()
    TUBE_IMAGE = pygame.image.load("images/tube.png").convert_alpha()
    ETHER_IMAGE = pygame.image.load("images/ether.png").convert_alpha()
    VICTOIRE_ECRAN = pygame.image.load("images/victoire.png").convert()
    DEFAITE_ECRAN = pygame.image.load("images/defaite.png").convert()

    #liste dans laquelle est stockée le tableau de jeu
    ARRAY = []

    #liste contenant les objets récupérés par le joueur
    items = []


    """Génration des éléments et de l'interface graphique"""

    #Labyrinthe.creation(window, ARRAY, BRICK, PERSO, GUARD)
    Labyrinthe.creation(ARRAY)

    Equipment("syringe", ARRAY)
    Equipment("tube", ARRAY)
    Equipment("ether", ARRAY)

    Labyrinthe.affichage(window, ARRAY, BRICK, PERSO, GUARD, SYRINGE_IMAGE, TUBE_IMAGE, ETHER_IMAGE, BACKGROUND)

    continuer = 1
    #variable qui continue la boucle de jeu tant que = 1


    """Boucle de jeu"""

    while continuer:

        #on met à jour l'affichage à partir du tableau actuel
        Labyrinthe.affichage(window, ARRAY, BRICK, PERSO, GUARD, SYRINGE_IMAGE, TUBE_IMAGE, ETHER_IMAGE, BACKGROUND)

        #boucle de recherche d'un évenement clavier avec le mouvement correspondant
        for event in pygame.event.get():
            if event.type == KEYDOWN:

                if event.key == K_RIGHT:
                    Personnage.mouvement(1, 0, ARRAY)

                if event.key == K_LEFT:
                    Personnage.mouvement(-1, 0, ARRAY)

                if event.key == K_UP:
                    Personnage.mouvement(0, -1, ARRAY)

                if event.key == K_DOWN:
                    Personnage.mouvement(0, 1, ARRAY)

        #on vérifie si le personnage rencontre un objet et si oui, on le place dans items
        Personnage.inventaire(items, ARRAY)

        #Boucle pour vérifier que le jeu n'est pas terminé
        for elt in ARRAY:
            if "PERSO" in elt and "GUARD" in elt and len(items) == 3:
                window.blit(VICTOIRE_ECRAN, (0, 0))
                pygame.display.flip()
                continuer = 0
                break
            elif "PERSO" in elt and "GUARD" in elt and len(items) != 3:
                window.blit(DEFAITE_ECRAN, (0, 0))
                pygame.display.flip()
                continuer = 0
                break
            else:
                pass

    #possibilité de recommencer
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_o:
                    main()
                if event.key == K_n:
                    pygame.quit()
                    exit()

if __name__ == "__main__":
    main()
