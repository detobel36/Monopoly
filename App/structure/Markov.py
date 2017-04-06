# -*- coding: utf-8 -*-

import numpy as np

"""
    Permet de représenter une chaine de markov.
    Cet objet contient donc plusieurs matrices
"""
class Markov:

    """
        Constructeur

        @param matInit matrice contenant les points de départs
        @param matDeplacement matrice contenant tous les changements d'états possible
    """
    def __init__(self, matInit, matDeplacement):
        self._matInit = matInit
        self._matDeplacement = matDeplacement

        # Cache stockant les résultats des exposants de la matrice de déplacement
        self._cacheExpoMatDepl = {0: np.eye(len(self._matDeplacement)), 1: self._matDeplacement} 


    """
        Ajout d'un déplacement/un changement d'état
    """
    def ajouterUnDeplacement(self):
        return ajouterDeplacement(1)


    """
        Ajout d'un déplacement, en d'autres mot: situation après un changement d'état

        @param nbrDeplacement nombre de déplacement/changement d'état à faire
    """
    def ajouterDeplacement(self, nbrDeplacement):
        self._matDeplacement = np.linalg.matrix_power(self._matDeplacement, nbrDeplacement+1)


    """
        Permet de récupérer la matrice de déplacement de la chaine de markov

        @return la matrice représentant les déplacements possibles
    """
    def getMatriceDeplacement(self):
        return self._matDeplacement
        

    """
        Permet de trouver les points fix à partir d'un point de départ précis
    """
    def trouverPointFix(self):
        # Le but final du calcul est de faire:
        # (P-I)^T w = (0, ..., 0, 1)
        # Où p est la matrice de déplacement et w la matrice que l'on cherche

        nbrLigne = len(self._matDeplacement)
        nbrColonne = len(self._matDeplacement[0])

        # Matrice avec laquelle on va travailler (histoire de ne pas modifier par erreur)
        # la matrice de déplacement
        matriceTravail = self._matDeplacement

        if(nbrLigne != nbrColonne):
            print("[WARNING] Le nombre de ligne n'est pas le même que le nombre de colonne " \
                    "(" + nbrLigne + ", " + nbrColonne + ")")

        matriceUnite = np.eye(nbrLigne)
        matriceTravail = matriceTravail - matriceUnite

        # On rajoute une colonne de un à la matrice de déplacement
        colonneDeUn = np.ones((nbrLigne, 1))
        matriceTravail = np.append(matriceTravail, colonneDeUn, axis=1)

        # On créé la matrice indiquant les résultats qui seront utilisé pour réalisé le calcul
        # C'est à dire une matrice colonne remplis de 0 sauf le dernier élément qui est un 1
        matriceResultat = np.zeros((nbrColonne+1, 1))
        matriceResultat[nbrColonne][0] = 1

        invMatriceTravail = matriceTravail.transpose()

        solution = np.linalg.lstsq(invMatriceTravail, matriceResultat)

        return solution[0]

    # TODO changer avec le bon nom xD
    def multiplicationInitiatialeDeplacement(self):
        return np.dot(self._matInit, self._matDeplacement)
        # return self._matInit.multiplication(self._matDeplacement)
