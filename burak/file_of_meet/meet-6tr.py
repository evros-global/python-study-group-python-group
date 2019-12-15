"""def asal_mi(sayi):
    bolen=0
    for i in range(2,sayi):
        if sayi%i == 0:
            bolen+=1
    if bolen>0:
        return False
    else:
        return True"""


"""def kuvvet_al(taban,us):
    return taban**us"""
"""
def hipotenus(kenar1,kenar2):
    hipo=(kenar1**2+kenar2**2)**(1/2)
    return hipo
a,b=1,1
while a>0 and b>0:
    a=int(input("Dik üçgenin 1. kenarının zunluğunu giriniz. "))
    b=int(input("Dik üçgenin 2. kenarının zunluğunu giriniz. "))

    print(round(hipotenus(a,b),3))
"""

"""print(15*6+kuvvet_al(4,5))
print(asal_mi(7))

a=7
if asal_mi(a):
    print("asaldır", a)
else:
    print("asal değildir", a)"""

"""a=[1,2,3,4]
b=[2,4,7,32,65,8]

def ters_liste_yazdır(liste):
    ters_liste=[]
    for i in liste:
        ters_liste.insert(0,i)
    return ters_liste
print(ters_liste_yazdır(a))
print(a)"""

"""b=ters_liste_yazdır(b)
print(b+ters_liste_yazdır(a))"""

a=[1,2,3,4,5,6]
b=[i**2 for i in a if i%2==1]
print(b)