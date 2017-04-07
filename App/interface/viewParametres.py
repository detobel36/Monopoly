#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Tkinter and External
import tkinter as tk
from tkinter import messagebox
# Utils
from Constantes import *


"""
    LabelFrame permettant d'afficher les paramètres sélectionné précédemment
"""
class ViewParametres(tk.LabelFrame):


    """
        Création de la fenêtre

        @param fenetre parent
    """
    def __init__(self, fenetre, selectMonopolyData):
        tk.LabelFrame.__init__(self, fenetre, text="Paramètres choisis", padx=3, pady=3, labelanchor="n", \
                relief=tk.RAISED)

        self._parent = fenetre
        self._monopolyData = selectMonopolyData

        self.__addLabelNbrDeDes()
        self.__addLabelNbrMaxPrisonTour()
        self.__addLabelProbSotirPrison()


    """
        Permet d'ajouter un label affichant le nombre de dés qui a été choisi
    """
    def __addLabelNbrDeDes(self):
        nbrDeDes = self._monopolyData.getNbrDeDes()
        tk.Label(self, text="Nombre de dés: " + str(nbrDeDes), anchor="n", wraplength=130, \
            justify=tk.LEFT).pack(pady=5)

    """
        Permet d'ajouter un label affichant le nombre de tour que l'on peut passer en prison
    """
    def __addLabelNbrMaxPrisonTour(self):
        nbrMaxPrison = self._monopolyData.getMaxTourPrison()
        tk.Label(self, text="Nombre de tour maximum en prison: " + str(nbrMaxPrison), anchor="n", \
            wraplength=130, justify=tk.LEFT).pack(pady=5)


    """
        Permet d'ajouter un label permettant d'afficher la probabiliter que le joueur décide
        de payer pour sotir de prison
    """
    def __addLabelProbSotirPrison(self):
        probSotirPrison = self._monopolyData.getProbSortirPrison()
        tk.Label(self, text="Probabilité de payer pour sortir de prison: " + str(probSotirPrison), \
            anchor="n", wraplength=130, justify=tk.LEFT).pack(pady=5)
