import streamlit as st

st.title("Halaman Penarikan")
st.image("image.jpeg", caption="ini gambar bank")
# Halaman Menabung
with st.form("Penarikan"):
    nama = st.text_input("Nama")
    jumlah = st.number_input("Jumlah (Rp.)", min_value=0)
    tanggal = st.date_input("Tanggal")
    waktu = st.time_input("Waktu")
    submit_button = st.form_submit_button(label="Penarikan")
    if submit_button:
        st.session_state["total_semua"].append({
            "Tipe" : "Penarikan",
            "Nama" : nama,
            "Jumlah" : jumlah
        })
        st.success("Anda Berhasil Menarik")
    else:
        st.error("Anda Gagal Melakukan Penarikan")