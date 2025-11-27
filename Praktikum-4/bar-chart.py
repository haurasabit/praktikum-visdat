import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd 

st.title("Bar Chart")
st.write("Kelompok: 10")
st.markdown("""
    - HAURA TSABITAH (110222242)
    - AHMAD AL-FAQIH ASASI (110222190)
    - MUHAMMAD REZA PAHLEVI H (110122110)
            """)

#sample data
data = {
    'Jurusan': ['Teknik Informatika', 'Sistem Informasi', 'Ilmu Komputer', 'Data Science'],
    'Jumlah Mahasiswa': [120,100,105,95]
}

df = pd.DataFrame(data)

#streamlit bar chart
st.title("Basic Bar Chart - Jumlah Mahasiswa per Jurusan")
st.bar_chart(df.set_index('Jurusan'))

st.title("Basic Bar Chart Menggunakan Matplotlib")
fig, ax = plt.subplots()
ax.bar(df['Jurusan'], data["Jumlah Mahasiswa"], color='pink')
ax.set_title('Jumlah Mahasiswa per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')

st.pyplot(fig)

#kustomisasi matplotlib bar chart
st.title("Kustomisasi Bar Chart")
fig, ax = plt.subplots()
colors = ['blue', 'green', 'orange', 'red']
bars = ax.bar(data['Jurusan'], data['Jumlah Mahasiswa'], color=colors)
ax.bar(df['Jurusan'], data["Jumlah Mahasiswa"], color=colors)
ax.set_title('Jumlah Mahasiswa per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')

for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
            str(bar.get_height()), ha = 'center')
    
st.pyplot(fig)

#multiple bar chart
st.title("Multiple Bar Chart")

#data tambahan
data_2023 = [120,108,100,97]
data_2024 = [99,110,125,125]

x = range(len(data['Jurusan']))
width = 0.4

fig,ax = plt.subplots()
ax.bar(x, data_2023, width=width, label='2023', color='lime')
ax.bar([p + width for p in x], data_2024, width=width, label='2024', color='orange')

ax.set_title('Jumlah Mahasiswa per Jurusan (2023 vs 2024)')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')
ax.set_xticks([p + width / 2 for p in x])
ax.set_xticklabels(data['Jurusan'])
ax.legend()

st.pyplot(fig)