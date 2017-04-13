

"""
    Class représentant le cercle lié à une case (la représentation graphique de la case)
"""
class CaseCercle:


    def __init__(self, canvas, case, coordLeftX, coordRightX, coordTopY, coordBottomY):
        self._case = case
        self._canvas = canvas

        self._idCreatedOval = canvas.create_oval(coordLeftX, coordTopY, \
            coordRightX, coordBottomY, outline="gray", fill=case.getCouleur(), \
            activeoutline="red", activewidth=2)

        self.__initCaseEvent()


    """
        Permet de récupérer les coordonnées de l'objet actuel

        @return un tuple x0, y0 et x1, y1 correspondant aux coordonnées des coins délimitant l'objet
    """
    def getCoords(self):
        return self._canvas.coords(self._idCreatedOval)

    """
        Permet de déclarer les événements possibles lié à la représentation d'une case

        @param guiCaseId id graphique (sur le canvas) de la case
    """
    def __initCaseEvent(self):
        self._canvas.tag_bind(self._idCreatedOval, "<Enter>", self.__viewOnlyOneCase)
        self._canvas.tag_bind(self._idCreatedOval, "<Leave>",self.__resetViewOnlyOneCase)


    """
        Permet d'afficher uniquement les relations d'une case bien spécifique

        @param event information lié au fait que l'utilisateur intéragit avec l'objet
    """
    def __viewOnlyOneCase(self, event):
        print("Entry : " + str(self._idCreatedOval))


    """
        Permet d'afficher normalement toutes les cases
        @see __viewOnlyOneCase

        @param event information lié au fait que l'utilisateur intéragit avec l'objet 
            (par défaut None)
    """
    def __resetViewOnlyOneCase(self, event):
        print("Reset ! " + str(event))


