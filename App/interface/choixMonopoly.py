#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
import monopoly.DataMonopoly as dataMonopoly


class ChoixMonopoly(tk.Toplevel):

    """
        Construction
    """
    def __init__(self):

        self.__loadAllMonopoly()
        if(len(self._listMonopolyDisponible) > 1):
            self._selectedMonopoly = None
            tk.Toplevel.__init__(self)
            self.ouvrirFenetreChoix()
        else:
            self._selectedMonopoly = self._listMonopolyDisponible[0]


    """
        Permet de récupérer la liste de tous les Monopoly
    """
    def __loadAllMonopoly(self):
        self._listMonopolyDisponible = dataMonopoly.getAllDataMonopoly()


    """
        Initialisation de la fenêtre permettant de choisir le monopoly
    """
    def ouvrirFenetreChoix(self):
        self.title("Choix du Monopoly")
        self.__addListBox()
        self.__addSelectButton()


    """
        Permet d'ajouter la liste des Monopoly disponibles
    """
    def __addListBox(self):
        # Création de la liste des choix
        self._liste = tk.Listbox(self, width=30)
        index = 0 # Numero des choix
        for monopoly in self._listMonopolyDisponible:
            self._liste.insert(index, monopoly.getDisplayNom())
            index += 1

        # Ajout de la liste sur la fenêtre
        self._liste.pack(fill=tk.BOTH, expand=1)


    """
        Ajout d'un button permettant de valider son choix
    """
    def __addSelectButton(self):
        tk.Button(self, text='Sélectionner', command=self.__selectMonopoly, height=2)\
            .pack(fill=tk.BOTH, expand=1)
        

    """
        Fonction appellé lorsque l'on confirme le monopoly choisi
    """
    def __selectMonopoly(self):
        if(len(self._liste.curselection()) > 0):
            indexSelect = self._liste.curselection()[0]

            self._selectedMonopoly = self._listMonopolyDisponible[indexSelect]
            print("Monopoly choisi: " + str(self._selectedMonopoly))
            self.__closeChoixMonopoly()


    """
        Permet de fermer la fenêtre de choix du Monopoly
    """
    def __closeChoixMonopoly(self):
        self.quit()
        self.destroy()


    """
        Récupération de la fenêtre selectionnée

        @return le monopoly sélectionné
    """
    def getSelectedMonopoly(self):
        return self._selectedMonopoly

