# -*- coding: utf-8 -*-
from monopoly.Case import *
from monopoly.CaseChance import CaseChance
from monopoly.CaseCommunaute import CaseCommunaute
from monopoly.CaseGoToPrison import CaseGoToPrison
from monopoly.CasePrison import CasePrison


# Liste de tous les DataMonopoly
_allDataMonopoly = []


"""
    Class permettant de stocker et récupérer des inforamtions sur un monopoly
"""
class DataMonopoly:

    """
        Permet d'initiliser les informations.

        @param nom des informations monopoly (permettant de le retrouver et de l'identifier)
        @param displayNom nom à afficher
        @param listCase liste (dans l'ordre) des cases (la case départ est ajoutée automatiquement)
    """
    def __init__(self, nom, displayNom, listCase):
        self.__initParam()
        self._nom = nom
        self._displayNom = displayNom
        self._listCase = [getCaseDepart()] + listCase + self.__initDefaultCase()

        _allDataMonopoly.append(self)


    """
        Permet d'initialiser tous les champs qui pourront être modifié
    """
    def __initParam(self):
        self._maxTourPrison = MAX_TOUR_PRISON
        # TODO ne peut pas fonctionner dans l'état actuelle


    """
        Permet de récupérer les cases par défaut qui doivent être rajouté aux informations

        @return une liste de case ajouté par défaut
    """
    def __initDefaultCase(self):
        return [CasePrison(i+1) for i in range(self._maxTourPrison)]


    """
        Permet de récupérer le nom des informations monopoly

        @return le nom
    """
    def getNom(self):
        return self._nom


    """
        Permet de récupérer le nom à afficher concernant ces informations monopoly

        @return le nom à afficher
    """
    def getDisplayNom(self):
        return self._displayNom


    """
        Permet de récupérer une case en fonction de son numero

        @param numeroCase le numero de la case à récupérer
        @param true pour éviter de vérifier que l'on est bien dans le plateau de jeu
        @return la case (ou None si pas trouvé)
    """
    def getCase(self, numeroCase, no_limit = False):
        if(not no_limit):
            numeroCase = numeroCase % len(self._listCase)

        for case in self._listCase:
            if(case.getPosition() == numeroCase):
                return case
        return None

    """
        Permet de récupérer la case prison (celle correspondant au premier tour du joueur)

        @return la Case prison correspondant au premier tour
    """
    def getCasePrison(self):
        return self.getCase(DECALAGE_PRISON+1, True)


    """
        Permet de récupérer toutes les cases du monopoly

        @return la liste des cases
    """
    def getListeCases(self):
        return self._listCase




############################ STATIC ############################

"""
    Permet de récupérer un "DataMonopoly" en fonction de son nom

    @param nom du monopoly que l'on cherche
    @return le DataMonopoly ou None si pas trouvé
"""
def getDataMonopoly(nom):
    for data in _allDataMonopoly:
        if(data.getNom() == nom):
            return data
    return None

"""
    Permet de récupérer tous les Monopoly disponibles

    @return une liste avec tous les noms des monopoly
"""
def getAllDataMonopoly():
    res = []
    for data in _allDataMonopoly:
        res.append(data)
    return res



############################ Initialisation ############################

# Couleur en Tkinter: http://wiki.tcl.tk/37701
# nom, position, couleur = "white", prix = 0

DataMonopoly("MONOPOLY_70", "Monopoly édition 70è anniversaire", [
    Case("Wavre Rue du commerce", 1, "sienna"), 
    CaseCommunaute(2),
    Case("Aalst Niewstraat", 3, "sienna"),
    Case("Impôts sur le revenu", 4, "beige"),
    Case("Aéroport de Bruxelles Zaventem", 5),
    Case("Sint-truiden Luiderstraat", 6, "dodger blue"),
    CaseChance(7),
    Case("Verviers place Verte", 8, "dodger blue"),
    Case("Mechelen Bruul", 9, "dodger blue"),
    Case("Prison simple visite", 10),
    Case("Arlon Grand'Rue", 11, "hot pink"),
    Case("Telecoms", 12),
    Case("Kortrijk Lange SteenStraat", 13, "hot pink"),
    Case("Mons Grand Rue", 14, "hot pink"),
    Case("Aéroport de Charleroi", 15),
    Case("Oostende Kapellestraat", 16, "dark orange"),
    CaseCommunaute(17),
    Case("Leuven Bondgenotenlaan", 18, "dark orange"),
    Case("Knokke Lippenslaan", 19, "dark orange"),
    Case("Parking", 20),
    Case("Charleroi Rue de la Montagne", 21, "orange red"),
    CaseChance(22),
    Case("Liège Rue de la Cathédrale", 23, "orange red"),
    Case("Antwerpen Huidevetterstraat", 24, "orange red"),
    Case("Aéroport de Liège", 25),
    Case("Hasselet Hoogstraat", 26, "gold"),
    Case("Brugge Steenstraat", 27, "gold"),
    Case("Internet", 28),
    Case("Namur Rue de Fer", 29, "gold"),
    CaseGoToPrison(30),
    Case("Bruxelles Av. Louise", 31, "sea green"),
    Case("Liège Pont d'Île", 32, "sea green"),
    CaseCommunaute(33),
    Case("Gent Veldstraat", 34, "sea green"),
    Case("Luchthaven Antwerpen", 35),
    CaseChance(36),
    Case("Antwerpen Meir", 37, "dark slate blue"),
    Case("Taxe de Luxe", 38),
    Case("Bruxelles Rue Neuve", 39, "dark slate blue")
    ])
