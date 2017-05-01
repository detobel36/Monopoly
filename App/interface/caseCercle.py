

"""
    Class représentant le cercle lié à une case (la représentation graphique de la case)
"""
class CaseCercle:


    def __init__(self, canvas, case, coordLeftX, coordRightX, coordTopY, coordBottomY):
        self._case = case
        self._canvas = canvas
        self._allRelationArc = []
        self._allRelationCase = []

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
        Permet d'ajouter une arête représentant une relation entre la case actuelle et une autre
        case

        @param idRelation id de l'arc de cercle reliant les deux cases
        @param case destination
    """
    def addRelation(self, idRelation, relationCase):
        self._allRelationArc.append(idRelation)
        self._allRelationCase.append(relationCase)


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
        for elem in self._allRelationArc:
            self._canvas.itemconfig(elem, fill="red")
            self._canvas.itemconfig(elem, width=4)

        for case in self._allRelationCase:
            case.highlight()

    """
        Permet d'afficher normalement toutes les cases
        @see __viewOnlyOneCase

        @param event information lié au fait que l'utilisateur intéragit avec l'objet 
            (par défaut None)
    """
    def __resetViewOnlyOneCase(self, event):
        for elem in self._allRelationArc:
            self._canvas.itemconfig(elem, fill="gray")
            self._canvas.itemconfig(elem, width=1)

        for case in self._allRelationCase:
            case.unHighlight()


    """
        Permet de mettre en évidence la case actuelle
    """
    def highlight(self):
        self._canvas.itemconfig(self._idCreatedOval, outline="red")
        self._canvas.itemconfig(self._idCreatedOval, width=3)

    """
        Permet de retirer la mise en évidence fait au préalable
    """
    def unHighlight(self):
        self._canvas.itemconfig(self._idCreatedOval, outline="gray")
        self._canvas.itemconfig(self._idCreatedOval, width=1)

