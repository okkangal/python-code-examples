# verilen kelimedeki büyük harflerin index numarasını bir liste ile veren kod denemesi :) 

def buyukbul(kelime):
    liste = list()
    for i in kelime : 
        if i.isupper() == True :
            liste.append(kelime.index(i))
    return(liste)



print(buyukbul("KanGal"))




