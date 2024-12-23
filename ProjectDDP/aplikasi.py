import streamlit as st

# Side Bar Directory
pengeluaran = st.Page("./fitur/pengeluaran.py", title="Pengeluaran")

pg = st.navigation(
    {
        "Menu Utama": [pengeluaran],
    }
)

if "jumlah" not in st.session_state:
    st.session_state["jumlah"] = []


#   Menjalankann aplikasi
pg.run()