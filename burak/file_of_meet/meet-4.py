dnm_liste=["ahmet","Ali","Hasan"]
print(dnm_liste)
dnm_liste.append("Necdet")
print(dnm_liste)

dnm_liste.insert(2,"Ali")
print(dnm_liste)


dnm_liste.remove("Ali")
print(dnm_liste)

print(dnm_liste.index("Hasan"))

dnm_liste.pop()
print(dnm_liste)

print("Hasan" in dnm_liste)

print(len(dnm_liste))
"""
53
1
53
%==0
"""
for i in range(1,5):
    c=c+i
    print(c)

"""
a="\rqweasd qwesad qwe"

print(len(a))
print(a.upper())
print(a)
"""
#list_a=a.split("\n")
#print(list_a)

"""
a=8.12
b=4.32
print("{} çarpı {} ={ 1:2f }".format(a,b,a*b))
print(f"{a} çarpı {b} ={a*b}")
"""
"""
dnm_2=dnm_liste
print(hex(id(dnm_2)))
print(hex(id(dnm_liste)))
dnm_liste=["Ahmet"]
print(dnm_2)
print(hex(id(dnm_2)))

print(hex(id(dnm_liste)))

list1 = ["a", "b" , "c", 3]
list2 = [1, 2, 3]

list3 = list1 + list2
list3=list(set(list3))
print(list3)
ad=input("Adınız: ")
print("Merhaba "+ad)

a=int(input("sayı giriniz"))
b=int(input("sayı giriniz"))
c=a*b
print("girdiğiniz sayıların çarpımı: " + str(c))
"""