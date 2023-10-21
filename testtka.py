import numpy as np
esik_deger = 1
# Eğitilmiş modelin en iyi öğrenme hızı ve ağırlıkları
en_iyi_ogrenme_hizi = 0.01  # Örneğin, eğitim sonucundan gelen en iyi öğrenme hızını burada belirtin
en_iyi_agirliklar = np.array([0.27135628, 0.74601203])  # Öğrenilmiş ağırlıkları burada belirtin

# Test verilerini oluşturun (örnek olarak)
test_verileri = np.array([[1, 0], [0, 1], [1, 1], [0,0]])

# Test sonuçlarını saklamak için boş bir liste oluşturun
test_sonuclari = []

# Her bir test verisini modelde uygulayın ve sonuçları saklayın
for test_verisi in test_verileri:
    net = np.dot(test_verisi, en_iyi_agirliklar)
    tahmin = 1 if net > esik_deger else 0
    test_sonuclari.append(tahmin)

# Test sonuçlarını yazdırın
for i, sonuc in enumerate(test_sonuclari):
    print(f"Test Verisi {i + 1}: Tahmin = {sonuc}")