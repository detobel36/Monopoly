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
    def __init__(self, numero):
        super().__init__("Prison " + str(numero), DECALAGE_PRISON+numero, "black", -1)


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
        # Si il n'y en a pas, on est obligé de payé
        if(nextPrison == None):
            proportionPayer = 1
        # Sinon ça va dépendre de ce que le joueur à décidé
        else:
            proportionPayer = CHOOSE_PAYE/100

        # => Payer pour sortir
        res[dataMonopoly.getCase(10)] = proportionPayer # Retour sur "prison visite seulement"

        # Si on est pas obligé de payé
        if(proportionPayer < 1):
            # => Lancer les dés
            nbrArangementPossible = pow(6, NBR_DES)

            # TODO le dé n'est pas équiréparti pour les doubles

            # Faire un double
            proportionJouer = 1-proportionPayer
            for i in range(NBR_DES, NBR_DES*6+1, NBR_DES):
                res[dataMonopoly.getCase(self._position+i)] = (1/nbrArangementPossible)*proportionJouer

            # Aucun double n'a été fait
            res[nextPrison] = ((nbrArangementPossible-6)/nbrArangementPossible)*proportionJouer

        return res

    """
        Permet de récupérer la case prison juste après la case actuelle (si elle n'existe pas, 
        on renvoie None)

        @parma dataMonopoly les informations liées au plateau monopoly
        @return la prochaine case prison ou None si pas trouvé
    """
    def __getNextCasePrison(self, dataMonopoly):
        res = None # Resultat
        currentPos = self.getPosition()

        if(currentPos < (DECALAGE_PRISON+MAX_TOUR_PRISON)):
            res = dataMonopoly.getCase(currentPos+1, True)

        return res
