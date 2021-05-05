#Auteurs: Menzou Jughurta 300128659 et Barth Angelo
print('Barth Angelo et Menzou Jughurta 300128659')

#########Q1:

def triangle(n):#Fonction qui affiche un triangle d'étoile en fonction de n
    if n==1:        #Condition de base 
        print('*'*n)
    else:   
        triangle(n-1)#Appel a la fonction avec (n-1) cela sera un recursivité.
        print('*'*n)#imprime '*' multiplié par n
        
##########Q2:
        
def prodListePos_rec(l,n):#Fonction qui multiplie les nombres positive des elements d'une liste
    '''(list,int)->int'''
    
    if n==1:       #Condition de base si n==1
        if l[0]>=0:#Si le premiers élément de la liste est superieurs ou égale a 0, k egale a 1.
            k=l[0]

        else:
            k=1
        
    
    else:                         #Autre creation de la variable x qui vaut lappel a la fonction avec la meme liste mais en (n-1)
        x=prodListePos_rec(l,n-1)
        if(l[n-1]>=0):           #Condition sur les éléments de la liste si elle sont vrais alors..
            k=x*l[n-1]          #k égale a l'élement*x
        else:
            k=x
    return k
