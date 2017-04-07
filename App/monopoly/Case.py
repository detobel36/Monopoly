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
        self._nbrDeDouble = 0


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
        Permet de savoir combien de double il faut pour attendre cette case

        @return le nombre de double qu'il faut
    """
    def getNbrDeDouble(self):
        return self._nbrDeDouble


    """
        Permet d'indiquer que cette case est seulement accèssible si le joueur à faire un nombre 
        précis de "double" consécutif

        @param nombreDeDouble qu'a fait le joueur pour se retrouver sur cette case
    """
    def setNbrDeDouble(self, nombreDeDouble):
        self._nbrDeDouble = nombreDeDouble


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
        @param proportionAjouter proportion à ajouter pour lancer les dés (facultatif, par défaut 1)
        @return un dictionnaire avec en clef la Case accèssible et avec comme valeur la probabilité 
        de rejoindre cette case
    """
    def getCasesSuivanteDes(self, dataMonopoly, proportionAjouter = 1):
        res = {}
        # On récupère la répartition des dés
        resRepartition = getRepartitionDes(dataMonopoly.getNbrDeDes())
        for elem in resRepartition: # Pour chaque case accèssibles
            probabilite = resRepartition[elem] # On récupère la probabilité

            # Récupéréation de la case correspondante
            nouvelleCase = self.__getReelCaseFromRelativeIndex(dataMonopoly, elem)

            if(nouvelleCase in res):
                res[nouvelleCase] += probabilite*proportionAjouter
            else:
                res[nouvelleCase] = probabilite*proportionAjouter

        return res


    """
        Permet de récupére la case réelle en fonction de l'index relatif à la case actuelle.  Les
        index négatif indique qu'il s'agit d'un double

        @param indexRelatif l'index relatif à la case actuelle
        @return la case correspondante à l'index
    """
    def __getReelCaseFromRelativeIndex(self, dataMonopoly, indexRelatif):
        # Si la case accèsible est négative, c'est que c'est un double
        if(indexRelatif < 0):
            indexRelatif = -indexRelatif # On ré inverse le signe

            # Si les triples doubles sont désactivé
            if(dataMonopoly.getNbrDeDouble() <= 0):
                nouvelleCase = dataMonopoly.getCase(self._position+indexRelatif)

            # Si on a fait trop de double
            elif(self._nbrDeDouble+1 >= dataMonopoly.getNbrDeDouble()):
                nouvelleCase = dataMonopoly.getCasePrison()

            # Sinon, on change juste
            else:
                nouvelleCase = dataMonopoly.getCase(self._position+indexRelatif, self._nbrDeDouble+1)

        else:
            nouvelleCase = dataMonopoly.getCase(self._position+indexRelatif)

        return nouvelleCase



############################ Initialisation ############################

# Initialise les cases par défaut
def getCaseDepart():
    return Case("Départ", 0, "white", -1)


############################ Utils AND Cache ############################

"""
    Permet de récupérer la probabilité de faire un certain score avec un dé en fonction du nombre
    de dé

    @param nbrDes nombre de dé avec lequel on veut la répartition
    @return un dictionnaire avec les nombres accèssible et leur probabilité. Les nombres négatif
        sont des doubles qui doivent être géré différemment
"""
def getRepartitionDes(nbrDes):
    res = {}

    # Si c'est déjà dans le cache
    if(nbrDes in cacheRepratitionDes):
        res = cacheRepratitionDes[nbrDes]

    else:
        nbrChoixPossible = pow(6, nbrDes)

        # "s" est les nombre que l'on peut atteindre
        for s in range(nbrDes, (nbrDes*6)+1):
            total = 0
            for k in range(0, int((s-nbrDes)/6)+1):
                sousTotal = -1 if(k % 2 == 1) else 1
                # (n \n k) (x-6k-1 \n n-1)
                sousTotal *= combinatoire(nbrDes, k) * combinatoire(s-6*k-1, nbrDes-1)
                total += sousTotal

            if(s % nbrDes == 0):
                total -= 1
                res[-s] = 1/nbrChoixPossible

            if(total > 0):
                res[s] = total/nbrChoixPossible

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


