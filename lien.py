class Lien:
    """Classe Lien"""
    IDLien = 0

    def __init__(self, n1, n2, distance):
            """Initialize the values"""
            Lien.IDLien+=1

            self.__id = Lien.IDLien
            self.noeudExtre1 = n1
            self.noeudExtre2 = n2
            self.distance = distance

    def getIDL(self):
            return self.IDLien

    def GetDistance(self):
            return self.distance

    def getIDN1(self):
            return self.noeudExtre1

    def getIDN2(self):
            return self.noeudExtre2

    def __str__(self):
        print("id = "+str(self.__id) + "   Noeud Extrêmité 1 : "+str(self.noeudExtre1) + "   Noeud Extrêmité 2 : "+str(self.noeudExtre2) + "   Distance : "+str(self.distance))


