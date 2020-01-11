"""a=[1,2,3,4,5,5,6,4,2,8,7]#list
b=(1,2,3,4)#tuple
c={"asd":"asd","dsa":3}
print(c)
d={1,2,3,4,5}
print(d)
a=list(set(a))"""
"""sayi=int(input("bir sayi giriniz"))
kelime=input("bir kelime giriniz")
print(str(sayi)+"tane"+kelime)#12 tane elma
print(sayi,"tane",kelime)"""
"""a=5
b=4

#or and 
if a<b:
    print("a kucuktur b ")
elif a>b:
    print("a buyuktur b")

else:
    print("a esittir b")"""

"""a=["elma","armut","karpuz"]
for i in a:
    print(i)"""
"""a=[3,6,2,8,0,6]

b=[]
for i in a:
    b.append(i**2)
print(b)"""

"""a=1
while a<10:
    print(a)
    a+=1 
print("a nin son degeri:",a)"""

"""a=1
while a!=5:
    print(a)
    a+=1
print("a nin son degeri:",a)"""
"""a=1
while a<10:
    if a!=5:
        print(a)
    a+=1
print("a nin son degeri",a)"""

"""sayi=int(input("bir sayi gircek misin"))
for i in range(3,sayi+1,3):
    print(i)"""
puan=0
el_sayisi=0
while puan<1000 and el_sayisi<6 :
    oldurulen_adam=int(input("kac adam oldurdun ?"))
    puan=puan+oldurulen_adam*100
    el_sayisi+=1
if puan<1000 :
    print("oyunu bitiremediniz")
else :
    print("oyunu",el_sayisi,"defada",puan,"puanla bitirdin")  
      
    
