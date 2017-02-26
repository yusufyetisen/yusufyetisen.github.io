#Uludağ Üniversitesi not hesaplama
a=int(input("Vize Notu Giriniz:"))
print("Final Notunuz 50'den aşağı ise büte kalacaksınız.")
b=int(input("Final Notu Giriniz:"))
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


