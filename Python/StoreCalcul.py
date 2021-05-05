#Auteur:Jughurta Menzou.
#Numéro d'étudiant: <300128659>.
print('Auteur: Menzou Jughurta')
print('Numéro d\'étudiant: 300128659')
#Question a): Calcul de prix d'un article on fonction de sa quantité.
def calculPrix(article,quantite):
    
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
#Question b): Calcul du prix totale d'une commande en utilisant le sous-algorithme calculPrix():
def calculTotal(article1,quantite1,article2,quantite2,article3,quantite3):
    monprix=calculPrix(article1,quantite1)
    monprix=calculPrix(article2,quantite2)+monprix
    monprix=calculPrix(article3,quantite3)+monprix #Addition des trois articles avec leur quantité apres avoir appeler le sous_algorithme calculTotal qui calcule le prix des articles d'apres leur quantités.
    


    return monprix
#Question c): Sous-algorithme qui permet la verification de la quantité de chaque article demandé:
def validerCommande(article1,quantite1,article2,quantite2,article3,quantite3): 
    if article1=='bureau' and  quantite1<=9 or article1=='chaise' and  quantite1<=25 or article1=='imprimante' and quantite1<=46 or article1=='scanneur' and quantite1<=17:
        r=True
    else:
        r=False
    if article2=='bureau' and  quantite2<=9 or article1=='chaise' and  quantite2<=25 or article2=='imprimante' and quantite2<=46 or article2=='scanneur' and quantite2<=17:
        True
    else:
         r=False
    if article3=='bureau' and  quantite3<=9 or article3=='chaise' and  quantite3<=25 or article3=='imprimante' and quantite3<=46 or article3=='scanneur' and quantite3<=17:
        True
    else:
         r=False
                 
    return bool(r) 

#Question d):  En utilisante tout les sous-algorithme précedent on a pu crée un programme qui vérifie tout les commande donner par l'utilisateur puis lui permettre de voir le cout totale de sa commande:
aR1=input('Entrez le premier article: ') 
q1=int(input('Entrez la quantité de votre 1ere article: '))
aR2=input('Entrez le deuxieme article: ')
q2=int(input('Entrez la quantité de votre 2eme article: '))
aR3=input('Entrez le troisième article: ')
q3=int(input('Entrez la quantité de votre 3eme article: '))
Validation=validerCommande(aR1,q1,aR2,q2,aR3,q3)#pour valider si la commande est correct on appel le sous algorithme validerCommande pour confirmer la disponibilté des commande entrer.
Totalite=calculTotal(aR1,q1,aR2,q2,aR3,q3)#permet d'appeler le sous-algorithme calculTotal qui ce dernier utilise un autre sous-alghorithme qui vont nous calculer la totalié de notre commande si cette dernier est valide.
if Validation==True:
    print('Le prix total de votre commande est:',Totalite,'$.Merci et à la prochaine.') #Si l'utilisateur à entrer les article et quantité qui sont disponible dans le magasin de vente le programme affichera ce message.
if Validation==False:
    print('Votre commande est annulée. SVP, vérifier les articles et les quantités')#si l'utilisateur a entrer les article et quantité indisponible au magasin alors le programme affiche ce message.


    
    

        
    
  
                
    
    
           

    







            

