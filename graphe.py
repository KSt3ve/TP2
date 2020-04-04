import sys


from noeud import Noeud
from lien import Lien

class Graphe :
    """Class graphe"""


    def __init__(self, id):
        self._id = id
        self._nbNoeuds = 0
        self._dicoNoeuds = {}
        self._dicoLiens = {}

    def get_Noeud(self):
        return self._nbNoeuds

    def addNoeud(self, noeud):
        self._nbNoeuds += 1
        IDnoeud = noeud.getIDN()
        self._dicoNoeuds[IDnoeud] = noeud

    def getDictNoeuds(self):
        return self._dicoNoeuds

    def addLien(self, idNoeudDep, idNoeudDest, Distance):
        lien = Lien(idNoeudDep,idNoeudDest,Distance)
        idLien = lien.getIDL()
        self._dicoLiens[idLien] = lien

        noeud1 = self._dicoNoeuds[int(idNoeudDep)]
        noeud2 = self._dicoNoeuds[int(idNoeudDest)]

        noeud1.addLien(idLien)
        noeud2.addLien(idLien)

    def obtenirProchainsNoeuds(self, IdNoeud):
        LienUtiliser = list
        NoeudSuivant = {}
        if IdNoeud in self._dicoNoeuds:
            noeud = self._dicoNoeuds[IdNoeud]
            LienUtiliser = noeud.getIDL()
        for i in LienUtiliser:
            lien = self._dicoLiens[i]
            noeud1 = lien.getIDN()
            IdN1 = noeud1.returnidNoeud
            if IdN1 == IdNoeud:
                NoeudSuivant[lien.getIDN2()] = lien.GetDistance()
            else:
                NoeudSuivant[lien.getIDN1()] = lien.GetDistance()
        return LienUtiliser, NoeudSuivant

    def __str__(self):
        print("Noeuds :")
        for value in self._dicoNoeuds.values():
            noeud = value
            print(" Noeud : " + str(noeud.getIDN()) + "\n", end="")
        print("\n Liens :")
        for value in self._dicoLiens.values():
            lien = value
            lien.__str__()



    def dijkstra(self, debut, fin):
        inf = float('inf')
        dicDistance = {}
        DicPrec = {}
        ensembleNoeuds = set()
        for key in self._dicoNoeuds.keys():
            if key == debut:
                dicDistance[key] = 0
            else:
                dicDistance[key] = inf
            DicPrec[key] = 0
            ensembleNoeuds.add(key)





    # def dijkstra(self, f, t):
    #     nodeId = f.getId()
    #     dist = [None] * len(self.getDictNoeuds())
    #     for i in range(len(dist)):
    #         dist[i] = sys.maxsize
    #         dist[i].append([self.getDictNoeuds()[nodeId]])
    #     dist[nodeId][0] = 0
    #     nodeQueue = [i for i in range(len(self.getDictNoeuds()))]
    #     nodesSeen = set()
    #     while len(nodeQueue):
    #         dist_min = sys.maxsize
    #         node_min = None
    #         for n in nodeQueue:
    #             if dist[n][0] < dist_min and n not in nodesSeen:
    #                 dist_min = dist[n][0]
    #                 node_min = n
    #         nodeQueue.remove(node_min)
    #         nodesSeen.add(nodesSeen)
    #         neighbours = self.obtenirProchainsNoeuds(node_min.getId())
    #         for (node, edge) in neighbours:
    #             dist_tot = edge.getl1() + dist_min
    #             if dist_tot < dist[node.getId()][0]:
    #                 dist[node.getId()][0] = dist_tot
    #                 dist[node.getId()][1] = list(dist[node_min][1])
    #                 dist[node.getId()][1].append(node)
    #         return dist



