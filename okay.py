# verilen kelimedeki b�y�k harflerin index numaras�n� bir liste ile veren kod denemesi :) 

def buyukbul(kelime):
    liste = list()
    for i in kelime : 
        if i.isupper() == True :
            liste.append(kelime.index(i))
    return(liste)



print(buyukbul("KanGal"))




