# -*- coding: utf-8 -*-
from monopoly.Case import *
from monopoly.CaseChance import CaseChance
from monopoly.CaseCommunaute import CaseCommunaute
from monopoly.CaseGoToPrison import CaseGoToPrison
from monopoly.CasePrison import CasePrison
from copy import deepcopy


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
        self._nom = nom
        self._displayNom = displayNom
        self._defaultListCase = listCase
        self._nbrCaseClassique = -1     # Nombre de case "normal" du monopoly

        _allDataMonopoly.append(self)


    """
        Permet d'initialiser correctement un Monopoly et de créé a proprement parlé
        l'ensemble des cases où le joueur peut aller
    """
    def initMonopoly(self):
        self._listCase = self.__initAllCases(0)

        # Initialisation des cases prisons
        self._nbrCaseClassique = len(self._listCase)
        self._listCase += self.__initPrisonCases()

        # Règle des triples doubles
        for i in range(self.getNbrDeDouble()-1):
            self._listCase += self.__initAllCases(i+1)


    """
        Permet d'initialiser toutes les cases d'un plateau

        @param nombreDeDouble le nombre de double pour pouvoir atteindre les cases que l'on est
            entrain de créer
    """
    def __initAllCases(self, nombreDeDouble):
        res = [getCaseDepart()] + deepcopy(self._defaultListCase)

        for case in res:
            case.setNbrDeDouble(nombreDeDouble)

        return res


    """
        Permet d'initialiser le nombre de case prison nécessaire

        @return une liste de case prison en fonction des paramètres (définit plus tôt)
    """
    def __initPrisonCases(self):
        return [CasePrison(self._nbrCaseClassique, i) for i in range(self._maxTourPrison)]


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
        Permet de récupérer une case en fonction de son numéro sur le plateau

        @param numeroCase le numero de la case à récupérer
        @param nbrDoubleDe le nombre de double que le joueur à du faire pour arriver à cette case
            (facultatif: 0 par défaut)
        @return la case (ou None si pas trouvé)
    """
    def getCase(self, numeroCase, nbrDoubleDe = 0):
        numeroCase = numeroCase % self._nbrCaseClassique # On fait en sorte que ça ne dépasse pas du plateau
        return self.__getExactCase(numeroCase, nbrDoubleDe)


    """
        Permet de récupérer un numero de case très précis.  Aucune vérification n'est faite

        @param numeroCase le numero de case à récupérer
        @param nbrDoubleDe nombre de double des qu'aura du faire le joueur pour atteindre cette case
            (facultatif: 0 par défaut)
        @return la case (ou None si pas trouvé)
    """
    def __getExactCase(self, numeroCase, nbrDoubleDe = 0):
        for case in self._listCase:
            if(case.getPosition() == numeroCase and case.getNbrDeDouble() == nbrDoubleDe):
                return case
        return None


    """
        Permet de récupérer la case prison (celle correspondant au premier tour du joueur)

        @return la Case prison correspondant au premier tour
    """
    def getCasePrison(self, nbrTourEnPrison = 0):
        return self.__getExactCase(self._nbrCaseClassique+nbrTourEnPrison)


    """
        Permet de récupérer la case "prison visite uniquement"

        @return la case "prison visite uniquement"
    """
    def getPrisonVisiteUniquement(self):
        return self.getCase(CASE_PRISON_VISITE_SIMPLE)


    """
        Permet de récupérer toutes les cases du monopoly

        @return la liste des cases
    """
    def getListeCases(self):
        return self._listCase


    ##### Définition des paramètres pouvant changé la configuration du monpoly #####

    def getMaxTourPrison(self):
        return self._maxTourPrison

    def setMaxTourPrison(self, nbrMaxTour):
        self._maxTourPrison = nbrMaxTour

    def getNbrDeDes(self):
        return self._nbrDeDes

    def setNbrDeDes(self, nbrDeDes):
        self._nbrDeDes = nbrDeDes

    def getProbSortirPrison(self):
        return self._probSortirPrison

    def setProbSortirPrison(self, probSortirPrison):
        self._probSortirPrison = probSortirPrison

    def getNbrDeDouble(self):
        # TODO changer par un paramètre
        return NOMBRE_DOUBLE


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

DataMonopoly("MERVEILLES_MONDE", "Monopoly Merveilles du monde", [
    Case("Les Chutes du Niagara", 1, "orchid", 60), 
    CaseCommunaute(2),
    Case("L'Everest", 3, "orchid", 60),
    Case("Assurance Voyage", 4, "beige", 200),
    Case("Amsterdam Schiphol", 5, "white", 200), # TODO couleur
    Case("La Grande Barrière de Corail", 6, "deep sky blue", 100),
    CaseChance(7),
    Case("Le Grand Canyon", 8, "deep sky blue", 100),
    Case("Les chutes Angel", 9, "deep sky blue", 120),
    Case("Prison simple visite", 10),
    Case("Le Christ Rédempteur", 11, "dark slate blue", 140),
    Case("Bureau de Change", 12, "ivory", 150),
    Case("La Tour Eiffel", 13, "dark slate blue", 140),
    Case("Le Colisée", 14, "dark slate blue", 160),
    Case("Paris Charles de Gaulle", 15, "white", 200),
    Case("Les ruines de Stonehenge", 16, "dark orange", 180),
    CaseCommunaute(17),
    Case("Le Taj Mahal", 18, "dark orange", 180),
    Case("Les statues Moai", 19, "dark orange", 200),
    Case("Parking", 20),
    Case("Machu Picchu", 21, "orange red", 220),
    CaseChance(22),
    Case("Le temple Angkor Wat", 23, "orange red", 220),
    Case("Pétra", 24, "orange red", 240),
    Case("Rhein-Main Frankfurt", 25), # TODO
    Case("La grande Muraille de Chine", 26, "gold", 260),
    Case("Le phare d'Alexandrie", 27, "gold", 260),
    Case("Agent de voyages", 28, "ivory", 150),
    Case("Le colosse de Rhodes", 29, "gold", 280),
    CaseGoToPrison(30),
    Case("Le mausolée, Halicarnasse", 31, "sea green", 300),
    Case("La statue de Zeus, Olympie", 32, "sea green", 300),
    CaseCommunaute(33),
    Case("Le temple d'Artémis à Ephèse", 34, "sea green", 320),
    Case("London Heathrow", 35), # TODO
    CaseChance(36),
    Case("Les jardins suspendus de Babylone", 37, "dark slate blue", 350),
    Case("Taxe de Luxe", 38, "black", 100),
    Case("La grande Pyramide de Gizeh", 39, "dark slate blue", 400)
    ])
