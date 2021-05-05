#Auteur: Menzou Jughurta
#Numéro d'étudiant: 300128659
print('auteur: Menzou Jughurta')
print('numéro d\'étudiant : 300128659')
#-----Programme qui retourne True 'Type(Booléan)' si il y'a une séquence de deux éléments consécutifs égaux, et False(Booléan) si il n'yen à pas.
def sequenceDesDeux(nombres):        #<----Fonctions qui prend un seule paramétre 'nombres' de type list.
    fauxOuVrais=False                #<----Variable "fauxOuVrais"  de Type(Bool) déclaré à "False".
    for i in range(0,len(nombres)):  #<----Utilisation de la boucle 'For' qui permet de passer en boucle  les donnée du paramètre 'nombres'.                
        if nombres[i]==nombres[i+1]: #<----Conditioner la boucle: Si le 1ér numéro  égale au 2 ème numéro donc on va prendre en considération la consécutivité de notre liste donc notre condition est vrais "True".
            fauxOuVrais=True
            break
        else:                        #<----Autre:Si y'a les deux numéro qui ce suivent ne sont pas égaux donc notre condition est Fausse "False".
            fauxOuVrais=False        
    return fauxOuVrais               #<----Retourne la variable de type(bool)




#-----PROGRAMME--PRINCIPALE-----#
liste=list(eval(input('Veuillez entrer une liste de valeurs séparées par des virgules : ')))#<----Demander à l'utilisateur d'entrez sa liste entre chaque numéro mettre virgule.

print(sequenceDesDeux(liste))        #<-----Affiche le resultat aprés avoir appeler notre fonction mais en paramétre les données de l'utilisateur.


#<=================================================FIN DU PROGRAMME MERCI================================================>#
            

        
