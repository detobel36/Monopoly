#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Tkinter and External
import tkinter as tk

"""
    LabelFrame contenant un canvas et permettant de dessiner la chaine de Markov
"""
class viewMarkov(tk.LabelFrame):

    CIRCLE_SIZE = 10
    ESPACE = 50
    CASE_PAR_LIGNE = 10

    """
        Permet d'initialiser la fenêtre

        @param fenetre la fenêtre parente à celle-ci
        @param listCase liste des cases à afficher
        @param matriceDeplacement matrice contenant tous les déplacements des états possibles
    """
    def __init__(self, fenetre, listCase, matriceDeplacement):
        tk.LabelFrame.__init__(self, fenetre, text="Chaine de Markov", padx=0, pady=0, labelanchor="n")

        self._listeCercleCase = {} # Liste stockant l'id du cercle en fonction de l'id de la case

        self._listeCase = listCase
        self._matriceDeplacement = matriceDeplacement
        self.__drawMarkov()

        print(self._listeCercleCase)


    """
        Permet de dessiner la chaine de Markov en tant que tel
    """
    def __drawMarkov(self):
        self.__initLimitAndBorder()

        # Création du canvas
        self._canvas = tk.Canvas(self, 
            width=self._width+(2*self._borderX), 
            height=self._height+(2*self._borderY), 
            background='white')

        self._canvas.pack()

        index = 0
        for case in self._listeCase:
            if(case.getNbrDeDouble() == 0):
                (x, y) = self.__generatePlateauCoord(index)
                self.__drawCase(case, x, y)
            index += 1

        index = 0
        for case in self._listeCase:
            if(case.getNbrDeDouble() == 0):
                colonne = 0
                for elem in self._matriceDeplacement[index]:
                    caseDestination = self._listeCase[colonne].getPosition()
                    if(elem > 0 and caseDestination in self._listeCercleCase):
                        idCercleSource = self._listeCercleCase[case.getPosition()]
                        idCercleDest = self._listeCercleCase[caseDestination]

                        variableSource = self._canvas.coords(idCercleSource)
                        variableDest = self._canvas.coords(idCercleDest)
                        print(case.getNom() + " -> " + self._listeCase[colonne].getNom())
                        print(str(self.__getCenterOfOval(variableSource)) + " -> " + str(self.__getCenterOfOval(variableDest)))
                        print(str(variableSource) + " -> " + str(variableDest))

                    colonne += 1


            index += 1
        

    """
        Permet d'initialiser les variables définissant les bordures et les échelles
    """
    def __initLimitAndBorder(self):
        self._width = 950
        self._height = 500
        self._borderX = 50
        self._borderY = 50


    """
        Permet d'afficher une case sur le canvas

        @param case qu'il faut représenter
        @param x coordonnée x
        @param y coordonnée y
    """
    def __drawCase(self, case, x, y):
        coordTopLeftX = x - viewMarkov.CIRCLE_SIZE + self._borderX
        coordTopLeftY = y - viewMarkov.CIRCLE_SIZE + self._borderY
        coordBottomRightX = x + viewMarkov.CIRCLE_SIZE + self._borderX
        coordBottomRightY = y + viewMarkov.CIRCLE_SIZE + self._borderY

        idCase = case.getPosition()
        self._listeCercleCase[idCase] = self._canvas.create_oval(coordTopLeftX, coordTopLeftY, \
            coordBottomRightX, coordBottomRightY,outline="gray", fill=case.getCouleur(), \
            activeoutline="red", activewidth=2)


    """
        Permet de retrouver les coordonnées central à partir des informations concernant les 
        coordonnées que nous donnent tkinter

        @param allCoordinate toutes les informations concernant les coordonnées de tkinter (
            coordonnées du point en haut à gauche et en bas à droite)
        @return un tuple contenant les coordonnées x, y
    """
    def __getCenterOfOval(self, allCoordinate):
        topLeftX = allCoordinate[0]
        topLeftY = allCoordinate[1]

        bottomRightX = allCoordinate[2]
        bottomRightY = allCoordinate[3]

        diffX = bottomRightX - topLeftX
        diffY = bottomRightY - topLeftY

        return bottomRightX + diffX/2, bottomRightY + diffY/2


    """
        Permet de dessiner une ligne entre deux cases

        @param case1 la case une
        @param case2 la seconde case
    """
    def __drawLine(self, case1, case2):
        pass



    """
        Permet de récupérer la position de la ième case

        @param index de la case à placer
        @return un tuple x, y
    """
    def __generatePlateauCoord(self, index):
        x = 0
        y = 0

        if(index < viewMarkov.CASE_PAR_LIGNE):
            x = index * viewMarkov.ESPACE
            y = 0

        elif(index < viewMarkov.CASE_PAR_LIGNE * 2):
            x = viewMarkov.CASE_PAR_LIGNE * viewMarkov.ESPACE
            y = (index-viewMarkov.CASE_PAR_LIGNE) * viewMarkov.ESPACE

        elif(index < viewMarkov.CASE_PAR_LIGNE * 3):
            maxX = viewMarkov.CASE_PAR_LIGNE * viewMarkov.ESPACE
            x = maxX - ((index - (2 * viewMarkov.CASE_PAR_LIGNE)) * viewMarkov.ESPACE)
            y = viewMarkov.CASE_PAR_LIGNE * viewMarkov.ESPACE

        elif(index < viewMarkov.CASE_PAR_LIGNE * 4):
            x = 0
            maxY = viewMarkov.CASE_PAR_LIGNE * viewMarkov.ESPACE
            y = maxY - ((index - (3 * viewMarkov.CASE_PAR_LIGNE)) * viewMarkov.ESPACE)

        else:
            newIndex = (index - viewMarkov.CASE_PAR_LIGNE * 4)
            x = (viewMarkov.CASE_PAR_LIGNE + 2) * viewMarkov.ESPACE
            y = newIndex * viewMarkov.ESPACE

        return x, y

