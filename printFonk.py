# En temel çıktı üretme biçimi

print("Kod-Asistan sistemine hoş geldiniz!")

# Virgül (,) ile Bağımsız Argümanları Ayırarak Çıktı Üretme

tam_sayi = 100
ondalikli_sayi = 25.27
metin = "Yalova"
bool_deger = False
print(tam_sayi, metin, ondalikli_sayi, bool_deger)

# Artı (+) Operatörü ile String Birleştirme

ad = "Ali"
soyad = "Yaşar"
print(ad+soyad)

# f-String (Formatlı String) Teknolojisi

ogrenci_ad = "Fatih"
ogrenci_soyad = "Gider"
ogrenci_yas = 15
print(f"Öğrencini Adı: {ogrenci_ad}, soyadı: {ogrenci_soyad}, yaşı: {ogrenci_yas}")

# f-String (Formatlı String) Teknolojisi 2

ogrenci_ad = "Deniz"
ogrenci_soyad = "Sever"
ogrenci_yas = 13
print("Öğrencini Adı: {}, soyadı: {}, yaşı: {}".format(ogrenci_ad,ogrenci_soyad,ogrenci_yas))

# sep [Separator (Ayırıcı)]: Virgülle ayrılmış ifadelerin arasına hangi karakterin geleceğini belirler. Varsayılan değeri boşluktur (sep=" ").

print("Aksa","Mesleki","ve","Teknik","Anadolu","Lisesi")
print("Aksa","Mesleki","ve","Teknik","Anadolu","Lisesi",sep="*")
print("Aksa","Mesleki","ve","Teknik","Anadolu","Lisesi",sep="/")

# end [End (Bitiriş)]: Çıktı ekrana basıldıktan sonra satırın nasıl sonlanacağını belirler. Varsayılan değeri bir alt satıra geçme komutu olan yeni satır karakteridir (end="\n").

print("Aksa", end="\n\n")
print("Mesleki", end=" BAŞARILI")
print("ve", end="*")
print("Teknik")
print("Anadolu")
print("Lisesi")

