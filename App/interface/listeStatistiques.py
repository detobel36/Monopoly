#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk

from operator import itemgetter
# from math import round

from interface.scrollTopFrame import scrollTopFrame


"""
    Permet de montrer les statistiques sous forme de liste ordonné en fonction des probabilités
"""
class ListeStatistiques(scrollTopFrame):

    COLOR_WIDTH = 50
    COLOR_HEIGHT = COLOR_WIDTH


    def __init__(self, listeCases):
        scrollTopFrame.__init__(self)
        # tk.Toplevel.__init__(self)
        self.title("Liste statistiques")
        
        self._listeCases = listeCases

        self.__initAllWidgets()
        self.__initEvent()
        self.__refreshScroll()


    def __initAllWidgets(self):
        self.__addTitle()
        self.__addAllCases()


    """
        Permet d'initialiser les events
    """
    def __initEvent(self):
        self.bind("<Escape>", self.__closeStats)


    def __addTitle(self):
        style = "Arial 12 bold"
        tk.Label(self.getMainFrame(), text="Couleur", font=style).grid(column=0, row=0)
        tk.Label(self.getMainFrame(), text="Case", font=style).grid(column=1, row=0)
        tk.Label(self.getMainFrame(), text="Proportion", font=style).grid(column=2, row=0)

    def __addAllCases(self):
        i = 1
        for case in sorted(self._listeCases, key=self._listeCases.get, reverse=True):
            canvas = tk.Canvas(self.getMainFrame(), width=ListeStatistiques.COLOR_WIDTH, height=ListeStatistiques.COLOR_HEIGHT, 
                background=case.getCouleur())
            canvas.grid(column=0, row=i)

            tk.Label(self.getMainFrame(), text=case.getNom()).grid(column=1, row=i, sticky=tk.W)
            tk.Label(self.getMainFrame(), text=round(self._listeCases[case], 4)).grid(column=2, row=i)

            i += 1


    """
        Fonction appellé lorsque l'on veut fermer la fenêtre
    """
    def __closeStats(self, event = None):
        self.quit()
        self.destroy()

    def __refreshScroll(self):
        self.after(100, lambda: scrollTopFrame.updateScroll(self))
