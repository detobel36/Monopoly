#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk

class Parametres(tk.Toplevel):

    # Paramètres par défaut
    DEFAULT_DES = 2
    DEFAULT_TOUR_PRISON = 3
    DEFAULT_PROB_SORTIR_PRISON = 0.5


    def __init__(self):
        tk.Toplevel.__init__(self)
        self.ouvrirFenetreParametres()


    """
        Permet d'initialiser la fenêtre graphique
    """
    def ouvrirFenetreParametres(self):
        self.title("Paramètres")

        self.__addNombreDeDes()
        self.__addNombreTourMaxPrison()
        self.__addProbPayerSortirPrison()

        # Ajout d'un bouton à cette fenêtre
        self.__addSubmitButton()


    """
        Permet de mettre une entrée permettant de choisir le nombre de dés qui seront utilisé
        pour simuler le Monopoly
    """
    def __addNombreDeDes(self):
        tk.Label(self, text="Nombre de dés:").pack()

        self._entryNbrDeDes = tk.StringVar()
        _entry = tk.Entry(self, textvariable=self._entryNbrDeDes, justify='right', width=7)\
            .pack()
        self._entryNbrDeDes.set(str(Parametres.DEFAULT_DES))


    """
        Permet d'ajouter une entrée permettant de choisir le nombre de tour que l'on va passer
        en prison
    """
    def __addNombreTourMaxPrison(self):
        tk.Label(self, text="Nombre de tour en prison:").pack()

        self._entryNbrTourPrison = tk.StringVar()
        _entry = tk.Entry(self, textvariable=self._entryNbrTourPrison, justify='right', width=7)\
            .pack()
        self._entryNbrTourPrison.set(str(Parametres.DEFAULT_TOUR_PRISON))


    """
        Permet de choisir quel sera la probabilité qu'un joueur paye pour sortir de prison
    """
    def __addProbPayerSortirPrison(self):
        tk.Label(self, text="Probabilité de payer pour sortir de prison:").pack()

        self._entryProbPayerSortirPrison = tk.StringVar()
        _entry = tk.Entry(self, textvariable=self._entryProbPayerSortirPrison, justify='right', width=7)\
            .pack()
        self._entryProbPayerSortirPrison.set(str(Parametres.DEFAULT_PROB_SORTIR_PRISON))


    def __addSubmitButton(self):
        tk.Button(self, text='Valider', command=self.__closeParametres).pack(pady=10)


    """
        Fonction appellé lorsque l'on a totalement fini de parametré
    """
    def __closeParametres(self):
        self.quit()
        self.destroy()


    """
        Permet de récupérer le nombre de dés avec lequelle la partie de Monopoly va se dérouler
        (Par défaut: 2)

        @return le nombre de dés
    """
    def getNbrDeDes(self):
        nbrDeDes = int(self._entryNbrDeDes.get())
        # Le nombre de dés doit être strictement suppérieur à 0
        if(nbrDeDes <= 0):
            print("[WARNING] Le nombre de dé doit toujours être strictement suppérieur à 0 " \
                "(actuellement: " + str(nbrDeDes) + ")")
            nbrDeDes = 1

        return  nbrDeDes


    """
        Permet de récupérer le nombre de tour maximum qu'un joueur peut passer en prison
        (Par défaut: 3)

        @return le nombre de tour maximum que peut passer un joueur en prison
    """
    def getNbrTourMaxPrison(self):
        nbrDeTour = int(self._entryNbrTourPrison.get())
        if(nbrDeTour < 0):
            print("[WARNING] Le nombre de tour passé en prison doit toujours être positif " \
                "(actuellement: " + str(nbrDeTour) + ")")

        return nbrDeTour


    """
        Permet de récupérer la probabilité que le joueur décide de sortir de prison en payant
        plutôt qu'en essayant de lancer les dés (1 = il paye directement, 0 il paye seulement quand 
        il n'a plus le choix)
        (Par défaut: 0.5)

        @return la probabilité qu'a le joueur de sotir de prison en payant
    """
    def getProbPayerSortirPrison(self):
        probabilite = float(self._entryProbPayerSortirPrison.get())
        # La probabilité doit être comprise entre 0 et 1
        if(probabilite < 0):
            probabilite = 0
            print("[WARNING] La probabilité doit toujours être suppérieure ou égale à 0 " \
                "(actuellement: " + str(probabilite) + ")")

        elif(probabilite > 1):
            probabilite = 1
            print("[WARNING] La probabilité doit toujours être inférieur ou égale à 1 " \
                "(actuellement: " + str(probabilite) + ")")

        return probabilite
