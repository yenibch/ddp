import streamlit as st

st.title("Halaman Dashboard")

#Fungsi menghitung
def total():
    total_pengeluaran = sum(t["Jumlah"] 
                            for t in st.session_state ["jumlah"] 
                            if t["Tipe"] == "Pengeluaran")

    return f"Total Pengeluaran anda {total_pengeluaran}"

st.write(total())