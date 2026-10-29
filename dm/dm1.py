from copy import deepcopy as copie 

#L = [0,1,1,0,1]
#L = [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
#L = [[0,1,0],[1,1,0],[0,1,1]]
#L = [[0, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1]]

def verifie_01(L):
    for bit in L:
        if bit !=0 and bit !=1:
            return False
    return True

def somme_modulo(L):
    S=0
    for bit in L:
        S+=bit
    return S%2

def rajoute_bit_parite(L):
    L2 = copie(L)
    L2.append(somme_modulo(L))
    return L2

def decodage_parite(L):
    if len(L)>=2:
        if somme(L) == 1:
            print("il y a eu une erreur")
            return
        return L[0:len(L)-1]
    return 

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
    
def rajoute_parite_croise(L):
    L_croise = []
    L_colone = []
    for i in range (len(L)):
        L_tempon = []
        L_croise.append(rajoute_bit_parite(L[i])) #n-1 premieres lignes ok, pas ligne des bits de parite
        #recup n-1 premieres colones, pas les bits de parite
        for k in range (len(L)):
            L_tempon.append(L[k][i])
        L_colone.append(L_tempon)
    L_tempon = []
    #recup n_eme colone, bit de parite
    for j in range(len(L_croise)):
        L_tempon.append(L_croise[j][len(L_croise[0])-1])
    L_colone.append(L_tempon)
    L_tempon = []
    #n_eme ligne, ligne des bit de parite
    for l in range (len(L_colone)):
       L_tempon.append(somme_modulo(L_colone[l]))
    L_croise.append(L_tempon)
    return L_croise

def parite_lignes(L):
    L_indicel = []
    for i in range (len(L)):
        if somme_modulo(L[i]) == 1:
            L_indicel.append(i)
    return L_indicel

def parite_colones(L):
    L_colone =[]
    L_indicec = []
    for i in range (len(L)):
        L_tempon = []
        for k in range (len(L)):
            L_tempon.append(L[k][i])
        L_colone.append(L_tempon)
    for j in range (len(L_colone)):
        if somme_modulo(L_colone[j]) == 1:
            L_indicec.append(j)
    return L_indicec 

def decodage_parite_croise(L):
    L_final = copie(L)
    if parite_colones(L) == [] and parite_lignes(L) == []:
        L_final.pop()
        for i in range (len(L_final)):
            L_final[i].pop()
        return L_final
    elif len(parite_colones(L)) >= 2 or len(parite_lignes(L)) >= 2:
        print ("on ne peut pas decoder ce texte, il y a eu trop d'erreurs")
        return
    else:
        vligne = parite_lignes(L)[0]
        vcolone = parite_colones(L)[0]
        if L_final[vligne][vcolone] == 1:
            L_final[vligne][vcolone] = 0
        else:
            L_final[vligne][vcolone] = 1
        L_final.pop()
        for i in range (len(L_final)):
            L_final[i].pop()
        return L_final
