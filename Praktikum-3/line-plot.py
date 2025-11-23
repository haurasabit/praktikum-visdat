import streamlit as st
import matplotlib.pyplot as plt 

#buat data sample
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
product_a_sales = [10,20,15,25,30,45,40,50,60,55,65,70]
product_b_sales = [5,15,20,25,30,35,40,45,50,55,60,65]

#Layout streamlit
st.title("Visualisasi Penjualan Produk")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("Pilih Tipe visualisasi", ("Single Line Plot",
                                                         "Multiple & Customizeations",
                                                         "Jenis Garis untuk Menunjukkan Tren",
                                                         "Subplot"))

#Identitas Kelompok
st.caption("Praktikum 3 - Matplotlib Line Chart")
st.write("Kelompok: 10")
st.markdown("""
    - HAURA TSABITAH (110222242)
    - AHMAD AL-FAQIH ASASI (110222190)
    - MUHAMMAD REZA PAHLEVI H (110122110)
            """)

#Single Line Plot
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months,product_a_sales,label="Produk A")
    ax.set_title('Penjualan Produk A per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    st.pyplot(fig)
    
#Multiple Line Plot & Customizations
def customizations_plot():
    fig, ax = plt.subplots()
    ax.plot(months,product_a_sales,label="Produk A", color="blue", linestyle='--', marker='o')
    ax.plot(months,product_b_sales,label="Produk B", color="red", linestyle='-', marker='x')
    
    ax.set_title('Penjualan Produk A & B per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
    
#Data sample tambahan
product_c_sales = [20,30,25,35,40,45,50,52,56,70,30,30]
product_d_sales = [15,20,18,22,30,44,30,60,55,20,40,35]
def tren_line_plot():
    fig, axs = plt.subplots()
    axs.plot(months,product_c_sales,label="Produk C", color="yellow", linestyle='-')
    axs.plot(months,product_d_sales,label="Produk D", color="green", linestyle=':')
    axs.set_title('Penjualan Produk per Bulan')
    axs.set_xlabel('Bulan')
    axs.set_ylabel('Penjualan')
    axs.legend()
    axs.grid(True)
    st.pyplot(fig)

#Subplot
def subplots():
    fig, axs = plt.subplots(2,1, figsize=(10,8))
    
    #plot pertama untuk produk c
    axs[0].plot(months,product_c_sales,label='Product C', linestyle='-', color='green', marker='d')
    axs[0].set_title('Penjualan Produk C per Bulan')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Penjualan')
    axs[0].legend()
    axs[0].grid(True)

    #plot pertama untuk produk d
    axs[1].plot(months,product_d_sales,label='Product D', linestyle='-', color='purple', marker='s')
    axs[1].set_title('Penjualan Produk D per Bulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Penjualan')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    st.pyplot(fig)

#Logika untuk menampilkan visualisasi
if option == "Single Line Plot":
    line_plot()
elif option == "Multiple & Customizeations":
    customizations_plot()
elif option == "Jenis Garis untuk Menunjukkan Tren":
    tren_line_plot()
elif option == "Subplot":
    subplots()

    