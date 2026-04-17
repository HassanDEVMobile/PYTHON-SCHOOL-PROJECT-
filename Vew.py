

class MenuCp :

    #Cette methode permettra d'afficher les differentes options dans la console
    def MenuCompetitons(self):
        print("""
               ================================================================
                            MENU PRINCIPALE DE LA COMPETITION 
               ================================================================
                1-AJOUTER UNE EQUIPE
                2-AJOUTER UN JOUEUR DANS UNE EQUIPE
                3-CREER UN MATCH ENTRE DEUX EQUIPES
                4-AFFICER LES EQUIPES DE LA COMPETITION
                5-AFFICHER LES JOUEURS D'UNE EQUIPES
                6-AFFICHER LES JOUEURS D'UNE EQUIPES
                7-AFFICHES LES MATCHS DE LA COMPETION
                0-QUITTER L'APPLICATION
        """)

    #Cette Methode permettra de recupder le choix de l'utilisateur
    def DemanderChoix(self):
        while (ValueError) :
             try :
                 choix = int(input("Veuillez selectionner une option : "))
                 if choix < 0   or choix > 6 :
                    print("Erreur Le choix doit etre compris entre 0 et 6")
                 else :
                     print("Connexion reussi Chargement en cours .......")
                     return choix
                     break
             except ValueError :
                 print("Erreur de Valeur")


    #Cette methode Represente notre interface pour ajouter une equipe
    def AjouterEquipe(self):
        NomEquipe = (input("Veuillez saisir Le nom de L'équipe :"))
        NbEtoile = int(input("Veuillez saisir le Nombre d'étoile de l'équipe : "))
        Classfif = int(input("Veuillez saisir le classement fifa de l'équipe : "))
        email = (input("Veuillez saisir l'email de l'équipe (xxxxx@gmail.com) : "))
        return NomEquipe,NbEtoile,Classfif,email



    #Cette methode Represente notre interface pour ajouer un Joueur dans une équipe
    def AjouterJoueurEquipe(self):
        Nom_Prenom = input("Veuillez saisir le nom et le prenom du joueur : ")
        age = int(input("Veuillez saisir l'age du joueur de l'équipe : "))
        poste = input("Veuillez saisir le poste du joueur :")
        IdEquipe = int(input("Veuillez saisir l'Identifiant de l'équipe du joueur : "))
        club = input("Veuillez saisir le Nom du club du joueur : ")
        return Nom_Prenom,age,poste,IdEquipe,club


    #Cette methode Represente notre interface pour Creer un match entre deux équipes
    def CreerMatch(self):
        NomStade = input("Veuillez saisir le nom du stade : ")
        IdEquipeDomicil = int(input("Veuillez saisir l'Identifiant de l'équipe Domicile : "))
        IdEquipeVisit = int(input("Veuillez saisir l'Identifiant de l'équipe Extérieur :"))
        Date = input("Veuillez saisir le date du Match : ")
        return NomStade,IdEquipeDomicil,IdEquipeVisit,Date


     #Cette Methode Nous permettra d'afficher Toute les équipe de la competions
    def AfficherEquipe(self,List : list):
       for element in List:
           print(f"Nom : {element[0]}, Nombre d'étoile : {element[1]} , Classement Fifa : {element[2]} , Email : {element[3]}" )


    #Cette Methode Nous permettra de demander l'identifiant de l'equipe dont on affichera la liste de tous les Joueurs qui la compose
    def DemancderIdEquipe(self):
        IdEquipe = int(input("Veuillez saisir l'Identifiant de l'equipe dont vous voulez afficher les joueurs : "))
        return IdEquipe


    #Cette methode nous permttra d'afficher la liste des Joueurs d'une équipe
    def AfficherJoueurEquipe(self,List : list):
        for element in List:
            print(f"Nom et prenom : {element[0]} , age : {element[1]} , poste : {element[2]} , IdEquipe : {element[3]}")


    #Cette methode nous permettra d'afficher tous les matchs de la competitions
    def AfficherMatchs(self,List : list):
        for element in List:
            print(element)