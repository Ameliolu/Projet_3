#!/usr/bin/python3
# -*- coding: Utf-8 -*


"""Modules Load Part File"""

import random

import pygame
from pygame.locals import *

from constantes import *


"""Initialisation du programme labyrinthe"""

pygame.init()
#initialisation de l'ensemble des modules pygame

window = pygame.display.set_mode((COTE_WINDOW, COTE_WINDOW))
#création de la fenêtre

pygame.display.set_caption("Mac Gyver : The Labyrinth")
#Titre de la fenêtre

#Images des différents éléments
BACKGROUND = pygame.image.load("images/background.jpg").convert()
PERSO = pygame.image.load("images/MacGyver.png").convert_alpha()
BRICK = pygame.image.load("images/brick.png").convert()
GUARD = pygame.image.load("images/guard.png").convert_alpha()
SYRINGE_IMAGE = pygame.image.load("images/syringe.png").convert_alpha()
TUBE_IMAGE = pygame.image.load("images/tube.png").convert_alpha()
ETHER_IMAGE = pygame.image.load("images/ether.png").convert_alpha()

#chargement et superposition de l'image de fond
window.blit(BACKGROUND, (0, 0))

#liste dans laquelle est stockée le tableau de jeu
ARRAY = []

#liste contenant les objets récupérés par le joueur
items = []


""""Class part"""

class Equipment:
    """Génére des items positionnés aléatoirement"""
    def __init__(self, name):
        while True:
            attempt = ARRAY[random.randint(0, len(ARRAY) - 1)]
            #après avoir selectionné au hasard un des éléments de ARRAY, on vérifie qu'il n'y a rien dans la case
            if len(attempt) == 2:
                attempt.append(name)
                break
            else:
                pass


"""Fonctions de génération graphique"""

def generate_initial():
    """méthode de lecture du fichier txt, de création du tableau initial et d'affichage graphique initial"""
    with open("level.txt", "r") as generating_file:
    #fonction performante pour travailer sur des fichiers
        content = []
	    #on crée une liste
        for ligne in generating_file:
            #on enlève le caractère de saut de ligne
            ligne_clear = ligne.rstrip("\n")
            content.append(ligne_clear)
            #on ajoute dans la liste le contenu

    numero_ligne = 0
    for element in content:
        numero_case = 0
        for sprite in element:
            x = numero_case * TAILLE_SPRITE
            y = numero_ligne * TAILLE_SPRITE
            if sprite == "b":
                window.blit(BRICK, (x, y))
                ARRAY.append([x, y, "BRICK"])
            elif sprite == "m":
                window.blit(PERSO, (x, y))
                ARRAY.append([x, y, "PERSO"])
            elif sprite == "g":
                window.blit(GUARD, (x, y))
                ARRAY.append([x, y, "GUARD"])
            else:
                # le cas du caractère o dans le fichier
                ARRAY.append([x, y])
            numero_case += 1
        numero_ligne += 1


def generate_array():
    """Génération du niveau graphique à partir de la lecture de ARRAY
    Si la fonction trouve un élément dans la case, elle l'affiche aux coordonnées
    de la case (ses deux premiers éléments)"""
    for elt in ARRAY:
        if "BRICK" in elt:
            window.blit(BRICK, (elt[0], elt[1]))
        if "PERSO" in elt:
            window.blit(PERSO, (elt[0], elt[1]))
        if "GUARD" in elt:
            window.blit(GUARD, (elt[0], elt[1]))
        if "syringe" in elt:
            window.blit(SYRINGE_IMAGE, (elt[0], elt[1]))
        if "tube" in elt:
            window.blit(TUBE_IMAGE, (elt[0], elt[1]))
        if "ether" in elt:
            window.blit(ETHER_IMAGE, (elt[0], elt[1]))
        else:
            pass


"""Génration des éléments et de l'interface graphique"""

generate_initial()

Equipment("syringe")
Equipment("tube")
Equipment("ether")

generate_array()

pygame.display.flip()
#rafraîchissmement de l'écran de façon à MAJ les images

continuer = 1
#variable qui continue la boucle de jeu tant que = 1


"""Boucle de jeu"""

while continuer:

    #on rafraîchit au cas où
    pygame.display.flip()

    #boucle de recherche d'un évenement clavier
    for event in pygame.event.get():
        if event.type == KEYDOWN:

            if event.key == K_RIGHT:
                window.blit(BACKGROUND, (0, 0))
                generate_array()
                position_x = 0
                position_y = 0
                position_initiale = 0

                #boucle pour enregistrer la nouvelle position souhaitée de PERSO et l'enlever de sa liste actuelle
                for elt in ARRAY:
                    if "PERSO" in elt:
                        position_x = elt[0] + TAILLE_SPRITE
                        position_y = elt[1]
                        position_initiale = ARRAY.index(elt)
                        elt.remove("PERSO")
                        #print(position_initiale)
                        window.blit(BACKGROUND, (0, 0))
                        generate_array()
                        pygame.display.flip()
                        break
                    else:
                        pass

				#boucle pour vérifier qu'il n'y ait pas de collision avec les BRICK
                for elt in ARRAY:
                    #if position_x in elt:
                    if elt[0] == position_x and elt[1] == position_y and "BRICK" in elt:
                        ARRAY[position_initiale].append("PERSO")
                        window.blit(BACKGROUND, (0, 0))
                        generate_array()
                        pygame.display.flip()
                        break
                    else:
                        pass

				#boucle pour mettre le PERSO dans sa liste vérifiée d'arrivée
                for elt in ARRAY:
                    if elt[0] == position_x and elt[1] == position_y and not "BRICK" in elt:
                    #if not "PERSO" in elt:
                        elt.append("PERSO")
                        window.blit(BACKGROUND, (0, 0))
                        generate_array()
                        pygame.display.flip()
                        break
                    else:
                        pass


            if event.key == K_LEFT:
                window.blit(BACKGROUND, (0, 0))
                generate_array()
                position_x = 0
                position_y = 0
                position_initiale = 0

                #boucle pour enregistrer la nouvelle position souhaitée de PERSO et l'enlever de sa liste actuelle
                for elt in ARRAY:
                    if "PERSO" in elt:
                        position_x = elt[0] - TAILLE_SPRITE
                        position_y = elt[1]
                        position_initiale = ARRAY.index(elt)
                        elt.remove("PERSO")
                        #print(position_initiale)
                        window.blit(BACKGROUND, (0, 0))
                        generate_array()
                        pygame.display.flip()
                        break
                    else:
                        pass

				#boucle pour vérifier qu'il n'y ait pas de collision avec les BRICK
                for elt in ARRAY:
                    #if position_x in elt:
                    if elt[0] == position_x and elt[1] == position_y and "BRICK" in elt:
                        ARRAY[position_initiale].append("PERSO")
                        window.blit(BACKGROUND, (0, 0))
                        generate_array()
                        pygame.display.flip()
                        break
                    else:
                        pass

				#boucle pour mettre le PERSO dans sa liste vérifiée d'arrivée
                for elt in ARRAY:
                    if elt[0] == position_x and elt[1] == position_y and not "BRICK" in elt:
                    #if not "PERSO" in elt:
                        elt.append("PERSO")
                        window.blit(BACKGROUND, (0, 0))
                        generate_array()
                        pygame.display.flip()
                        break
                    else:
                        pass


            if event.key == K_UP:
                window.blit(BACKGROUND, (0, 0))
                generate_array()
                position_x = 0
                position_y = 0
                position_initiale = 0

                #boucle pour enregistrer la nouvelle position souhaitée de PERSO et l'enlever de sa liste actuelle
                for elt in ARRAY:
                    if "PERSO" in elt:
                        position_x = elt[0]
                        position_y = elt[1] - TAILLE_SPRITE
                        position_initiale = ARRAY.index(elt)
                        elt.remove("PERSO")
                        #print(position_initiale)
                        window.blit(BACKGROUND, (0, 0))
                        generate_array()
                        pygame.display.flip()
                        break
                    else:
                        pass

				#boucle pour vérifier qu'il n'y ait pas de collision avec les BRICK
                for elt in ARRAY:
                    #if position_x in elt:
                    if elt[0] == position_x and elt[1] == position_y and "BRICK" in elt:
                        ARRAY[position_initiale].append("PERSO")
                        window.blit(BACKGROUND, (0, 0))
                        generate_array()
                        pygame.display.flip()
                        break
                    else:
                        pass

				#boucle pour mettre le PERSO dans sa liste vérifiée d'arrivée
                for elt in ARRAY:
                    if elt[0] == position_x and elt[1] == position_y and not "BRICK" in elt:
                    #if not "PERSO" in elt:
                        elt.append("PERSO")
                        window.blit(BACKGROUND, (0, 0))
                        generate_array()
                        pygame.display.flip()
                        break
                    else:
                        pass


            if event.key == K_DOWN:
                window.blit(BACKGROUND, (0, 0))
                generate_array()
                position_x = 0
                position_y = 0
                position_initiale = 0

                #boucle pour enregistrer la nouvelle position souhaitée de PERSO et l'enlever de sa liste actuelle
                for elt in ARRAY:
                    if "PERSO" in elt:
                        position_x = elt[0]
                        position_y = elt[1] + TAILLE_SPRITE
                        position_initiale = ARRAY.index(elt)
                        elt.remove("PERSO")
                        #print(position_initiale)
                        window.blit(BACKGROUND, (0, 0))
                        generate_array()
                        pygame.display.flip()
                        break
                    else:
                        pass

				#boucle pour vérifier qu'il n'y ait pas de collision avec les BRICK
                for elt in ARRAY:
                    #if position_x in elt:
                    if elt[0] == position_x and elt[1] == position_y and "BRICK" in elt:
                        ARRAY[position_initiale].append("PERSO")
                        window.blit(BACKGROUND, (0, 0))
                        generate_array()
                        pygame.display.flip()
                        break
                    else:
                        pass

				#boucle pour mettre le PERSO dans sa liste vérifiée d'arrivée
                for elt in ARRAY:
                    if elt[0] == position_x and elt[1] == position_y and not "BRICK" in elt:
                    #if not "PERSO" in elt:
                        elt.append("PERSO")
                        window.blit(BACKGROUND, (0, 0))
                        generate_array()
                        pygame.display.flip()
                        break
                    else:
                        pass

    #on rafraîchit après l'évenement clavier	
    pygame.display.flip()

    #boucle pour ajouter les items à l'inventaire
    for elt in ARRAY:
        if "PERSO" in elt and "syringe" in elt:
            elt.remove("syringe")
            items.append("syringe")
            generate_array()
            pygame.display.flip()
            break
        if "PERSO" in elt and "tube" in elt:
            elt.remove("tube")
            items.append("tube")
            generate_array()
            pygame.display.flip()
            break
        if "PERSO" in elt and "ether" in elt:
            elt.remove("ether")
            items.append("ether")
            generate_array()
            pygame.display.flip()
            break
        else:
            pass

    #boucle pour vérifier si le jeu est terminé en récupérant les 3 objets, dans le cas contraire game over
    for elt in ARRAY:
        if "PERSO" in elt and "GUARD" in elt and len(items) == 3:
            print("You win.")
            continuer = 0
            break
        elif "PERSO" in elt and "GUARD" in elt and len(items) != 3:
            print("Game over.")
            continuer = 0
            break
        else:
            pass
