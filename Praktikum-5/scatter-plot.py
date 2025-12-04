import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd 

st.title("Scatter Plot Chart")
st.write("Kelompok: 10")
st.markdown("""
    - HAURA TSABITAH (110222242)
    - AHMAD AL-FAQIH ASASI (110222190)
    - MUHAMMAD REZA PAHLEVI H (110122110)
            """)

#dataset utama
suhu = [20,21,22,25,26,26,27,30,31,35]
penjualan = [50,60,70,80,90,100,105,110,115,120]

#dataset tambahan (data penjualan)
penjualan_weekdays = [50,60,70,80,90,100,105,110,115,120]
penjualan_weekends = [150,155,160,165,170,175,180,185,190,195]

#data untuk analisis
data = {
    'Suhu': [20,21,22,25,26,26,27,30,31,35],
    'penjualan_coklat': [12,16,18,20,22,24,26,28,30,32],
    'penjualan_vanila': [5,7,9,11,13,15,17,19,21,23],
    'penjualan_stroberi': [5,10,15,20,25,30,35,40,45,50],
    'kelembapan': [70,75,80,85,90,95,100,105,110,115]
}

#konfersi ke data
df = pd.DataFrame(data)

#Menu di Sidebar
option = st.sidebar.selectbox(
    "Pilih contoh Scatter Plot",
    (
        "Basic Scatter Plot",
        "Kustomisasi Scatter Plot",
        "Multiple Scatter Plot",
        "Analisis Scatter Plot"
    )
)

# 1 BASIC SCATTER PLOT
def basic_scatter():
    st.subheader("1. Basic Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan)
    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    st.pyplot(fig)

# 2 KUSTOMISASI SCATTER PLOT
def custom_scatter():
    st.subheader("2. Kustomisasi Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan, color='violet', s=100, edgecolors='black', alpha=0.7)
    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    ax.grid(True)
    st.pyplot(fig)

# 3 MULTIPLE SCATTER PLOT
def multiple_scatter():
    st.subheader("3. Multiple Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan_weekdays, color='blue', label='Hari Kerja', s=8)
    ax.scatter(suhu, penjualan_weekends, color='red', label='Hari Libur', s=8)
    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    ax.grid(True)
    st.pyplot(fig)

# 4 ANALISIS SCATTER PLOT
def scatter_3_var():
    st.subheader("4. Analisis 3 Variabel")
    
    #opsi jenis eskrim
    jenis_eskrim = st.selectbox('Pilih Jenis Es Krim', ['coklat','vanila','stroberi'])
    
    #logika untuk opsi jenis eskrim berdasarkan pilihan
    if jenis_eskrim == 'coklat':
        penjualan = df['penjualan_coklat']
    elif jenis_eskrim == 'vanila':
        penjualan = df['penjualan_vanila']
    else:
        penjualan = df['penjualan_stroberi']
        
    st.subheader("Data Penjualan & Suhu")
    st.dataframe(df)

    #scatter plot
    fig,ax = plt.subplots()
    scatter = ax.scatter(df['Suhu'], penjualan, c=df['kelembapan'], s=100, cmap='coolwarm', alpha=0.7)

    #styling
    ax.set_title(f'Hubungan Penjualan {jenis_eskrim} vs Suhu, dan Kelembapan')
    ax.set_xlabel('suhu')
    ax.set_ylabel(f'Penjualan Es Krim {jenis_eskrim}')
    fig.colorbar(scatter,label='kelembapan(%)')

    st.pyplot(fig)

    #ringkasan hubungan
    st.subheader('Analisis Hubungan')
    st.write(f'Grafik menunjukkan hubungan antara suhu, kelembapan, dan penjualan eksrim jenis **{jenis_eskrim}**')

#routing berdasarkan menu sidebar
if option == "Basic Scatter Plot":
    basic_scatter()
elif option == "Kustomisasi Scatter Plot":
    custom_scatter()
elif option == "Multiple Scatter Plot":
    multiple_scatter()
elif option == "Analisis Scatter Plot":
    scatter_3_var()
