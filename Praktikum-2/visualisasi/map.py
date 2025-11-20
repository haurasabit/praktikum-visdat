import streamlit as st 
import pandas as pd 
import numpy as np 

st.title("Map")
#nama + kelompok
st.write("Kelompok: 10")
st.markdown("""
    - HAURA TSABITAH (110222242)
    - AHMAD AL-FAQIH ASASI (110222190)
    - MUHAMMAD REZA PAHLEVI H (110122110)
            """)

df = pd.DataFrame(
    np.random.randn(50,2)/[10/10] + [15.4589, 75.0078],
    columns=["latitude", "longitude"]
)
st.map(df)

