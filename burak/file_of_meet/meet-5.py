"""sayi=int(input("Bir sayı giriniz: "))
bolen=0
for i in range(2,sayi):
    if sayi%i == 0:
        bolen+=1 #bolen=bolen + 1
if bolen>0:
    print(str(sayi) + " asal sayı değildir.")
else:
    print(str(sayi) + " asal sayıdır.23")"""

"""sayi2=int(input("Bir rakam giriniz 1-9: "))
sonuc=sayi2+sayi2*11+sayi2*111
print(sonuc)"""
"""sayi=(input("a"))
if type(sayi)==type("a"):
    print("olmadı")"""

"""sayi=0
while sayi<10:
    print(sayi)
    sayi+=1

while sayi>0:
    print(sayi)
    sayi-=1"""

"""if sayi==0: print("çalışıyor")"""

sifre="asd"
kont_sif=input("Şifrenizi giriniz: ")
count=1
while sifre != kont_sif and count<3:
    kont_sif=input("Girdiğiniz şifre hatalı, tekrar giriniz: ")
    count+=1

if sifre==kont_sif:
    print("Hoşgeldiniz")