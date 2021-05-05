#Auteur: Menzou Jughurta
#Numéro d'étudiant: 300128659
print('auteur: Menzou Jughurta')
print('numéro d\'étudiant : 300128659')
#-----Programme qui calcule et retourn le nombre d'élément dans une liste divisible par 'n'----#


def nombreDivisible(nombres, n): #<---Fonction qui prend 2 paramétre une liste'nombres' et un entiers 'n'.
    compteur=0                   #<---Compteur à zéro.
    for i in range(len(nombres)):#<---Boucle "for" qui permet "i" de passer en boucle tout le long de notre liste 'nombres.
        if (nombres[i]%n == 0):  #<---Condition dans la boucle si élement de la liste est divisible par 'n'.
            compteur+=1          #<---Compteur qui additionne 1 a chaque fois que la Condition est correcte.
    return compteur              #<---Fonction retourne nombre de Compteur.

listeNombres=list(eval(input('Veuillez entrer une liste des entiers par des virgules : ')))#<---L'utilisateur entre les nombres séparer avec virgules.

nombreDiviseur=int(input('Veuillez entrer un entier positif : '))                          #<---L'utilisateur entre le chiffre qui dévise.
appelFonction=nombreDivisible(listeNombres,nombreDiviseur)                                 #<---Appel a la fonction 'nombreDivisible' avec comme paramètre les donnée entrer par l'utilisateur.

print('le nombre des éléments divisble par',nombreDiviseur,'est : ',appelFonction)         #<---Imprime le nombres d'élément de la liste entrer qui sont divisible par le deviseur entrer.

#############<============================================FIN DU PROGRAMME MERCI===============================================>################   
            
        
            
    

