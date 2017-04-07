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
from interface.viewParametres import ViewParametres



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
        self.__applyParamOnDataMonopoly()
        self._selectedMonopoly = Monopoly(self._selectedDataMonopoly)

        # Affichage des paramètres choisi
        self._viewParam = ViewParametres(self, self._selectedDataMonopoly)
        self._viewParam.grid(row=1, column=1, padx=7, sticky=tk.N+tk.S+tk.E+tk.W)

        # Création de la fenêtre de gestion de tour
        self._nbrTourFrame = ConfigTour(self)
        self._nbrTourFrame.grid(row=0, column=1, padx=7, sticky=tk.N+tk.E+tk.W)

        # Création de la fenêtre de statistique
        self._statFrame = Statistiques(self._selectedMonopoly.getResultatSimulation(), self)
        self._statFrame.grid(row=0, column=0, rowspan=2)

        # self.wait_window(self) TODO
        self.mainloop()


    """
        Permet de choisir le Monopoly à utiliser

        @return l'objet DataMonopoly contenant toutes les informations du Monopoly choisi
    """
    def __choixDuMonopoly(self):
        choixMonopoly = ChoixMonopoly()
        selectedDataMonopoly = choixMonopoly.getSelectedMonopoly();

        if(selectedDataMonopoly == None):
            self.wait_window(choixMonopoly)

        if(DEBUG):
            print("[DEBUG] Monopoly sélectionné: " + selectedDataMonopoly.getNom())

        return selectedDataMonopoly


    """
        Permet de choisir les paramètres qui seront utilisé pour modéliser le Monopoly
    """
    def __choixParametres(self):
        self._choixParametres = Parametres()
        self.wait_window(self._choixParametres)


    """
        Permet d'appliqué les choix fait lors du paramétrage sur le Monopoly
    """
    def __applyParamOnDataMonopoly(self):
        nbrDes = self._choixParametres.getNbrDeDes()
        nbrMaxTourPrison = self._choixParametres.getNbrTourMaxPrison()
        probSortirPrison = self._choixParametres.getProbPayerSortirPrison()

        if(DEBUG):
            print("[DEBUG] Paramètres: nombre de dés: " + str(nbrDes))
            print("[DEBUG] Paramètres: nombre max de tour en prison: " + str(nbrMaxTourPrison))
            print("[DEBUG] Paramètres: probabilité de payer pour sortir de prison: " + \
                str(probSortirPrison))

        self._selectedDataMonopoly.setNbrDeDes(nbrDes)
        self._selectedDataMonopoly.setMaxTourPrison(nbrMaxTourPrison)
        self._selectedDataMonopoly.setProbSortirPrison(probSortirPrison)


    """
        Permet de mettre à jour le graphique en fonction du nombre de tour choisi

        @param pointFixe permet de savoir si on veut mettre à jour le graphique en fonction des 
            probabilité après une "infinité" de tour (c'est à dire lorsqu'il n'y a plus de variation
            des états)
    """
    def updateNewTour(self, pointFixe = False):
        nbrTour = self._nbrTourFrame.getNbrTourASimuler()

        if(pointFixe):
            newData = self._selectedMonopoly.simulerInfini()
            if(DEBUG):
                print("[DEBUG] Simulation des points fixe")

        else:
            if(DEBUG):
                print("[DEBUG] Simulation de " + str(nbrTour))

            newData = self._selectedMonopoly.simulerDesTours(nbrTour)
            newData = self._selectedMonopoly.getResultatSimulation()

        self._statFrame.updateCanvas(newData)




