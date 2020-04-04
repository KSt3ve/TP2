from graphe import Graphe


class GrapheOriente(Graphe):
    def __init__(self):
        Graphe.__init__(self,id)

    def obtenirProchainsNoeuds(self,IdNoeud):
        LienUtiliser = list
        NoeudSuivant = {}
        if IdNoeud in self._dicoNoeuds:
            noeud = self._dicoNoeuds[IdNoeud]
            LienUtiliser = noeud.getIDL()
        for i in LienUtiliser:
            lien = self._dicoLiens[i]
            NoeudSuivant[lien.getIDN1()] = lien.GetDistance()
        return LienUtiliser, NoeudSuivant