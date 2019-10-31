ad = input("Adinizi giriniz : ")
kazananlar = ["ali","veli"]
sayi = 0
for karakter in ad:
    sayi = sayi + 1
if ad in kazananlar:
    print("Kazananlar listesindesiniz")

print("Adinizda", sayi, "karakter var")
