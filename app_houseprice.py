import streamlit as st
import pandas as pd
import numpy as np
import pickle  # jika Anda memiliki model yang sudah dilatih
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Judul dan Deskripsi
def run():
    st.title("Aplikasi Prediksi Harga Rumah")
    st.write("""
    Aplikasi ini memprediksi **Harga Rumah** berdasarkan fitur input!
    """)

    # Input di sidebar (ganti dengan input yang sesuai untuk model Anda)
    st.sidebar.header('Fitur Input Pengguna')

    # Contoh input pengguna
    def user_input_features():
        # Anda bisa menambahkan lebih banyak input di sini sesuai dengan model Anda
        #Square_Footage, Num_Bedrooms, Num_Bathrooms, Year_Built, Lot_Size, Garage_Size, Neighborhood_Quality, House_Price
        squre_footage = st.sidebar.number_input('Ukuran Persegi (Square Footage)', min_value=0, max_value=10000, value=821)
        num_bedrooms = st.sidebar.number_input('Jumlah Kamar (Num Badrooms)', min_value=0, max_value=5, value=1)
        num_bathrooms = st.sidebar.number_input('Jumlah Kamar Mandi (Num Bathrooms)', min_value=0, max_value=5, value=1)
        year_built = st.sidebar.number_input('Tahun Dibangun (Year Built)', min_value=1800, max_value=2024, value=2001)
        lot_area = st.sidebar.number_input('Luas Tanah (Lot Area)', min_value=0.0, max_value=10000.0, value=1.81066688)
        garage_area = st.sidebar.number_input('Luas Garasi (Garage Area)', min_value=0, max_value=1500, value=0)
        overall_qual = st.sidebar.slider('Kualitas Keseluruhan (Overall Quality)', 1, 10, 7)
        
        data = {
            'Square Footage': squre_footage,
            'Num Badrooms': num_bedrooms,
            'Num Bathrooms': num_bathrooms,
            'Year Built': year_built,
            'Lot Area': lot_area,
            'Garage Area': garage_area,
            'Overall Quality': overall_qual
        }
        
        features = pd.DataFrame(data, index=[0])
        return features

    input_df = user_input_features()

    # Memuat data dan model (jika Anda memiliki model yang sudah dilatih)
    model = pickle.load(open('houseprice/regresi1.pkl', 'rb'))

    # Placeholder untuk memuat data (ganti dengan pemrosesan data yang sebenarnya)
    data = pd.read_csv('houseprice/house_price_regression_dataset.csv')



    # Menampilkan input pengguna
    st.subheader('Fitur Input Pengguna')
    st.write(input_df)

    # Prediksi
    prediction = model.predict(input_df)
    st.subheader('Harga Rumah yang Diprediksi')
    st.write(prediction[0])


