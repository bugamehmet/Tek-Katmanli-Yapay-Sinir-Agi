import numpy as np

# Eğitim verilerini ve beklenen çıkışları kullanıcıdan alın
X = []
y = []
egitim_veri_sayisi = int(input("Kaç eğitim verisi girmek istersiniz? "))
for i in range(egitim_veri_sayisi):
    girdi_degerleri = input(f"{i + 1}. Eğitim verisi için girdileri arada boşluk bırakarak girin (örn: 1 0): ")
    girdiler = girdi_degerleri.split()
    girdiler = [float(girdi) for girdi in girdiler]  # Girdileri ondalık sayılara dönüştürün
    X.append(girdiler)
    beklenen_cikis = float(input(f"{i + 1}. Eğitim verisi için beklenen çıkışı girin (0 veya 1): "))
    y.append(beklenen_cikis)

# Eşik değerini alın
esik_deger = float(input("Eşik değeri girin: "))

ogrenme_katsayilari = input("Öğrenme katsayılarını arada boşluk bırakarak girin (örn: 0.1 0.2 0.3): ")
ogrenme_katsayilari = [float(katsayi) for katsayi in ogrenme_katsayilari.split()]

# Maksimum iterasyon sayısını alın
max_iterasyon = int(input("Maksimum iterasyon sayısını girin: "))

# Sonuçları saklamak için bir veri yapısı oluşturun
sonuclar = []

for ogrenme_katsayisi in ogrenme_katsayilari:
    # Ağırlıkları rastgele başlatın
    w = np.random.rand(len(X[0]))

    # Perceptron öğrenme algoritması
    iterasyon = 0
    for iterasyon in range(max_iterasyon):
        hata_toplami = 0
        for i in range(len(X)):
            xi = np.array(X[i])
            yi = y[i]
            net = np.dot(xi, w)
            cikti = 1 if net > esik_deger else 0
            hata = yi - cikti
            w = w + ogrenme_katsayisi * hata * xi
            hata_toplami += abs(hata)
            print(f"Öğrenme Hızı: {ogrenme_katsayisi}, Iterasyon {iterasyon + 1}, Veri: {X[i]}, Gerçekleşen Çıkış: {xi}, Beklenen Çıkış: {yi}, Ağırlıklar: {w}")
        # Hata toplamı sıfırsa, erkenden çık
        if hata_toplami == 0:
            break
    # Eğitim sonucunu saklayın
    sonuclar.append((ogrenme_katsayisi, w, iterasyon + 1))

# En iyi sonucu bulun
en_iyi_sonuc = min(sonuclar, key=lambda x: x[2])
en_iyi_ogrenme_katsayisi, en_iyi_ağırlıklar, en_iyi_iterasyon = en_iyi_sonuc

# Eğitim sonucunu yazdırın
print(f"En iyi öğrenme hızı: {en_iyi_ogrenme_katsayisi}")
print(f"Eğitim sonrası ağırlıklar: {en_iyi_ağırlıklar}")
print(f"{en_iyi_iterasyon} iterasyon sonunda eğitim tamamlandı.")


