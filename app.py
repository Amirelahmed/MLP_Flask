from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Eğitilmiş modeli yükle
try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    print("HATA: model.pkl dosyası bulunamadı. Lütfen MLP_Flask notebook'u çalıştırdığınızdan emin olun.")
    model = None

@app.route("/")
def home():
    # Şehir listesi, index.html'e gönderilir
    cities = ['Istanbul', 'Ankara', 'Izmir', 'Bursa', 'Antalya', 'Adana', 'Konya']
    # index.html dosyasını templates/ dizininden yükler
    return render_template("index.html", cities=cities)

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return "Model yüklenemedi. Lütfen sunucuyu kontrol edin.", 500
        
    try:
        # Formdan gelen verileri al (TÜM 7 ÖZELLİK)
        area = float(request.form["area"])
        rooms = float(request.form["rooms"])
        age = float(request.form["age"])
        city = request.form["city"]
        
        # YENİ EKLENEN ÖZELLİKLER
        is_furnished = int(request.form["is_furnished"])
        has_balcony = int(request.form["has_balcony"])
        floor_level = float(request.form["floor_level"])

        # Girdileri DataFrame'e çevir (Modelin beklediği format)
        input_df = pd.DataFrame([[area, rooms, age, city, is_furnished, has_balcony, floor_level]],
                                # YENİ SÜTUN BAŞLIKLARI
                                columns=["area", "rooms", "age", "city", "is_furnished", "has_balcony", "floor_level"])

        # Tahmin
        predicted_price = model.predict(input_df)[0]
        
        # Sonucu result.html şablonuna gönderir
        return render_template("result.html", result=int(predicted_price))
    except ValueError:
        return render_template("index.html", error="Lütfen tüm alanlara geçerli sayısal değerler giriniz."), 400
    except Exception as e:
        # Hata durumunda basit bir mesaj döndür
        return f"Tahmin sırasında bir hata oluştu: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)