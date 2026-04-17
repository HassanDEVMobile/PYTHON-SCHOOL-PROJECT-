import sqlite3
from sqlite3.dbapi2 import Date
from webbrowser import get

conn = sqlite3.connect('Competitions.db')
cursor = conn.cursor()
class Equipe :
    def __init__(self,Id,Nom,NbEtoile,ClassFifa,emails):
        self.Id = Id
        self.Nom = Nom
        self.NbEtoile = NbEtoile
        self.ClassFifa = ClassFifa
        self.emails = emails
    def __init__(self,Nom,NbEtoile,ClassFifa,emails):
        self.Nom = Nom
        self.NbEtoile = NbEtoile
        self.ClassFifa = ClassFifa
        self.emails = emails
class Joueur :
    def __init__(self,Id,Nom_prenom,age,post,IdEquipe,Club):
        self.Id = Id
        self.Nom_prenom = Nom_prenom
        self.age = age
        self.post = post
        self.IdEquipe = IdEquipe
        self.Club = Club
    def __init__(self,Nom_prenom,age,post,IdEquipe,Club):
        self.Nom_prenom = Nom_prenom
        self.age = age
        self.post = post
        self.IdEquipe = IdEquipe
        self.Club = Club
class Match :
    def __init__(self,Id,NomStade,IdEquipeDomicil,IdEquipeVisit,Date):
        self.Id = Id
        self.NomStade = NomStade
        self.IdEquipeDomicil = IdEquipeDomicil
        self.IdEquipeVisit = IdEquipeVisit
        self.Date = Date
    def __init__(self,NomStade,IdEquipeDomicil,IdEquipeVisit,Date):
        self.NomStade = NomStade
        self.IdEquipeDomicil = IdEquipeDomicil
        self.IdEquipeVisit = IdEquipeVisit
        self.Date = Date

#Cette Classe contient Toute les requetes SQL de la BASE DE DONNEES
class CompetitionsRepository :



        # Cette methode permet de d'ajouter un joueur dans la competition
        def saveJoueur(self,joueur: tuple):
          conn = sqlite3.connect('Competitions.db')
          cursor = conn.cursor()
          cursor.execute("""
          INSERT INTO Joueurs (Nom_prenom,age,post,IdEquipe,Club)
          VALUES (?,?,?,?,?) """, (joueur))
          conn.commit()
          conn.close()



        def saveEquipe(self, equipe : tuple ):
                conn = sqlite3.connect('Competitions.db')
                cursor = conn.cursor()
                cursor.execute("""
                INSERT INTO Equipes (Nom, NbEtoile,ClassFifa,emails)
                VALUES (?,?,?,?) """, (equipe))
                conn.commit()
                conn.close()

        def saveMatch(self,match : tuple):
          conn = sqlite3.connect('Competitions.db')
          cursor = conn.cursor()
          cursor.execute("""
          INSERT INTO Match (NomStade,IdEquipeDomicil,IdEquipeVisit,Date)
          VALUES (?,?,?,?) """,(match))
          conn.commit()
          conn.close()



        #Cette methode nous permettra de lister tous les joueurs de la competition
        def FindAllJoueurs(self):
          conn = sqlite3.connect('Competitions.db')
          cursor = conn.cursor()
          cursor.execute("SELECT * FROM Joueurs ")
          joueurs = cursor.fetchall()
          return joueurs

    #Cette methode nous permettra de lister Toutes les Equipes de la competition
        def FindAllEquipes(self):
          conn = sqlite3.connect('Competitions.db')
          cursor = conn.cursor()
          cursor.execute("SELECT * FROM Equipes ")
          equipes = cursor.fetchall()
          return equipes

      #Cette methode nous permettra de lister tous les Matchs de la competition
        def FindAllMatches(self):

          conn = sqlite3.connect('Competitions.db')
          cursor = conn.cursor()
          cursor.execute("SELECT IdEquipeDomicil,IdEquipeVisit,Date,NomStade FROM Match ")
          result = cursor.fetchall()
          conn.close()
          return result



       #Cette methode permet de lsiter tous les Joueurs d'une equipe
        def FindAllJoueursEquipe(self,IdEquipe : tuple):
          conn = sqlite3.connect('Competitions.db')
          cursor = conn.cursor()
          cursor.execute("SELECT * FROM Joueurs WHERE IdEquipe=? ",(IdEquipe))
          joueurs = cursor.fetchall()
          return joueurs

        # Cette methode va nous permettre de creer la Table Equipe qui va nous permettre de sauvegarder les       informations de chaque Equipe
       # conn = sqlite3.connect('Competions.db')
       # cursor = conn.cursor()


        cursor.execute("DROP TABLE IF EXISTS Equipes")
        # Cette requete permet de créér la table Equipes
        cursor.execute("""CREATE TABLE IF NOT EXISTS Equipes (
             Id INTEGER PRIMARY KEY AUTOINCREMENT,
             Nom TEXT,
             NbEtoile INTEGER,
             ClassFifa INTEGER,
             emails TEXT)
             """)


        cursor.execute("DROP TABLE IF EXISTS Joueurs")
        # Cette requete Sql permet de créér la table Joueurs
        cursor.execute("""CREATE TABLE IF NOT EXISTS Joueurs (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Nom_prenom TEXT,
                age INTEGER,
                post TEXT,
                IdEquipe INTEGER,
                Club TEXT)       
                """)

        cursor.execute("DROP TABLE IF EXISTS Match")
        # Cette requete permet de créér la table Match
        cursor.execute("""CREATE TABLE IF NOT EXISTS Match (
               Id INTEGER PRIMARY KEY AUTOINCREMENT,
               NomStade TEXT,
               IdEquipeDomicil INTEGER,
               IdEquipeVisit INTEGER,
               Date TEXT)
               """)
        conn.close()
#Cette methode nous permettra d'afficher un Match dans notre Boucle for que nous utilisons pour afficher tous les matchs
class AfficherMatch :
    def __init__(self,EquipeDomicilNom):
        self.EquipeDomicilNom = EquipeDomicilNom
    def __get__(self):
        return (self.EquipeDomicilNom)

    def afficheMatch(self,result :tuple,list=[]):
         return f"Match : {list[0]} vs {list[1]} Stade : {result[3]} Date : {result[2]} "


