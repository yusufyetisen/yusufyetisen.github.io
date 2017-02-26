#Uludağ Üniversitesi not hesaplama
a=int(input("Vize Notu Giriniz:"))
if a>100 or a<0:
    print("0 ile 100 arasında bir değer giriniz.")
    exit()
b=int(input("Final Notu Giriniz:"))
if b>100 or b<0:
    print("0 ile 100 arasında bir değer giriniz.")
    exit()
abo=((a*40/100)+(b*60/100)) #Vize ve final notunun yüzde kaçının alıp toplanacağını hesapladım ve buna değer verdim.
if abo>=50 and b>50:
    print("Geçtiniz.")
    exit()
else: #eğer final geçme notunu(50) geçemediyse ve vize finalin yüzde toplamı 50'yi geçmiyorsa büt notu isteyecek.
    bt = int(input("Büt Notu Giriniz:"))
    bs = ((a * 40 / 100) + (bt * 60 / 100))
if bs>=50:
    print("Büt ile Geçtiniz")
    exit()
else:
    print("Geçemediniz.")


