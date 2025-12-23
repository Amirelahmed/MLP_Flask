# 🏡 BLG407 Çoklu Doğrusal Regresyon (MLR) ve Flask Uygulaması

Bu proje, **BLG407 Makine Öğrenmesi** dersi kapsamında geliştirilmiş olup, ev fiyatlarını tahmin etmek için optimize edilmiş bir **Çoklu Doğrusal Regresyon (MLR)** modeli kullanır ve bu modeli modern bir **Flask** web arayüzü ile sunar.

---

## 🎯 Proje Başarısı ve Metodoloji Özeti

### 1. Veri Seti Geliştirme (Mühendislik Katkısı)

Projenin temel gücü, kullanılan veri setinin optimizasyonudur. Orijinal 4 temel özelliğe ek olarak, tahmin gücünü artırmak için **tarafımdan 3 yeni özellik** eklenmiştir.

| Kriter | Özellikler | Açıklama |
| :--- | :--- | :--- |
| **Temel Veri (4 Özellik)** | `area`, `rooms`, `age`, `city` | Veri setinin başlangıç yapısı. |
| **Tarafımdan Eklenen (3 Yeni Özellik)** | `floor_level` (Kat Seviyesi), `is_furnished` (Eşyalı), `has_balcony` (Balkon). | Bu özellikler tahmin performansını önemli ölçüde artırmıştır. |
| **Model Girdisi** | Toplam **7 Optimize Edilmiş İstatistiksel Özellik**. | |

### 2. Model Optimizasyonu ve Sonuç

| Metodoloji Adımı | Açıklama |
| :--- | :--- |
| **Ön İşleme (Pipeline)** | Veri tutarlılığı ve sızıntı önleme için **Pipeline** kullanıldı. Sayısal veriler **StandardScaler** , kategorik veriler **One-Hot Encoding** ile dönüştürüldü. |
| **Özellik Seçimi** | Modelin sadece istatistiksel olarak anlamlı değişkenleri kullanması için **Backward Elimination** yöntemi uygulandı (p-value < 0.05). |
| **Başarım Metriği ($R^2$ Score)** | Model, test setinde **$R^2 = 0.8425$** skoruna ulaşmıştır. Bu, fiyat varyasyonunun %84.25'ini başarıyla açıkladığı anlamına gelir. |

---

## 📁 Proje Yapısı

| Dosya / Klasör | Açıklama |
| :--- | :--- |
| `app.py` | Eğitilmiş `model.pkl` dosyasını yükleyen ve kullanıcıdan 7 girdiyi alıp tahmini yapan **Flask Backend Uygulaması**. |
| `templates/` | `index.html` (Giriş Formu) ve `result.html` (Sonuç Ekranı) HTML arayüz dosyaları. |
| `model.pkl` | Pipeline adımları dahil, **eğitilmiş regresyon modelinin tamamı**. |
| `house_prices_dataset.csv` | **Tarafımdan 3 yeni özellikle geliştirilmiş** ham veri seti. |
| `MLP_Flask.ipynb` | Colab ortamında **veri ön işleme, Backward Elimination ve model eğitimi** adımlarının ayrıntılı olarak gösterildiği eğitim dosyası. |

---

## 📸 Uygulama Ekran Görüntüleri

### 🟦 Giriş Formu (7 Özellik Girişi)
Kullanıcıdan **7 kritik özellik** (alan, oda, yaş, şehir, kat, eşya, balkon) bilgileri alınır.

![Giriş Ekranı](https://raw.githubusercontent.com/Amirelahmed/MLP_Flask/main/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C%202025-11-26%20164446.png)

---

### 🟩 Tahmin Sonucu
Model tarafından hesaplanan tahmini fiyat kullanıcıya gösterilir.

![Sonuç Ekranı](https://raw.githubusercontent.com/Amirelahmed/MLP_Flask/main/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C%202025-11-26%20164458.png)

---

## 🚀 Uygulamayı Çalıştırma

### 1️⃣ Gerekli Kütüphaneler
```bash
pip install flask pandas scikit-learn numpy statsmodels
```
### 2️⃣ Uygulamayı Başlat
```bash
python app.py
```
### 3️⃣ Tarayıcıdan Açın
```bash
[http://127.0.0.1:5001](http://127.0.0.1:5001)
```

🎉 **Uygulama artık hazır!**

---

## 👨‍💻 Geliştirici Bilgileri

| Bilgi | İçerik |
|-------|--------|
| **Ad Soyad** | Amir Elahmed |
| **Ders** | BLG407 – Makine Öğrenmesi |
| **Öğretim Üyesi** | Doç. Dr. Sinan Uğuz |

---


