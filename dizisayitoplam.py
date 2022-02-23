# Bir sayı dizisi ve bir k sayısı var.
# Bu dizideki herhangi iki sayının toplamının k olup olmadığını bulunuz. 


dizi = [10,15,3,7]
k = 17 
sonuc = []


for eleman in dizi :
    x = 17 - eleman
    for i in dizi :
        if x == i :
            sonuc.append(i)
            sonuc.append(eleman)
print(sonuc)


##  Yukarıdaki kodu fonksiyon yaptık ... 


def f (list,toplam):
    dizi = [10,15,3,7]
    k = 17 
    sonuc = []


    for eleman in dizi :
        x = 17 - eleman
        for i in dizi :
            if x == i :
                sonuc.append(i)
                sonuc.append(eleman)
    return(sonuc)


print(f(dizi, k ))
