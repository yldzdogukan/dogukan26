 #1. Kullanıcıdan adını ve soyadını ayrı ayrı alıp, tam adını ekrana yazdıran program.
ad = input("Adınızı girin: ")
soyad = input("Soyadınızı girin: ")
tam_ad = ad + " " + soyad
print("Tam adınız:", tam_ad)

#2.İki sayının toplamı, farkı ve çarpımı
x = 30
y = 10
print(x + y)
print(x - y)
print(x * y)

#3.Kullanıcının yaşını alıp, 18 yaşından büyük olup olmadığını True/False olarak gösteren program
yas = input("lütfen yaasınızı girin")
sonuç = int(yas)<18
print(sonuç)

#4.Dikdörtgenin alanını ve çevresini hesaplayan program
kisa_kenar = float(input("28: "))
uzun_kenar = float(input("68: "))
alan = kisa_kenar * uzun_kenar
cevre = 2 * (kisa_kenar + uzun_kenar)
print("Alan:", alan)
print("Çevre:", cevre)

#5. Girilen bir sayının pozitif olup olmadığını kontrol eden program.
sayi = float(input("24: "))
pozitif_mi = 10 > 0
print("Sayı pozitif mi?", pozitif_mi)

#6.Kullanıcıdan bir kelime alıp kelimenin ilk 3 harfini ve son 2 harfini yazdıran program.
x = "dogukan"
y = "dogukan"
print(x[0:3])
print(y[-2:])

#7.İki sayının ortalamasını hesaplayıp, sonucu ondalıklı sayı olarak gösteren program.
sayi1 = int(input("75"))
sayi2 = int(input("15"))
sayi_1 = sayi1 * 0.4
sayi_2 = sayi2 * 0.6
ortalama = sayi_1 + sayi_2
print(ortalama)

#8.Kullanıcının girdiği iki sayının her ikisinin de çift sayı olup olmadığını kontrol eden program
sayi1 = int(input("1. 44: "))
sayi2 = int(input("2. 22: "))
sonuç = (sayi1 % 2 == 0) and (sayi2 % 2 == 0)
print("Her iki sayı da çift mi?", sonuç)

#9.Girilen bir metnin uzunluğunu ve büyük harfe çevrilmiş halini ekrana yazdıran program
metin = input("merhaba arkadaşlar ben dogukan: ")
uzunluk = len(metin)
buyuk_harf = metin.upper()
print("Metnin uzunluğu:", uzunluk)
print("Büyük harf hali:", buyuk_harf)

#10.Dairenin alanını hesaplayan program (pi = 3.14)
pi = 3.14
yaricap = float(input("60: "))
alan = pi * (yaricap ** 2)
print("Dairenin alanı:", alan)

#11.İki sayının eşit olup olmadığını ve birincinin ikinciden büyük olup olmadığını gösteren program
sayi1 = int(input("1.30: "))
sayi2 = int(input("2. 30: "))
esit_mi = (sayi1 == sayi2)
birinci_buyuk_mu = (sayi1 > sayi2)
print("İki sayı eşit mi?", esit_mi)
print("Birinci sayı ikinciden büyük mü?", birinci_buyuk_mu)

#12.Bir sayının hem 3’e hem de 5’e tam bölünüp bölünmediğini kontrol eden program
sayi = int(input("Bir sayı girin: "))
bolunur_mu = (sayi % 4 == 0) and (sayi % 10== 0)

print("Sayı hem 4'e hem de 10'e tam bölünüyor mu?", bolunur_mu)
