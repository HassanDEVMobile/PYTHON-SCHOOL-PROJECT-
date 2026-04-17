from Model import CompetitionsRepository, Equipe, Joueur, Match
from Vew import MenuCp



class Controller :
    def __init__(self):
        self.menucp = MenuCp()
        self.compt = CompetitionsRepository()
    def AJOUTEREQUIPE(self):
        Nom ,NbEtoile,ClassFifa,emails = self.menucp.AjouterEquipe()
        equipe = Equipe( Nom ,NbEtoile,ClassFifa,emails)
        montuple = tuple(equipe.__dict__.values())
        self.compt.saveEquipe(montuple)


    def AJOUTERJOUEUREQUIPE(self):
        Nom_prenom, age, poste, IdEquipe, Club = self.menucp.AjouterJoueurEquipe()
        print(Nom_prenom, age, poste, IdEquipe, Club)
        joueur = Joueur(Nom_prenom,age,poste,IdEquipe,Club)
        montuple = tuple(joueur.__dict__.values())
        self.compt.saveJoueur(montuple)


    def CREERMATCH(self):
        NomStade, IdEquipeDomicil, IdEquipeVisit, Date = self.menucp.CreerMatch()
        match = Match(NomStade, IdEquipeDomicil, IdEquipeVisit, Date)
        montuple = tuple(match.__dict__.values())
        self.compt.saveMatch(montuple)


    def AFFICHEREQUIPE(self):
       self.menucp.AfficherEquipe(self.compt.FindAllEquipes())


    def AFFICHERJOUEUREQUIPE(self):
             montuple = tuple([self.menucp.DemancderIdEquipe()])
             self.compt.FindAllJoueursEquipe(montuple)
             print(self.menucp.AfficherJoueurEquipe(self.compt.FindAllJoueursEquipes(montuple)))

    def AFFICHERMATCH(self):
        self.menucp.AfficherMatchs(self.compt.FindAllMatches())


    def Appdemarrer(self):
        fermeture = True
        while (fermeture == True):
            self.menucp.MenuCompetitons()
            Choix = self.menucp.DemanderChoix()
            if Choix == 1:
              self.AJOUTEREQUIPE()
            elif Choix == 2:
              self.AJOUTERJOUEUREQUIPE()
            elif Choix == 3:
              self.CREERMATCH()
            elif Choix == 4:
              self.AFFICHEREQUIPE()
            elif Choix == 5:
              self.AFFICHERJOUEUREQUIPE()
            elif Choix == 6:
                self.AFFICHERMATCH()
            elif Choix == 0:
                print("Application Fermer ........")
                fermeture = False
            else :
                print("Veuillez faire le bon choix")