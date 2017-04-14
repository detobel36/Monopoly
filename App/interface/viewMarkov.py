#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Tkinter and External
import tkinter as tk

from interface.caseCercle import CaseCercle

import math


"""
    LabelFrame contenant un canvas et permettant de dessiner la chaine de Markov
"""
class viewMarkov(tk.LabelFrame):

    CIRCLE_SIZE = 10
    ESPACE = 50
    CASE_PAR_LIGNE = 10
    ARC_DECALAGE = -40


    """
        Permet d'initialiser la fenêtre

        @param fenetre la fenêtre parente à celle-ci
        @param listCase liste des cases à afficher
        @param matriceDeplacement matrice contenant tous les déplacements des états possibles
    """
    def __init__(self, fenetre, listCase, matriceDeplacement):
        tk.LabelFrame.__init__(self, fenetre, text="Chaine de Markov", padx=0, pady=0, labelanchor="n")

        self._listeCercleCase = {} # Liste stockant l'id du cercle en fonction de l'id de la case
        self._listeLigneDepl = {}  # Liste stockant l'id de la ligne en fonction de l'id de la case de départ

        self._listeCase = listCase
        self._matriceDeplacement = matriceDeplacement
        self.__drawMarkov()


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
        self.__drawAllNodes()
        self.__drawAllDeplacement()


    """
        Permet d'initialiser les variables définissant les bordures et les échelles
    """
    def __initLimitAndBorder(self):
        self._width = 950
        self._height = 500
        self._borderX = 50
        self._borderY = 50


    """
        Permet de dessiner les cases du Monopoly, représenté par des noeud
    """
    def __drawAllNodes(self):
        index = 0
        for case in self._listeCase:
            if(case.getNbrDeDouble() == 0):
                (x, y) = self.__generatePlateauCoord(index)
                self.__drawCase(case, x, y)
            index += 1


    """
        Permet de dessiner les déplacements possibles
    """
    def __drawAllDeplacement(self):
        index = 0
        for case in self._listeCase:
            if(case.getNbrDeDouble() == 0):
                colonne = 0

                for elem in self._matriceDeplacement[index]:
                    idCaseDestination = self._listeCase[colonne].getPosition()
                    if(elem > 0 and idCaseDestination in self._listeCercleCase):
                        self.__drawDeplacement(case.getPosition(), idCaseDestination)

                    colonne += 1
            index += 1


    """
        Permet d'afficher une case sur le canvas

        @param case qu'il faut représenter
        @param x coordonnée x
        @param y coordonnée y
    """
    def __drawCase(self, case, x, y):
        coordLeftX = x - viewMarkov.CIRCLE_SIZE + self._borderX
        coordTopY = y - viewMarkov.CIRCLE_SIZE + self._borderY
        coordRightX = x + viewMarkov.CIRCLE_SIZE + self._borderX
        coordBottomY = y + viewMarkov.CIRCLE_SIZE + self._borderY

        idCase = case.getPosition()
        caseCercle = CaseCercle(self._canvas, case, coordLeftX, coordRightX, coordTopY, coordBottomY)
        self._listeCercleCase[idCase] = caseCercle


    """
        Permet de retrouver les coordonnées central à partir des informations concernant les 
        coordonnées que nous donnent tkinter

        @param allCoordinate toutes les informations concernant les coordonnées de tkinter (
            coordonnées du point en haut à gauche et en bas à droite)
        @return un tuple contenant les coordonnées x, y
    """
    def __getCenterOfOval(self, allCoordinate):
        x0 = allCoordinate[0]
        y0 = allCoordinate[1]

        x1 = allCoordinate[2]
        y1 = allCoordinate[3]

        diffX = max(x0, x1) - min(x0, x1)
        diffY = max(y0, y1) - min(y0, y1)

        return min(x0, x1) + diffX/2, min(y0, y1) + diffY/2


    """
        Permet de dessiner une ligne entre deux cases (représentant donc un déplacement possible sur
            le plateau de Monopoly)

        @param idCase1 id de la case une
        @param idCase2 id de la seconde case
    """
    def __drawDeplacement(self, idCase1, idCase2):
        idCercleSource = self._listeCercleCase[idCase1]
        idCercleDest = self._listeCercleCase[idCase2]

        variableSource = idCercleSource.getCoords()
        variableDest = idCercleDest.getCoords()

        coordsSource = self.__getCenterOfOval(variableSource)
        coordsDest = self.__getCenterOfOval(variableDest)

        idArc = self.__createArc(coordsSource, coordsDest)
        if(idCase1 in self._listeLigneDepl):
            self._listeLigneDepl[idCase1].append(idArc)
        else:
            self._listeLigneDepl[idCase1] = [idArc]


    """
        Permet de tracer un arc de cercle entre deux points

        @param p0 point 0 
        @param p1 point 1

        @return l'id de l'arc créé
    """
    def __createArc(self, p0, p1):
        minX = min(p0[0], p1[0])
        minY = min(p0[1], p1[1])

        milieuX = minX
        milieuY = minY
        
        diffX = max(p0[0], p1[0]) - minX
        diffY = max(p0[1], p1[1]) - minY

        if(diffY == 0):
            milieuX += diffX/2
            milieuY += viewMarkov.ARC_DECALAGE

        elif(diffX == 0):
            milieuX += viewMarkov.ARC_DECALAGE
            milieuY += diffY/2

        else:
            milieuX += diffX/2 + viewMarkov.ARC_DECALAGE
            milieuY += diffY/2 + viewMarkov.ARC_DECALAGE

        milieu = (milieuX, milieuY)

        idLine = self._canvas.create_line(p0, milieu, p1, smooth=True)
        self._canvas.tag_lower(idLine)

        return idLine


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

