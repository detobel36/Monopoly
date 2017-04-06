# -*- coding: utf-8 -*-

# Afficher ou non les messages de DEBUG
# Type: Boolean
DEBUG = True


# Nombre de dés dans la partie
# Type: int
NBR_DES = 2


# Nombre de tour maximum que l'on passe en prison
# Type: int
MAX_TOUR_PRISON = 3


# Les cartes prisons n'existent pas physiquement. On leur attribue donc un ID fixé à partir de
# cette valeur
# Type: int
DECALAGE_PRISON = 50


# Chance en pourcent que le joueur paye sa sortie de prison (chaque tour est indépendant)
# Donc 50 représente le fait que le joueur à une chance sur deux de payer OU de lancer les dés
# Type: nombre
CHOOSE_PAYE = 50


# Définit le nombre de tour maximum que l'on peut simuler
# Type: int
MAX_TOUR_SIMULE = 30
