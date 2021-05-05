#AUTEUR: Menzou Jughurta 300128659/ Tahani Kravtsov 300146260
#Programme: Ce programme est un jeu de sudoku qui interagie avec l'utilisateur.
print('Auteur: Menzou Jughurta 300128659 et Tahani kravtsov 300146260')
def calculPrix(article,quantite):
    ''' (str,int)---> float. ce programme calcule et affiche le prix de nombre de l'article voulu
        précondition: chaque article a sont prix unique.
    '''
    
    if article=='bureau':    
       prix=(quantite*75.9)#Multiplication de la quantité avec le prix de chaque article spécifié au dessus.
    elif article=='chaise':
        prix=(quantite*50.9)
    elif article=='imprimante':
         prix=(quantite*32.5)
    elif article=='scanneur':
        prix=(quantite*28.0)
    
    else:
        prix=False      
    
    
    return prix

#Question b): Calcul du prix totale d'une commande en utilisant la fonction calculPrix():
def calculTotal(article1,quantite1,article2,quantite2,article3,quantite3):
    ''' (str,int,str,int,str,int)--> float,
           calcule le prix totale de trois articles '''
    lePrix=calculPrix(article1,quantite1)
    lePrix=calculPrix(article2,quantite2)+lePrix
    lePrix=calculPrix(article3,quantite3)+lePrix #Addition des trois articles avec leur quantité apres avoir appeler la fonctions aprés chaque article calculTotal qui calcule le prix des articles d'apres leur quantités.
    


    return lePrix

#Question c): Sous-algorithme qui permet la verification de la quantité de chaque article demandé:
def validerCommande(article1,quantite1,article2,quantite2,article3,quantite3): 
    '''(str,int,str,int,str,int)-----> Bool.
       Vérifie si la commande est valide
       précondtion: les noms des article similaire a ceux dans l'inventaire et quantité depasse pas leur quantité maximum.'''
    #Utilisation de condition 'if' pour valider que l'utilisateur a bien entrer le nom de l'article et la quantité valide.
    if article1=='bureau' and  quantite1<=9 or article1=='chaise' and  quantite1<=25 or article1=='imprimante' and quantite1<=46 or article1=='scanneur' and quantite1<=17:
        r1=True
    else:
        r1=False
    
    if article2=='bureau' and  quantite2<=9 or article2=='chaise' and  quantite2<=25 or article2=='imprimante' and quantite2<=46 or article2=='scanneur' and quantite2<=17:
        r2=True
    else:
        r2=False
    if article3=='bureau' and  quantite3<=9 or article3=='chaise' and  quantite3<=25 or article3=='imprimante' and quantite3<=46 or article3=='scanneur' and quantite3<=17:
        r3=True 
    else:
        r3=False
    if r1==False or r2==False or r3==False:#Si une des condition précedente est fausse la fonction return faux si elle sont toute vrais return True.
        return False
    else:
        return True
#--------------------------Programme Principale---------------------------#
#Question d):  En utilisante tout les fonction précedent on a pu crée un programme qui vérifie tout les commande donner par l'utilisateur puis lui permettre de voir le cout totale de sa commande.
q={'bureau':9,'chaise':25, 'imprimante':46,'scanneur':17}          #Dictionnaire sur l'inventaire (stock) des articles et leur quantité valide
p={'bureau':75.9,'chaise':50.9,'imprimante':32.5,'scanneur':28.0}
while True:                                                        #Boucle qui sera toujours True pour implementer l'exception.
  try:                                                             #l'exception a l'interieur de la boucle si l'utilisateur entre les renseignements valide-
    aR1=str(input('Entrez le premier article: '))                  #-alors la boucle s'arrete a l'aide de 'break' si l'utilisateur entre des renseignement
    q1=int(input('Entrez la quantité de votre 1ere article: '))    #-éronner alors affiche une message pour réintroduire des renseignement de type valide.
    aR2=str(input('Entrez le deuxieme article: '))
    q2=int(input('Entrez la quantité de votre 2eme article: '))
    aR3=str(input('Entrez le troisième article: '))
    q3=int(input('Entrez la quantité de votre 3eme article: '))
    break                                                
  except ValueError:
      print('Veuillez entrez un entier dans les quantité. Merci')
Validation=validerCommande(aR1,q1,aR2,q2,aR3,q3)                 #pour valider si la commande est correct on appel la fonction validerCommande pour confirmer la disponibilté des commande entrer.
Totalite=calculTotal(aR1,q1,aR2,q2,aR3,q3)#permet d'appeler le sous-algorithme calculTotal qui ce dernier utilise un autre sous-alghorithme qui vont nous calculer la totalié de notre commande si cette dernier est valide.
if Validation==True:                      #Si la validation est vrais or la fonction(validercommande) retourn vrais le programme
    print('Le prix total de votre commande est:',Totalite,'$.Merci et à la prochaine.')#Si l'utilisateur à entrer les articles et quantités qui sont disponible dans le magasin de vente le programme affichera ce message.        
    for i in q: #Boucles for pour q le dictionnaire des inventaires a l'interieur des boucle les conditions permettent de supprimé la quantité des articles acheté.
        if 'bureau' in i and aR1 == 'bureau' or 'chaise' in i and aR1=='chaise' or 'scanneur' in i and aR1=='scanneur' or 'imprimante' in i and aR1=='imprimante':
           q[i]=q[i]-q1
    for z in q:
        if 'bureau' in z and aR2 == 'bureau' or 'chaise' in z and aR2=='chaise' or 'scanneur' in z and aR2=='scanneur' or 'imprimante' in z and aR2=='imprimante':
           q[z]=q[z]-q2
    for x in q:
        if 'bureau' in x and aR3 == 'bureau' or 'chaise' in x and aR3=='chaise' or 'scanneur' in x and aR3=='scanneur' or 'imprimante' in x and aR3=='imprimante':
            q[x]=q[x]-q3
    print('Les quantités disponsibles aprés l\'achat sont:\n',q) #Affiche (q dictionnaire) quantité aprés l'achat.
if Validation==False:
     print('Votre commande est annulée. SVP, vérifier les articles et les quantités\n',q)#si l'utilisateur a entrer les article et quantité indisponible au magasin alors le programme affiche ce message.


