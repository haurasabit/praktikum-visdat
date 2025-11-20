import streamlit as st

st.title("Columns")
#nama + kelompok
st.write("Kelompok: 10")
st.markdown("""
    - HAURA TSABITAH (110222242)
    - AHMAD AL-FAQIH ASASI (110222190)
    - MUHAMMAD REZA PAHLEVI H (110122110)
            """)

col1,col2 = st.columns(2)

col1.write("ini adalah kolom pertama")
col1.image("")

col2.write("ini adalah kolom kedua")