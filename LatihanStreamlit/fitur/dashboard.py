import streamlit as st

st.title("Halaman Dashboard")

# fungsi untuk menghitung dan menyimpan total nabung
def total():
    total_nabung = sum(t['Jumlah'] 
                       for t in st.session_state ["total_semua"] 
                       if t ['Tipe'] == 'Menabung')
    
    total_penarikan = sum(t['Jumlah'] 
                       for t in st.session_state ['total_semua'] 
                       if t ['Tipe'] == 'Penarikan')
    
    saldo = total_nabung - total_penarikan
    return total_nabung, total_penarikan, saldo

total_semua = st.session_state["total_semua"]
total_nabung, total_penarikan, saldo = total()

st.metric("Total Pemasukan", f"Rp {total_nabung:,}")
st.metric("Total Penarikan", f"Rp {total_penarikan:,}")
st.metric("Total Saldo", f"Rp {saldo:,}")