from copy import deepcopy as copie 

def verifie_01(Liste):
    for bit in Liste:
        if bit !=0 and bit !=1:
            return False
    return True

def somme(Liste):
    S=0
    for bit in Liste:
        S+=bit
    return S%2

def rajoute_bit_parite(Liste):
    L2 = copie(Liste)
    L2.append(somme(L))
    return L2

def decodage_parite(L):
    if len(L)>=2:
        if somme(L) == 1:
            print("il y a eu une erreur")
            return
        return L[0:len(L)-1]
    return 

#L = [0,1,1,0,1]
L = [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1]

def repetition(L,k):
    L2 = []
    for bit in L:
        for _ in range(k):
            L2.append(bit)
    return L2

def decodage_majoritaire(L,k):

    L2 = []
    for i in range(0,len(L),k):
        c1 = 0
        c0 = 0
        for j in range (k):
            if L[i+j] == 1:
                c1 += 1
            else:
                c0 += 1
        if c1 > c0 and c1 <= k:
            L2.append(1)
        elif c0 > c1 and c0 <= k:
            L2.append(0)
        else:
            print("impossible de decoder!")
            return
    return L2

    


#print(repetition(L,3))

print(decodage_majoritaire(L,3))