# -*- coding: utf-8 -*-
from monopoly.Case import Case
from Constantes import *


"""
    Permet de réprésenter une case Prison

    Informations: 
    La case prison fait soit référence à la prochaine case prison (de base 3 chances), soit à une 
    case pouvant être atteint via un double.

    /!\ Warning !  La case prison est donc dupliqué pour représenter les différents tours que l'on 
    peut passer sur celle-ci.
"""
class CasePrison(Case):

    """
        Permet d'initiliser une case Prison

        @param numero de la case prison (représentant le nombre de tour passé sur cette case)
    """
    def __init__(self, decalage, numero):
        super().__init__("Prison " + str(numero+1), decalage+numero, "black", -1)
        self._tourEnPrison = numero


    """
        Permet de récupérer les cases accèssibles depuis la case actuelle

        @param dataMonopoly les informations liées au plateau monopoly (permettant de récupérer 
            les autres cases)
        @return liste des objets cases étant accèssibles
        @Override
    """
    def getCasesSuivantes(self, dataMonopoly):
        res = {}

        # On récupère la prison suivante
        nextPrison = self.__getNextCasePrison(dataMonopoly)

        if(nextPrison == None): # Si il n'y en a pas, on est obligé de payé
            proportionPayer = 1
        else: # Sinon ça va dépendre de ce que le utilisateur à décidé
            proportionPayer = dataMonopoly.getProbSortirPrison()

        # Case "prison visite uniquement"
        casePrisonVisiteUniquement = dataMonopoly.getPrisonVisiteUniquement()
        posCasePrisonVisite = casePrisonVisiteUniquement.getPosition()
        
        # => Payer pour sortir
        res[casePrisonVisiteUniquement] = proportionPayer # Retour sur "prison visite seulement"

        # Si on est pas obligé de payer
        if(proportionPayer < 1):
            nbrDeDes = dataMonopoly.getNbrDeDes()

            # => Lancer les dés
            nbrArangementPossible = pow(6, nbrDeDes)

            # Faire un double
            proportionJouer = 1-proportionPayer
            nombreDeDouble = 0
            for i in range(nbrDeDes, nbrDeDes*6+1, nbrDeDes):
                res[dataMonopoly.getCase(posCasePrisonVisite+i)] = (1/nbrArangementPossible)*proportionJouer
                nombreDeDouble += 1

            # Aucun double n'a été fait
            res[nextPrison] = ((nbrArangementPossible-nombreDeDouble)/nbrArangementPossible)*proportionJouer

        return res

    """
        Permet de récupérer la case prison juste après la case actuelle (si elle n'existe pas, 
        on renvoie None)

        @parma dataMonopoly les informations liées au plateau monopoly
        @return la prochaine case prison ou None si pas trouvé
    """
    def __getNextCasePrison(self, dataMonopoly):
        res = None # Resultat

        # Si ce n'est pas notre dernier tour en prison
        if(self._tourEnPrison < dataMonopoly.getMaxTourPrison()):
            res = dataMonopoly.getCasePrison(self._tourEnPrison+1)

        return res
