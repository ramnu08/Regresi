import streamlit as st
import app_houseprice
import app_winequality


# Sidebar untuk memilih tampilan
st.sidebar.title("Linear Regresion")
page = st.sidebar.selectbox("Pilih Program", ("House Price", "Wine Quality"))

# Menampilkan program yang dipilih
if page == "House Price":
    app_houseprice.run()
elif page == "Wine Quality":
    app_winequality.run()
