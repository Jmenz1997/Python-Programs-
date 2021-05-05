#Auteur: Menzou Jughurta
#Numéro d'étudiant: 300128659
print('auteur: Menzou Jughurta')
print('numéro d\'étudiant : 300128659')
#-----Ce programme retourne la langeur maximale des nombres consécutives égaux dans une liste.
def sequenceMax(nombres):#<----Fonction qui prend un seule paramètre une liste.
    i = 0                #<----Définition de 'i' égale a '0'.
    M = 0                #<----Variable 'M' qui représente la langeur maximale.
    while 0 <= i < len(nombres):#<---- Utiliser la boucle 'while' tant que le 'i' est entre 0 et la langeur de la liste.
        t = 1                   #<----Variable qui enregistre temporairement la longeurs des élements consécutive.
        for j in range(i+1, len(nombres)):#<----Utilisation de la boucle "For".
            if nombres[j] != nombres[i]:  #<----Condition Si élément de nombres[j] n'égale pas a nombres[i] alors i=j et le programme sera suspendu et va sauter les ligne et recomence la boucle. 
                i = j                     
                break
            t += 1                        #<----Dans le cas ou nombres[j]==nombres[i] le programme va ajouter a 't' +1 qui est notre compteur de notre liste.
            i += 1                        #<----i+=1 a chaque boucle on ajout a 'i'+1.
        if t > M:                         
            M = t  
        if i == len(nombres) - 1:
            M==1
            break
    return M
#-----------------PROGRAME PRINCIPALE--------------#
nombre=list(eval(input('Veuillez entrer une liste de valeurs séparées par des virgules: ')))
print(sequenceMax(nombre))
