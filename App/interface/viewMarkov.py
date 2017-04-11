#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Tkinter and External
import tkinter as tk

"""
    LabelFrame contenant un canvas et permettant de dessiner la chaine de Markov
"""
class viewMarkov(tk.LabelFrame):

    CIRCLE_SIZE = 10

    """
        Permet d'initialiser la fenêtre

        @param fenetre la fenêtre parente à celle-ci
        @param data les données à afficher
    """
    def __init__(self, fenetre, data):
        tk.LabelFrame.__init__(self, fenetre, text="Chaine de Markov", padx=0, pady=0, labelanchor="n")

        self._data = data
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

        i = 0
        for case in self._data:
            if(i == 0):
                self.__drawCase(case, 0, 0)
            i += 1

        # print(self._data)
        # case = self._data[3]
        # print(case)
        


    """
        Permet d'initialiser les variables définissant les bordures et les échelles
    """
    def __initLimitAndBorder(self):
        self._width = 1000
        self._height = 800
        self._borderX = 25
        self._borderY = 25


    """
        Permet d'afficher une case sur le canvas
    """
    def __drawCase(self, case, x, y):
        coordTopLeftX = x - viewMarkov.CIRCLE_SIZE + self._borderX
        coordTopLeftY = y - viewMarkov.CIRCLE_SIZE + self._borderY
        coordBottomRightX = x + viewMarkov.CIRCLE_SIZE + self._borderX
        coordBottomRightY = y + viewMarkov.CIRCLE_SIZE + self._borderY

        self._canvas.create_oval(coordTopLeftX, coordTopLeftY, coordBottomRightX, coordBottomRightY,\
            outline="gray", fill=case.getCouleur())


    """
        Fonction génératrice de coordonnée x et y permettant d'afficher les cases en forme
        de plateau rectangulaire

        @return un tuple x, y
    """
    def __generatePlateauCoord(self):
        pass

