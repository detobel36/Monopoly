#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
import monopoly.DataMonopoly as dataMonopoly


class ChoixMonopoly:

    """
        Construction
    """
    def __init__(self):
        self._listMonopolyDisponible = dataMonopoly.getAllDataMonopoly()

        if(len(self._listMonopolyDisponible) > 1):
            self.ouvrirFenetreChoix()

        else:
            self._selectedMonopoly = self._listMonopolyDisponible[0]
            

    """
        Initialisation de la fenêtre permettant de choisir le monopoly
    """
    def ouvrirFenetreChoix(self):
        self._fenetre = tk.Tk() # Création de la fenêtre
        self._fenetre.wm_title("Choix du Monopoly")

        # Création de la liste des choix
        self._liste = tk.Listbox(self._fenetre)
        index = 0 # Numero des choix
        for monopoly in self._listMonopolyDisponible:
            self._liste.insert(index, monopoly.getDisplayNom())
            index += 1
        # Ajout de la liste sur la fenêtre
        self._liste.pack()

        # Ajout d'un bouton à cette fenêtre
        tk.Button(self._fenetre, text='Sélectionner', command=self.__selectMonopoly).pack()

        # Attente de la fin de l'event
        self._fenetre.mainloop()
        

    """
        Fonction appellé lorsque l'on confirme le monopoly choisi
    """
    def __selectMonopoly(self):
        if(len(self._liste.curselection()) > 0):
            indexSelect = self._liste.curselection()[0]

            self._selectedMonopoly = self._listMonopolyDisponible[indexSelect]
            # Femeture de la fenêtre
            self._fenetre.quit()
            self._fenetre.destroy()


    """
        Récupération de la fenêtre selectionnée

        @return le monopoly sélectionné
    """
    def getResult(self):
        return self._selectedMonopoly

