# -*- coding: utf-8 -*-
from Constantes import *

# Cache permettant d'éviter de faire les mêmes calcul tout le temps
cacheRepratitionDes = {}


"""
    Permet de réprésenter une case du monopoly
"""
class Case:

    """
        Permet d'initiliser une case

        @param nom de la case
        @param position sur le plateau de jeu (-1 pour indiqué que ce n'est pas une case accessible)
        @param couleur de la case (par défaut "black")
        @param prix pour acheter la case (-1 pour une case qui ne peut pas être achetée)
    """
    def __init__(self, nom, position, couleur = "black", prix = 0):
        self._nom = nom
        self._position = position
        self._couleur = couleur
        self._prix = prix


    """
        Permet de récupérer le nom de la case

        @return le nom de la case
    """
    def getNom(self):
        return self._nom


    """
        Permet de récupérer la couleur de la case

        @return la couleur de la case
    """
    def getCouleur(self):
        return self._couleur


    """
        Permet de récupérer le prix de la case

        @return le prix de la case
    """
    def getPrix(self):
        return self._prix


    """
        Permet d'avoir la position de la case sur le plateau de jeu

        @return le numero représentant l'emplacement de la case sur le plateau de jeu
    """
    def getPosition(self):
        return self._position


    """
        Permet de récupérer les cases accèssibles depuis la case actuelle

        @param dataMonopoly les informations liées au plateau monopoly (permettant de récupérer 
            les autres cases)
        @return liste des objets Case étant accèssibles
    """
    def getCasesSuivantes(self, dataMonopoly):
        return self.getCasesSuivanteDes(dataMonopoly, 1)


    """
        Permet de récupérer les cases accèssibles depuis la case actuelle seulement en lancant les
        dés

        @param dataMonopoly les informations liées au plateau monopoly (permattant de récupérer les 
            autres cases)
        @param proportionAjouter proportion à ajouter pour lancer les dés
        @return un dictionnaire avec en clef la Case accèssible et avec comme valeur la probabilité 
        de rejoindre cette case
    """
    def getCasesSuivanteDes(self, dataMonopoly, proportionAjouter = 1):
        res = {}
        resRepartition = getRepartitionDes(self._parent.getNbrDeDes())
        for elem in resRepartition:
            probabilite = resRepartition[elem]
            nouvelleCase = dataMonopoly.getCase(self._position+elem)

            res[nouvelleCase] = probabilite*proportionAjouter

        return res

    """
        Permet de définir le "DataMonopoly" pour lequel cette case a été créé

        @param parent le DataMonopoly auquel appartient cette case
    """
    def setParentDataMonopoly(self, parent):
        self._parent = parent




############################ Initialisation ############################

# Initialise les cases par défaut
def getCaseDepart():
    return Case("Départ", 0, "white", -1)


############################ Utils AND Cache ############################

"""
    Permet de récupérer la probabilité de faire un certain score avec un dé en fonction du nombre
    de dé

    @param nbrDes nombre de dé avec lequel on veut la répartition
    @return un dictionnaire avec les nombres accèssible et leur probabilité
"""
def getRepartitionDes(nbrDes):
    res = {}

    # Si c'est déjà dans le cache
    if(nbrDes in cacheRepratitionDes):
        res = cacheRepratitionDes[nbrDes]

    else:
        # "s" est les nombre que l'on peut atteindre
        for s in range(nbrDes, (nbrDes*6)+1):
            total = 0
            for k in range(0, int((s-nbrDes)/6)+1):
                sousTotal = -1 if(k % 2 == 1) else 1
                # (n \n k) (x-6k-1 \n n-1)
                sousTotal *= combinatoire(nbrDes, k) * combinatoire(s-6*k-1, nbrDes-1)
                total += sousTotal

            res[s] = total/pow(6, nbrDes)

        cacheRepratitionDes[nbrDes] = res

    return res



def combinatoire(n, p):
    numerateur = n
    maxDivision = max(n-p, p)
    minDiv = min(n-p, p)

    res = 1

    multiplicationAFaire = numerateur - maxDivision

    for k in range(multiplicationAFaire):
        res *= (numerateur / minDiv)
        numerateur -= 1
        minDiv -= 1

    return res


