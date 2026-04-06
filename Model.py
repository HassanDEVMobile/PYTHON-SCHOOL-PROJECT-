import sqlite3
from sqlite3.dbapi2 import Date
from webbrowser import get


class Equipe :
    def __init__(self,Id,Nom,NbEtoile,ClassFifa,emails):
        self.Id = Id
        self.Nom = Nom
        self.NbEtoile = NbEtoile
        self.ClassFifa = ClassFifa
        self.emails = emails
class Joueur :
    def __init__(self,Id,Nom_prenom,age,poste,IdEquipe,Club):
        self.Id = Id
        self.Nom_prenom = Nom_prenom
        self.age = age
        self.poste = poste
        self.IdEquipe = IdEquipe
        self.Club = Club
class Match :
    def __init__(self,Id,NomStade,IdEquipeDomicil,IdEquipeVisit,Date):
        self.Id = Id
        self.NomStade = NomStade
        self.IdEquipeDomicil = IdEquipeDomicil
        self.IdEquipeVisit = IdEquipeVisit
        self.Date = Date
class Competions :
    # Cette methode va nous permettre de creer la Table Equipe qui va nous permettre de sauvegarder les informations de chaque Equipe
    def TableEquipe (self):
        conn = sqlite3.connect('Competions.db')
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Equipes (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nom TEXT,
        NbEtoile INTEGER,
        ClassFifa INTEGER,
        emails TEXT
        """)
        conn.close()

#Cette methode nous permettra d'afficher un Match dans notre Boucle for que nous utilisons pour afficher tous les matchs
class AfficherMatch :
    def __init__(self,EquipeDomicilNom):
        self.EquipeDomicilNom = EquipeDomicilNom
    def __get__(self):
        return (self.EquipeDomicilNom)

    def afficheMatch(self,result,list=[]):
         return f"Match : {list[0]} vs {list[1]} Stade : {result[3]} Date : {result[2]} "


    # Cette methode va nous permettre de creer la Table Joueur qui va nous permettre de sauvegarder les informations de chaque Joueur
    def TableJoueur (self):
        conn = sqlite3.connect('Competitions.db')
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Joueurs (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nom_prenom TEXT,
        age INTEGER,
        post TEXT,
        IdEquipe INTEGER,
        Club TEXT       
        """)
        conn.close()

    # Cette methode va nous permettre de creer la Table Match qui va nous permettre de sauvegarder les informations de chaque Match
    def TableMatch (self):
        conn = sqlite3.connect('Competitions.db')
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Match (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        NomStade TEXT,
        IdEquipeDomicil INTEGER,
        IdEquipeVisit INTEGER,
        Date TEXT
        """)
        conn.close()

    #Cette methode permet de d'ajouter un joueur dans la competition
    def saveJoueur(self,joueur:Joueur):
      conn = sqlite3.connect('Competitions.db')
      cursor = conn.cursor()
      cursor.execute("""
      INSERT INTO Competitions 
      (Nom_prenom,age,poste,IdEquipe,Club)
        VALUES (?,?,?,?,?)
         """,(joueur))
      conn.commit()
      conn.close()

    #Cette methode permet de d'ajouter une Equipe dans la competition
    def saveEquipe(self,equipe : Equipe):
        conn = sqlite3.connect('Competitions.db')
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Equipes
        (Nom, NbEtoile,ClassFifa,emails)
        VALUES
        (?,?,?,?)
        """,(equipe))
        conn.commit()
        conn.close()

    #Cette methode permet de d'ajouter un Match dans la competition
    def saveMatch(self,match:Match):
        conn = sqlite3.connect('Competitions.db')
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Match
        ( NomStade,IdEquipeDomicil,IdEquipeVisit,Date)
        VALUES
        (?,?,?,?)
        """,(match))
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
        List = []
        cptr = 0
        conn = sqlite3.connect('Competitions.db')
        cursor = conn.cursor()
        cursor.execute("SELECT IdEquipeDomicil,IdEquipeVisit,Date,NomStade FROM Match ")
        result = cursor.fetchall()
        for match in result:
            for recup in match:
                if cptr == 2 :
                    tuple = (recup,)
                    conn = sqlite3.connect('Competitions.db')
                    cursor = conn.cursor()
                    requete = cursor.execute("SELECT Nom FROM Equipes WHERE Id=? ", (tuple))
                    reqResult = requete.fetchone()
                    conn.close()
                    affichematch = AfficherMatch(reqResult[0])
                    List.append(affichematch)
                    cptr = cptr + 1
                    break
        print(affichematch.afficheMatch(result,List))
        List.clear()
        conn.close()

    #Cette methode nous permettra de lister tous les Joueurs d'une Equipe
    def FindAllJoueursEquipe(self,IdEquipe):
        conn = sqlite3.connect('Competitions.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Joueurs WHERE IdEquipe=? ",(IdEquipe))
        joueurs = cursor.fetchall()
        return joueurs