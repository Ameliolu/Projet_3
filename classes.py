"""Classes part file"""


from random import shuffle, randrange
from constantes import *
from mac_gyver_labyrinth import *

class Equipment:
    """Génére des items positionnés aléatoirement"""
    def __init__(self, name, ARRAY):
        while True:
            attempt = ARRAY[random.randint(0, len(ARRAY) - 1)]
            #après avoir selectionné au hasard un des éléments de ARRAY, on vérifie qu'il n'y a rien dans la case
            if len(attempt) == 2:
                attempt.append(name)
                break
            else:
                pass

class Personnage:
    """Classe qui gère les méthodes relatives au personnage"""
    def __init__(self):
        pass

    def mouvement(x, y, ARRAY):
        """"fonction qui gère les déplacements"""
        position_x = 0
        position_y = 0
        position_initiale = 0

        #boucle pour enregistrer la nouvelle position souhaitée de PERSO et l'enlever de sa liste actuelle
        for elt in ARRAY:
            if "PERSO" in elt:
                position_x = elt[0] + (x * TAILLE_SPRITE)
                position_y = elt[1] + (y * TAILLE_SPRITE)
                position_initiale = ARRAY.index(elt)
                elt.remove("PERSO")
                break
            else:
                pass

        #boucle pour vérifier qu'il n'y ait pas de collision avec les BRICK
        for elt in ARRAY:
            if elt[0] == position_x and elt[1] == position_y and "BRICK" in elt:
                ARRAY[position_initiale].append("PERSO")
                break
            else:
                pass

		#boucle pour mettre le PERSO dans sa liste vérifiée d'arrivée
        for elt in ARRAY:
            if elt[0] == position_x and elt[1] == position_y and not "BRICK" in elt:
                elt.append("PERSO")
                break
            else:
                pass

        #on rafraîchit après l'évenement clavier	
        pygame.display.flip()

    def inventaire(items, ARRAY):
        """fonction qui sert à gérer l'inventaire"""
        for elt in ARRAY:
            if "PERSO" in elt and "syringe" in elt:
                elt.remove("syringe")
                items.append("syringe")
                break
            if "PERSO" in elt and "tube" in elt:
                elt.remove("tube")
                items.append("tube")
                break
            if "PERSO" in elt and "ether" in elt:
                elt.remove("ether")
                items.append("ether")
                break
            else:
                pass

class Labyrinthe:
    def __init__(self):
        pass
		
    def make_maze(w = 7, h = 7):
        """Fonction de génération aléatoire d'un labyrinthe adaptée du code disponible sur https://rosettacode.org/wiki/Maze_generation#Python"""
        vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
        vertical = [["bo"] * w + ['b'] for _ in range(h)] + [[]]
        horizontal = [["bb"] * w + ['b'] for _ in range(h + 1)]
        def walk(x, y):
            vis[y][x] = 1
            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(d)
            for (xx, yy) in d:
                if xx == -1 and yy == 0:
                    vertical[y][max(x, xx)] = "mo"
                if xx == 7 and yy == 6:
                    vertical[y][max(x, xx)] = "g"
                if vis[yy][xx]:
                    continue
                if xx == x:
                    horizontal[max(y, yy)][x] = "bo"
                if yy == y:
                    vertical[y][max(x, xx)] = "oo"
                walk(xx, yy)
        walk(randrange(w), randrange(h))
        #s = ""
        s = []
        for (a, b) in zip(horizontal, vertical):
            #s += ''.join(a + ['\n'] + b + ['\n'])
            s += ''.join(a + b)

        return s
		
    #def creation(window, ARRAY, BRICK, PERSO, GUARD):
    def creation(ARRAY):
        """fonction de préparation des éléments du jeu"""
        lab = Labyrinthe.make_maze()
        content = []
        compteur_ligne = 0
        var_ligne = ""
        for elt in lab:
            compteur_ligne += 1
            var_ligne = var_ligne + elt
            if compteur_ligne == 15:
                content.append(var_ligne)
                compteur_ligne = 0
                var_ligne = ""

        numero_ligne = 0
        for element in content:
            numero_case = 0
            for sprite in element:
                x = numero_case * TAILLE_SPRITE
                y = numero_ligne * TAILLE_SPRITE
                if sprite == "b":
                    #window.blit(BRICK, (x, y))
                    ARRAY.append([x, y, "BRICK"])
                elif sprite == "m":
                    #window.blit(PERSO, (x, y))
                    ARRAY.append([x, y, "PERSO"])
                elif sprite == "g":
                    #window.blit(GUARD, (x, y))
                    ARRAY.append([x, y, "GUARD"])
                else:
                    # le cas du caractère o dans le fichier
                    ARRAY.append([x, y])
                numero_case += 1
            numero_ligne += 1

    def affichage(window, ARRAY, BRICK, PERSO, GUARD, SYRINGE_IMAGE, TUBE_IMAGE, ETHER_IMAGE, BACKGROUND):
        """"Génération du niveau graphique à partir de la lecture de ARRAY"""
    #Si la fonction trouve un élément dans la case, elle l'affiche aux coordonnées de la case (ses deux premiers éléments)
        window.blit(BACKGROUND, (0, 0))
        for elt in ARRAY:
            if "BRICK" in elt:
                window.blit(BRICK, (elt[0], elt[1]))
            elif "PERSO" in elt:
                window.blit(PERSO, (elt[0], elt[1]))
            elif "GUARD" in elt:
                window.blit(GUARD, (elt[0], elt[1]))
            elif "syringe" in elt:
                window.blit(SYRINGE_IMAGE, (elt[0], elt[1]))
            elif "tube" in elt:
                window.blit(TUBE_IMAGE, (elt[0], elt[1]))
            elif "ether" in elt:
                window.blit(ETHER_IMAGE, (elt[0], elt[1]))
            else:
                pass
        #rafraîchissmement de l'écran de façon à MAJ les images
        pygame.display.flip()

if __name__ == "__main__":
    pass