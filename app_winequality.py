import streamlit as st
import pandas as pd
import numpy as np
import pickle  # jika Anda memiliki model yang sudah dilatih
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error , r2_score

# Judul dan Deskripsi
def run():
    st.title("Aplikasi Prediksi Kualitas Wine")
    st.write("""
    Aplikasi ini memprediksi **Kualitas Wine** berdasarkan fitur input!
    """)

    # Input di sidebar (ganti dengan input yang sesuai untuk model Anda)
    st.sidebar.header('Fitur Input Pengguna')

    # Contoh input pengguna
    def user_input_features():
        # Anda bisa menambahkan lebih banyak input di sini sesuai dengan model Anda
        #fixed acidity,volatile acidity,citric acid,residual sugar,chlorides,free sulfur dioxide,total sulfur dioxide,density,pH,sulphates,alcohol,quality
        fixed_acidity = st.sidebar.number_input('Keasaman Tetap (Fixed Acidity)', min_value=0.0, max_value=10000.0, value=6.8)
        volatile_acidity = st.sidebar.number_input('Keasaman Yang Mudah Menguap (Volatile Acidity)', min_value=0.0, max_value=10000.0, value=0.67)
        citric_acid = st.sidebar.number_input('Asam Sitrat (Citric Acid)', min_value=0.0, max_value=10000.0, value=0.02)
        residual_sugar= st.sidebar.number_input('Sisa Gula (Residual Sugar)', min_value=0.0, max_value=10000.0, value=1.8)
        chlorides= st.sidebar.number_input('Klorida (Chlorides)', min_value=0.0, max_value=10000.0, value=0.05)
        free_sulfur_dioxide= st.sidebar.number_input('Bebas Sulfur Dioksida (Free Sulfur Dioxide)', min_value=1.0, max_value=10000.0, value=5.0)
        total_sulfur_dioxide= st.sidebar.number_input('Total Sulfur Dioksida (Total Sulfur Dioxide)', min_value=1.0, max_value=10000.0, value=11.0)
        density= st.sidebar.number_input('Kepadatan (Density)', min_value=0.0, max_value=10000.0, value=0.9962)
        pH= st.sidebar.number_input('Potensi Hidrogen (pH)', min_value=0.0, max_value=10000.0, value=3.48)
        sulphates= st.sidebar.number_input('Sulfat (Sulphates)', min_value=0.0, max_value=10000.0, value=0.52)
        alcohol= st.sidebar.number_input('Alkohol (Alcohol)', min_value=0.0, max_value=10000.0, value=9.5)

        
        data = {
            'Fixed Acidity':fixed_acidity,
            'Volatile Acidity':volatile_acidity,
            'Citric Acid': citric_acid,
            'Residual Sugar':residual_sugar,
            'Chlorides': chlorides,
            'Free Sulfur Dioxide': free_sulfur_dioxide,
            'Total Sulfur Dioxide': total_sulfur_dioxide,
            'Density': density,
            'pH': pH,
            'Sulphates': sulphates,
            'Alcohol': alcohol
        }
        
        features = pd.DataFrame(data, index=[0])
        return features

    input_df = user_input_features()

    # Memuat data dan model (jika Anda memiliki model yang sudah dilatih)
    model = pickle.load(open('redwine/regresiwine.pkl', 'rb'))

    # Placeholder untuk memuat data (ganti dengan pemrosesan data yang sebenarnya)
    data = pd.read_csv('redwine\winequality-red.csv')



    # Menampilkan input pengguna
    st.subheader('Fitur Input Pengguna')
    st.write(input_df)

    # Prediksi
    prediction = model.predict(input_df)
    st.subheader('Kulaitas Wine yang Diprediksi')
    st.write(prediction[0])

