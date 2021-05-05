#AUTEUR: Menzou Jughurta 300128659/ Tahani Kravtsov 300146260
#Programme: Ce programme est un jeu de sudoku qui interagie avec l'utilisateur.
print('Auteur: Menzou Jughurta 300128659 et Tahani kravtsov 300146260')

import math        #importer le module math.
def modifierMat(matrice):#fonction qui prend en paramètre une matrice.
    '''(list)-->(list) ce programme permet de modifier les nombres paire
       de la matrices par leurs racine carrée'''
    i=0             #Compteur a 0 de L'index utiliser sur la boucle while.
    while i<len(matrice): #Utiliser boucle while pour parcourir la liste
        j=0
        while j<len(matrice[i]):#Utiliser boucle while a l'interieur de la 1 ere boucle cela permet de parcourir la matrice.
            if matrice[i][j]%2==0:#Condition si le chiffre de la matrice est un pairs(identifier si un paire en utilisant le modulo).
                matrice[i][j]=math.sqrt(matrice[i][j])# si la condition est vrais il va modifier le nombre paire qui est dans la matrice en racine carée de ce nombre la.
            j+=1#a chaque boucle compteur j va  s'additioner +1, meme chose pour i.
        i+=1

    print(matrice)#Appel la fonction print() pour afficher la nouvelle matrice.
                
