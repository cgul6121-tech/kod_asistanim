# Senaryo A: Virgül (,) ve Artı (+) Operatörlerinin Karşılaştırması

asistan_adi = "Kod Asistanı"
versiyon = 2

# Virgül: Otomatik tür dönüşümü ve otomatik boşluk bırakır.

print("Benim adım", asistan_adi, "Sistem versiyonum:", versiyon)

# Artı (+): Sadece stringleri yapışık bağlar.

karsilama = "Merhaba " + "Yazılımcı"
print(karsilama)

# print("Yaşınız: " + 18) -> TypeError fırlatacağı için bilerek yoruma alındı.

# Senaryo B: F-String (Formatlı String) Teknolojisi

kullanici = "Mustafa"
islem_adedi = 5
print(f"Hoş geldiniz {kullanici}. Bugün yapay zekâ ile {islem_adedi} kod denetlediniz.")

# Senaryo C: print() Fonksiyonunun Gizli Parametreleri (sep ve end)

# sep (Separator): Kelimeler arasına varsayılan boşluk yerine "-" koyar.

print("Siber", "Güvenlik", "Mühendisliği", sep="-")

# end (End): Varsayılan alt satıra geçme (\n) komutunu ezer, aynı satırda tutar.

print("Kod denetimi başladı...", end=" [BAŞARILI] ")
print("Sistem kararlı.")