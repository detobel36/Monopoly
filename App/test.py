# -*- coding: utf-8 -*-
from Monopoly import *
from structure.Markov import *


def printResult(monopoly):
    results = monopoly.getResultatSimulation()
    for case in results:
        print(str(case.getPosition()) + ". " + case.getNom() + ": " + str(round(results[case], 5)))


res = getMonopoly("MONOPOLY_70")
printResult(res)

res.simulerDesTours(5)
printResult(res)


# matDeplacement = res.creerMatriceDeplacementMonopoly()
# # print(matDeplacement)
# # print("Taille: " + str(matDeplacement.getNbrCol()))
# # print("")
# matInit = res.creerMatriceInitialMonopoly()
# # print(matInit)
# # print("Taille: " + str(matInit.getNbrCol()))

# markov = Markov(matInit, matDeplacement)
# print(markov.getMatriceDeplacement())
# print("----")
# markov.ajouterDeplacement(5)
# print(markov.getMatriceDeplacement())

# print("")
# print("---------")
# print("")
# print(markov.multiplicationInitiatialeDeplacement())