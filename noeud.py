class Noeud:
    """Class Noeud"""

    idNoeud = 0

    def __init__(self):
        Noeud.idNoeud += 1
        self.__id = Noeud.idNoeud
        self.__lien = []

    def __str__(self):
        print("id = "+str(self.__id))
        self.afficherID()

    def afficherID(self):
        for i in range(len(self.__lien)):
            print(self.__lien[i])

    def getIDN(self):
        return self.__id

    def addLien(self,idLien):
        self.__lien.append(idLien)

