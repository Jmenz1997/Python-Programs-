#Auteur: Menzou Jughurta
#Numéro d'étudiant: 300128659
print('auteur: Menzou Jughurta')
print('numéro d\'étudiant : 300128659')

# Jeu de cartes appelé "Pouilleux" 

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

def attend_le_joueur():#done
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():#done
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente tous les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):#done
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)

def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
     et ça continue jusqu'à la fin du paquet p.
     '''
     
     donneur=[]
     autre=[]
     
     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     
     for i in range(0,25):
         donneur.append(p[i])
     for l in range(25,len(p)):
        autre.append(p[l])
     
     return (donneur, autre)#<----retourne la liste des carte de donneur et autres.


def elimine_paires(l):
    '''
     (list of str)->list of str

     Retourne une copy de la liste l avec tous les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''
    
    resultat=[]


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
    trouve = False#<----Variable type(bool)
    
    for val in l:#<----Boucle 'for' pour la liste 'l'.
        for res in resultat:#<----Boucle 'for' introduite dans la 1 ére boucle pour la liste 'resultat'.
            if val[:-1] == res[:-1]:#<---Condition si l'élément dans 'l' égale à  l'élément de 'resultat'.
                resultat.remove(res)#<--- supprime l'element 'res' de 'resultat' or les paires.
                trouve = True
                break
        
        if not trouve:
            resultat.append(val)
        else:
            trouve = False
    random.shuffle(resultat)
    return resultat  #<-----Retourne la liste sans paires.


def affiche_cartes(p):#<----Fonctions qui affiche les élements de la p séparer avec des éspace.
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
    for s in p:
        print(s+' ')
    

    

def entrez_position_valide(n):
     '''
     (int)->int
     Retourne un entier du clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas dans l'intervalle [1,n]
     
     Précondition: n>=1
     '''

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     print('SVP,entrez un entier valide entre 1 et',n,':')
     n_entier=int(input('=> '))
     while not (1<=n_entier<=n):
            n_entier=int(input('Position non valide. Réintroduisez un entier : '))
     
     return n_entier#<---- Retourne un entier tapez par l'utilisateur qui serviras a récupérer la carte de Robot et l'entier represente la position da la carte dans la list.

def joue():
     '''()->None
     Cette fonction joue le jeu'''
    
     p=prepare_paquet()
     melange_paquet(p)
     tmp=donne_cartes(p)
     donneur=tmp[0]
     humain=tmp[1]

     print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
     print("Votre main est:")
     affiche_cartes(humain)
     print("\nNe vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
     print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
     attend_le_joueur()
     
     donneur=elimine_paires(donneur)
     humain=elimine_paires(humain)

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     while len(humain)!=1 or len(donneur)!=1:
           print('*********************************************************')
           print('Votre tour.')
           print('Votre main est:')
           affiche_cartes(humain)
     
           print('\nJ\'ai',len(donneur)-1,'cartes. Si 1 est la position de ma première carte et',len(donneur)-1,'est la position de ma dernière carte,laquelle de mes cartes voulez-vous?')
           j=entrez_position_valide(len(donneur)-1)
           if j==1:
               print('Vous avez demandé ma 1ère carte.')
           else:
               print('Vous avez demandé ma',j,'ème carte.')
           print('La voilà. C\'est un',donneur[j])
           print('Avec',donneur[j],'ajouté, votre main est:')
           humain.append(donneur[j])
           donneur.remove(donneur[j])
           
           affiche_cartes(humain)
           print('\nAprés avoir défaussé toutes les paires et mélangé les cartes, votre main est:\n')
           humain=elimine_paires(humain)
           affiche_cartes(humain)
           attend_le_joueur()
           if len(humain)==1:
              print('J\'ai terminé toutes les cartes.')
              print('Félicitation! Vous, Humain, vous avez gagné.')
              break
           print('***********************************************************')
           print('Mon tour.')
           z=random.randrange(1,len(humain)-1)
           donneur.append(humain[z])
           humain.remove(humain[z])
           donneur=elimine_paires(donneur)
           if len(donneur)==1:
              print('J\'ai terminé toutes les cartes.')
              print('Vous avez perdu! moi, Robot, j\'ai gagné')
              break
           if z==1:
              print('J\'ai pris votre 1 ère carte.')
           else:
              print('J\'ai pris votre',z+1,'ème carte.')
     
     
     

	 
# programme principale
joue()
####<----------FIN DU PROGRAMME------->####
