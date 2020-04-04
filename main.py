from graphe import Graphe
import csv

from lien import Lien
from noeud import Noeud


def mainTest ():
    graphe = createGraphe('Graphe de test','fileGraph1(1).csv')
    # graphe2 = createGraphe('Graphe2 de test','fileGraph2.csv')
    print(graphe.__str__())
    # print(graphe2.__str__())
    graphe.dijkstra(1, 5)
    # graphe2.dijkstra(1, 10)




def createGraphe(idGraphe,cheminLien):
    graphe = Graphe(idGraphe)
    with open(cheminLien, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        nbLines = 0
        for line in reader:
            if nbLines == 0:
                NbNoeud = int(line[0])
                for _ in range(0, NbNoeud):
                    noeud = Noeud()
                    graphe.addNoeud(noeud)
            else:
                graphe.addLien(int(line[0]),int(line[1]),float(line[2]))
            nbLines+=1
    return graphe


mainTest()