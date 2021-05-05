# -*- coding: utf-8 -*-

#Auteur: Menzou Jughurta
#Numéro d'étudiant: <300128659>
print('Auteur: Menzou Jughurta')
print('Numéro d\'étudiant: <300128659> ')

def palindrome(chaine):
    chaine=str(chaine)
    i = 0
    l=len(chaine)
    while i < l :
        if chaine[i] != chaine[-i-1]:
            return False
        else:
            return True
        i= i+1
    return bool

