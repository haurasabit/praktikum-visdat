import streamlit as st 
import pandas as pd 
import numpy as np 

st.title("Area Chart")
#nama + kelompok
st.write("Kelompok: 10")
st.markdown("""
    - HAURA TSABITAH (110222242)
    - AHMAD AL-FAQIH ASASI (110222190)
    - MUHAMMAD REZA PAHLEVI H (110122110)
            """)

df = pd.DataFrame(
    np.random.randn(40,4),
    columns=["C1", "C2", "C3", "C4"]
)
st.area_chart(df)

