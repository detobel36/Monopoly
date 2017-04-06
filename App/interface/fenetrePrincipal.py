#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Tkinter and External
import tkinter as tk
from copy import deepcopy
# Utils
from Constantes import *
from Monopoly import Monopoly
# Interface
from interface.choixMonopoly import ChoixMonopoly
from interface.parametres import Parametres
from interface.statistiques import Statistiques
from interface.configTour import ConfigTour



"""
    FenetrePrincipal qui hérite de tkinter.Tk et contenant toutes les autres fenêtres à afficher
"""
class FenetrePrincipal(tk.Tk):


    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_title("Stats")
        self.config(padx=5, pady=5)

        # Choix des paramètres
        self.__choixParametres()

        # Choix du monopoly
        self._selectedDataMonopoly = self.__choixDuMonopoly()
        self._selectedMonopoly = Monopoly(self._selectedDataMonopoly)

        # Création de la fenêtre de gestion de tour
        self._nbrTourFrame = ConfigTour(self)
        self._nbrTourFrame.grid(row=0, column=1, sticky="n", padx=7)

        # Création de la fenêtre de statistique
        self._statFrame = Statistiques(self._selectedMonopoly.getResultatSimulation(), self)
        self._statFrame.grid(row=0, column=0)


        self.mainloop()


    """
        Permet de choisir le Monopoly à utiliser

        @return l'objet DataMonopoly contenant toutes les informations du Monopoly choisi
    """
    def __choixDuMonopoly(self):
        choixMonopoly = ChoixMonopoly()
        selectedDataMonopoly = choixMonopoly.getResult();

        if(DEBUG):
            print("[DEBUG] Monopoly sélectionné: " + selectedDataMonopoly.getNom())

        return selectedDataMonopoly

    """
        Permet de choisir les paramètres qui seront utilisé pour modéliser le Monopoly
    """
    def __choixParametres(self):
        choixParametres = Parametres()
        self.wait_window(choixParametres)


    """
        Permet de mettre à jour le graphique en fonction du nombre de tour choisi

        @param pointFixe permet de savoir si on veut mettre à jour le graphique en fonction des 
            probabilité après une "infinité" de tour (c'est à dire lorsqu'il n'y a plus de variation
            des états)
    """
    def updateNewTour(self, pointFixe = False):
        nbrTour = self._nbrTourFrame.getNbrTourASimuler()

        newDataMonopoly = deepcopy(self._selectedDataMonopoly)
        # TODO clarifier tout ça

        newMonopoly = Monopoly(newDataMonopoly)

        if(pointFixe):
            newData = newMonopoly.simulerInfini()
        else:
            newMonopoly.simulerDesTours(nbrTour)
            newData = newMonopoly.getResultatSimulation()

        self._statFrame.updateCanvas(newData)




