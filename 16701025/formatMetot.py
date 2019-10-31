"""
Baslangic = "Burada baslar "
Son = "Burada biter "
String = "Burasi ort "

newString = Baslangic + String + Son

print(newString)


cumle = """
#English: Hello World
#Turkce : {} {}
""".format("Merhaba","Dunya")
print(cumle)

karakterler = "abcdxfg"
for i in karakterler:
    print("Basilan karakterler: {}".format(i))

"""

degisken1 = "oguz"
degisken2 = "sak"
sayi = 13
#konumlari belirleme
#:> saga yasla :< sola yasla :^ ortala :s sadece string bas :d sayilari bas :b ikili karsilik
ifade1 = "|{:d}|".format(sayi)
ifade2 = "{} {}".format(degisken2,degisken1)
print(ifade1)
print(ifade2)

