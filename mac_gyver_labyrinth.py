#!/usr/bin/python3
# -*- coding: Utf-8 -*


"""Modules Load Part File"""

import random

import pygame
from pygame.locals import *


"""Constants Part File"""

#Paramètres de la fenêtre
NOMBRE_SPRITE_COTE = 15
TAILLE_SPRITE = 45
COTE_WINDOW = NOMBRE_SPRITE_COTE * TAILLE_SPRITE


"""Labyrinthe Game Part File"""

pygame.init()
#initialisation de l'ensemble des modules pygame

window = pygame.display.set_mode((COTE_WINDOW, COTE_WINDOW))
#création de la fenêtre

pygame.display.set_caption("Mac Gyver : The Labyrinth")
#Titre de la fenêtre

background = pygame.image.load("images/background.jpg").convert()
window.blit(background, (0, 0))
#chargement et superposition de l'image de fond


"""Constantes"""

PERSO = pygame.image.load("images/MacGyver.png").convert_alpha()
BRICK = pygame.image.load("images/brick.png").convert()
GUARD = pygame.image.load("images/guard.png").convert_alpha()
syringe = pygame.image.load("images/syringe.png").convert_alpha()

ARRAY = []
#liste dans laquelle est stockée le tableau de jeu

items = []
#liste contenant les objets récupérés par le joueur


"""Lecture du fichier txt et conversion dy labyrinthe en image"""

def generate_initial():
    """méthode de lecture du fichier txt, de création du tableau initial et d'affichage graphique initial"""
    with open("level.txt", "r") as generating_file:
    #fonction performante pour travailer sur des fichiers
        content = []
	    #on crée une liste
        for ligne in generating_file:
            content.append(ligne)
        #content.append(generating_file.read())
	    #on ajoute dans la liste le contenu 


    numero_ligne = 0
    for element in content:
        numero_case = 0
        for sprite in element:
            x = numero_case * TAILLE_SPRITE
            y = numero_ligne * TAILLE_SPRITE
            if sprite == "b":
                window.blit(BRICK, (x,y))
                ARRAY.append([x, y, "BRICK"])
            elif sprite == "m":
                window.blit(PERSO, (x,y))
                ARRAY.append([x, y, "PERSO"])
            elif sprite == "g":
                window.blit(GUARD, (x,y))
                ARRAY.append([x, y, "GUARD"])
            else:
                ARRAY.append([x, y])
            numero_case += 1
        numero_ligne += 1

		
"""Génerer les objets aléatoirement"""

def generate_item():
    while True:
        attempt = ARRAY[random.randint(0, 239)]
        if not "BRICK" in attempt and not "PERSO" in attempt and not "GUARD" in attempt:
            attempt.append("syringe")
            break
        else:
            pass



"""Génération du niveau graphique à partir de la lecture de ARRAY"""

def generate_array():
    """Génération du niveau graphique à partir de la lecture de ARRAY"""
    for elt in ARRAY:
        if "BRICK" in elt:
            window.blit(BRICK, (elt[0], elt[1]))
        elif "PERSO" in elt:
            window.blit(PERSO, (elt[0], elt[1]))
        elif "GUARD" in elt:
            window.blit(GUARD, (elt[0], elt[1]))
        elif "syringe" in elt:
            window.blit(syringe, (elt[0], elt[1]))
        else:
            pass


"""Elements d'initialisation"""

generate_initial()
generate_item()
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
                window.blit(background, (0, 0))
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
                        window.blit(background, (0, 0))
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
                        window.blit(background, (0, 0))
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
                        window.blit(background, (0, 0))
                        generate_array()
                        pygame.display.flip()
                        break
                    else:
                        pass
                        
                    
            if event.key == K_LEFT:
                window.blit(background, (0, 0))
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
                        window.blit(background, (0, 0))
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
                        window.blit(background, (0, 0))
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
                        window.blit(background, (0, 0))
                        generate_array()
                        pygame.display.flip()
                        break
                    else:
                        pass
				

            if event.key == K_UP:
                window.blit(background, (0, 0))
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
                        window.blit(background, (0, 0))
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
                        window.blit(background, (0, 0))
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
                        window.blit(background, (0, 0))
                        generate_array()
                        pygame.display.flip()
                        break
                    else:
                        pass
						
						
            if event.key == K_DOWN:
                window.blit(background, (0, 0))
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
                        window.blit(background, (0, 0))
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
                        window.blit(background, (0, 0))
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
                        window.blit(background, (0, 0))
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
        else:
            pass

    #boucle pour vérifier si le jeu est terminé et si oui en bien ou en mal			
    for elt in ARRAY:
        if "PERSO" in elt and "GUARD" in elt and len(items) == 1:
            print("You win.")
            continuer = 0
            break
        elif "PERSO" in elt and "GUARD" in elt and len(items) != 1:
            print("Game over")
            continuer = 0
            break
        else:
            pass