sayi = 23
dorumu = True

while dorumu:
    tahmin = int(input("Sayi gir :"))
    if tahmin == sayi:
        print("bildin")
        dorumu = False
    elif tahmin < sayi:
        print("Daha buyuk bir sayi girmeyi dene")
    else:
        print("Daha kucuk bir sayi dene")
else:
    print("Doru  tahmin gg")
print("Tebrikler")

