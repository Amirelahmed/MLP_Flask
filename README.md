# MLP_Flask
"BLG407 Çoklu Doğrusal Regresyon ve Flask GUI Projesi"
# 🏡 MLP_Flask – Ev Fiyat Tahmin Uygulaması

Bu proje, **BLG407 Makine Öğrenmesi** dersi kapsamında geliştirilmiş olup,  
çoklu doğrusal regresyon modeli kullanarak **ev fiyatı tahmini** yapan bir Flask web uygulamasıdır.

Uygulama, kullanıcıdan alınan alan (m²), oda sayısı, evin yaşı ve şehir bilgisine göre fiyat tahmini yapar  
ve sonucu modern bir arayüz üzerinde gösterir.

---

## 📁 Proje Yapısı

Aşağıdaki tablo proje klasörlerinin ve önemli dosyaların açıklamasını içermektedir:

| Dosya / Klasör | Açıklama |
|----------------|----------|
| `app.py` | Flask backend uygulaması |
| `templates/` | HTML arayüz dosyaları |
| `model.pkl` | Eğitimli regresyon modeli |
| `house_prices_dataset.csv` | Kullanılan veri seti |
| `BLG407_Coklu_Dogrusal_Regresyon_ve_Flask.ipynb` | Colab eğitim dosyası |

---

## 🌟 Özellikler

- Modern ve neon tasarımlı kullanıcı arayüzü  
- Çoklu doğrusal regresyon ile fiyat tahmini  
- Flask tabanlı backend  
- Kullanıcı girişine göre gerçek zamanlı tahmin  
- Sonuç ekranı ve yeni tahmin oluşturma butonu  

---

## 📸 Uygulama Ekran Görüntüleri

### 🟦 Giriş Formu  
Kullanıcıdan **alan, oda sayısı, evin yaşı ve şehir** bilgileri alınır.

![Giriş Ekranı](https://raw.githubusercontent.com/Amirelahmed/MLP_Flask/main/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202025-11-26%20164446.png)

---

### 🟩 Tahmin Sonucu  
Model tarafından hesaplanan tahmini fiyat kullanıcıya gösterilir.  
Ayrıca **Yeni Bir Tahmin Yap** butonu ile ana sayfaya dönüş yapılabilir.

![Sonuç Ekranı](https://raw.githubusercontent.com/Amirelahmed/MLP_Flask/main/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202025-11-26%20164458.png)

---

## 🤖 Makine Öğrenmesi Modülü

Model, doğrusal regresyon (LinearRegression) algoritması ile eğitilmiştir.

| Özellik | Açıklama |
|---------|----------|
| **area** | Evin m² alanı |
| **rooms** | Oda sayısı |
| **age** | Evin yaşı |
| **city** | One-Hot Encoding ile işlenmiş şehir bilgisidir |
| **price** | Tahmin edilmesi gereken değer |

Model eğitimi `.ipynb` dosyasında ayrıntılı şekilde gösterilmiştir.

---

## 🚀 Uygulamayı Çalıştırma

### 1️⃣ Gerekli Kütüphaneler  
Aşağıdaki komut ile gerekli paketleri yükleyebilirsiniz:

```bash
pip install flask pandas scikit-learn

2️⃣ Uygulamayı Başlat

Aşağıdaki komut ile Flask sunucusunu başlatın:

python app.py

3️⃣ Tarayıcıdan Açın

Sunucu çalıştıktan sonra bu adresi tarayıcıya yazın:

http://127.0.0.1:5000


🎉 Uygulama artık hazır!

👨‍💻 Geliştirici Bilgileri
Bilgi	İçerik
Ad Soyad	Amir Elahmed
Ders	BLG407 – Makine Öğrenmesi
Proje	Çoklu Doğrusal Regresyon + Flask Web Uygulaması



