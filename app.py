from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Eğitilmiş modeli yükle
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        area = float(request.form["area"])
        rooms = float(request.form["rooms"])
        age = float(request.form["age"])
        city = request.form["city"]

        # Girdileri DataFrame'e çevir
        input_df = pd.DataFrame([[area, rooms, age, city]],
                                columns=["area", "rooms", "age", "city"])

        # Tahmin
        predicted_price = model.predict(input_df)[0]

        return render_template("result.html", result=int(predicted_price))
    except Exception as e:
        # Hata durumunda basit bir mesaj döndür
        return f"Hata oluştu: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)