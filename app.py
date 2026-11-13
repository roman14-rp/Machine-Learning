import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")
kolom = joblib.load("kolom.pkl")

st.title("Prediksi Kelulusan Siswa")
st.write("Isi data siswa, lalu klik tombol Prediksi.")

studytime = st.selectbox("Lama belajar mingguan (1 = <2 jam, 4 = >10 jam)", [1, 2, 3, 4])
failures = st.number_input("Jumlah kegagalan sebelumnya", 0, 3, 0)
absences = st.number_input("Jumlah absensi", 0, 93, 5)
higher = st.selectbox("Ingin lanjut kuliah?", ["yes", "no"])
Medu = st.selectbox("Pendidikan ibu (0-4)", [0, 1, 2, 3, 4], index=2)

if st.button("Prediksi"):
    # Mulai dari semua kolom bernilai 0, lalu isi yang diinput
    data = pd.DataFrame([[0] * len(kolom)], columns=kolom)
    data["studytime"] = studytime
    data["failures"] = failures
    data["absences"] = absences
    data["Medu"] = Medu
    if "higher_yes" in data.columns:
        data["higher_yes"] = 1 if higher == "yes" else 0

    hasil = model.predict(data)[0]
    if hasil == 1:
        st.success("Prediksi: LULUS")
    else:
        st.error("Prediksi: TIDAK LULUS")