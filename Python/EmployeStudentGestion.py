#Auteurs: Menzou Jughurta, Barth Angelo
#         300128659      , 
print('Menzou Jughurta 300128659 et Barth Angelo')
class Personne:
    '''represente une classe Personne'''
    def __init__(self, nom, prenom, identifiant):
        '''(str,str, int)->None
        initialise les attributs de la classe Personne'''
        # A completer
        #Attribut de la calsse personne.
        self.nom=nom      
        self.prenom=prenom
        self.identifiant=identifiant

    def __repr__(self):
        '''(Personne)->str
        retourne une representation de l'objet'''
        # A completer
        return ('Nom: '+self.nom+
                'Prénom: '+self.prenom+
                'Identifiant :'+ str(self.identifiant))# retourn un chaine de caractere des entré.

    def __eq__(self, autre):
        '''(Personne, Personne)->bool
        self == autre si le nom et le prenom sont les memes'''
        # A completer
        return (self.nom==autre.nom and
               self.prenom==autre.prenom and
               self.identifiant==autre.identifiant) #Retourn True si self==Autre et false sinon.

class Etudiant(Personne):
    '''represente une classe Etudiant'''
     # solde est un attribut de la classe Etudiant
     # cours est une liste de cours (une liste de chaine de caracteres)
     
     # methodes
    def __init__(self,nom,prenom,identifiant,solde=0,cours=[]):#Inisialise les Attributs..
         '''(str,str,int,int,list)->None
            Initialise les attributs de la classe Etudiant'''
     # A completer
         
         self.nom=nom
         self.prenom=prenom
         self.identifiant=identifiant
         self.solde=solde
         self.cours=cours
    def __repr__(self):
        return ('Nom: '+self.nom+' prenom: '+self.prenom+' identifiant: '
                +str(self.identifiant)+' solde: '+str(self.solde)+' cours: '
                +str(self.cours))
    def ajouterCours(self,cour):#Fonction qui permet d'ajouter un cour si le solde est egale a 0 sinon False.
        if self.solde==0:
            self.cours.append(str(cour))
            return True
        else:
            return False
class Employe(Personne):
    '''represente un employe'''
    # tauxHoraire est un attribut de la classe Employe
    # methodes

    def __init__(self,nom='',prenom='',identifiant=0,tauxHoraire=15): #inistilasiation des attributs avec taux Horraire=15($) par heure...
        self.nom=nom
        self.prenom=prenom
        self.identifiant=identifiant
        self.tauxHoraire=tauxHoraire
    def __repr__(self):
        return('Nom: '+self.nom+' prenom: '+self.prenom+' identifiant: '
                +str(self.identifiant)+' taux: '+str(self.tauxHoraire))# retourn une chaine de caractere des attributs de la classe Employe
    def calculerSalaire(self,nombreHeures):
        return self.tauxHoraire*nombreHeures
    
    
    # A completer
class Gestion:
 listEtudiant = [] 
 listEmploye = []
 def ajouterEtudiant(self):
    ''' none -> bool
    ajouter des etudiants dans une liste d'etudiant'''
    # Completer
    #Prendre les entrer de l'utilisateur a propos des informations de l'étudiant
    nom=str(input('Entrez le nom de l\'étudiant: '))
    prenom=str(input('Entrez le prénom de l\'étudiant: '))
    identifiant=int(input('Entrez l\'identifiant de l\'étudiant: '))
    solde=int(input('Entrez le solde de l\'étudiant: '))
    cours=[]
    while True:#Utilisation de l'exception avec une boucle while..cela permet de ne pas donner erreur puis redemarrer tout le programme
        try:
            entreeChoix=str(input('Si vous voulez ajoutez un cours repondez oui/non: '))
            if entreeChoix=='oui' or entreeChoix=='non': #condition si l'entrer de l'utilisateur est exactement 'oui' ou 'non' donc la boucle s'arrete avec (break).
                break
            else:
                print('SVP repondez par oui ou non') #sinon continue la boucle en affichant un message d'avertisement.
                continue
        except TypeError:
            print('SVP repondez par oui/non')
    if entreeChoix=='oui': #Si l'utilisateur entre oui cela permetrais a l'utilisateur d'entrer dans la liste un cours au choix.
        cours.append(input('Entrez le cours: '))
    
    etudiantInfo=Etudiant(nom,prenom,identifiant,solde,cours)#Variable qui est egale a la classe étudiant avec c parametre.
    if etudiantInfo in self.listEtudiant:
        print('Cet étudiant est déja ajouter')
        return True #si la variable est dans la listEtudiant retourne True/ Sinon False
    else:
        print('Cet étudiant viens d\'etre ajouter')
        self.listEtudiant.append(etudiantInfo)
        return False
    
    
 def ajouterEmploye(self): #Meme chose que la fonctions ajouterEtudiant() lit l'entrer de l'utilisateur sur les info de l'employe ensuite verifie c c'est information sont dans la list(listEmploye)
     #retourn vrais si elle existais deja/False si elle n'existais pas avant.
    ''' none -> bool
    ajouter des etudiants dans une liste d'etudiant'''
    # Completer
    nom=str(input('Entrez le nom de l\'employé: '))
    prenom=str(input('Entrez le prénom de l\'employé: '))
    identifiant=int(input('Entrez l\'identifiant de l\'employé: '))
    
    
    employeInfo=Employe(nom,prenom,identifiant)
    if employeInfo in self.listEmploye:
        print('Cet employé est déja ajouter')
        return True
    else:
        print('Cet employé viens d\'etre ajouter')
        self.listEmploye.append(employeInfo)
        return False
 def SoldeNonPaye(self):
    ''' none -> int
    retourner le nombre des etudiants qui ont un solde non paye'''
    # Completer
    
    i=0#Inisialiser compteur
    for etudiant in self.listEtudiant: #Calcule les étudiants qui on un solde>0.
            if etudiant.solde != '0':
                i = i+1 #Compteur
        
    return i #retourne le numéro des étudiant qui on le solde non payé
    

 def salaireInd(self, employe, heures):
    '''(str) -> float
    retourne le salaire d'un employe'''
    # Completer
    if employe in self.listEmploye: #employe dans la liste
            return (employe.calculerSalaire(heure))  #calcul le salaire
    else: #Si employe n'existe pas
            return 0
g = Gestion()
print("Ajoutez des etudiants.")
# Ajouter des etudiants
g.ajouterEtudiant()
g.ajouterEtudiant()

# Ajouter des employes
print("Ajouter des employes.")
g.ajouterEmploye()
g.ajouterEmploye()
#g.ajouterEmployes()

# Afficher le nombre des employes et des etudiants
print("il y a: ", len(Gestion.listEtudiant), " etudiants.")
print("il y a: ", len(Gestion.listEmploye), " employes.")
# Afficher le nombre des etudiants qui ont un solde a payer
print("il y a ", g.SoldeNonPaye(), "etudiants qui n'ont pas paye leur solde.")
# Afficher les salaires de tous les employes
for e in Gestion.listEmploye:
    heure = int(input("Entrez le nombre des heures pour employe " + e.prenom + " " + e.nom + " "))
    print('Le salaire de:', e.nom, e.prenom, 'est:', g.salaireInd(e, heure), '$.')

#Afficher toute la Gestion
print("Toute la gestion: ")
print(Gestion.listEtudiant)
print(Gestion.listEmploye)

    


    

