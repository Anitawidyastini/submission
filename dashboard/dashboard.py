import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul dashboard
st.title("Dashboard Analisis Penyewaan Sepeda")

st.write("Dashboard ini menampilkan analisis penyewaan sepeda berdasarkan cuaca, jam, dan jenis hari.")

# Load data
import os
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "main_data.csv")

with open(file_path, "rb") as file:
    df = pd.read_csv(file)

# Sidebar filter
st.sidebar.header("Filter Data")

year_option = st.sidebar.selectbox(
    "Pilih Tahun",
    sorted(df['year'].unique())
)

# Filter data
df_filtered = df[df['year'] == year_option]

# Tampilkan data
st.subheader("Akses Dataset")

st.write("Dataset yang Digunakan Dalam Analisis:")

# Download clean data
with open("main_data.csv", "rb") as file:
    st.download_button(
        label="Download Data Clean",
        data=file,
        file_name="main_data.csv",
        mime="text/csv"
    )

# Download data 1/day.df
with open("../data/data_1.csv", "rb") as file:
    st.download_button(
        label="Download Raw Day.df",
        data=file,
        file_name="data_1.csv",
        mime="text/csv"
    )

# Download raw data 2
with open("../data/data_2.csv", "rb") as file:
    st.download_button(
        label="Download Raw Hour.df",
        data=file,
        file_name="data_2.csv",
        mime="text/csv"
    )
st.write("---")


# ========================
# 📊 GRAFIK 1: CUACA
# ========================
weather_analysis = df_filtered.groupby('weathersit')['daily_rentals'].mean().sort_values(ascending=False)

st.subheader("Pengaruh Cuaca terhadap Penyewaan Sepeda")

fig, ax = plt.subplots()
sns.barplot(x=weather_analysis.index, y=weather_analysis.values, ax=ax)

ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Rata-rata Penyewaan")
ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Cuaca")

st.pyplot(fig)

# ========================
# 📊 GRAFIK 2: JAM
# ========================
hourly_analysis = df_filtered.groupby('hr')['hourly_rentals'].mean()

st.subheader("Pola Penyewaan Sepeda Berdasarkan Jam")

fig2, ax2 = plt.subplots()
hourly_analysis.plot(ax=ax2)

ax2.set_xlabel("Jam")
ax2.set_ylabel("Rata-rata Penyewaan")
ax2.set_title("Penyewaan Sepeda per Jam")

st.pyplot(fig2)

# ========================
# 📊 GRAFIK 3: WORKINGDAY
# ========================
workingday_analysis = df_filtered.groupby('workingday')['daily_rentals'].mean()

st.subheader("Perbandingan Penyewaan: Hari Kerja vs Akhir Pekan")

fig3, ax3 = plt.subplots()
sns.barplot(x=workingday_analysis.index, y=workingday_analysis.values, ax=ax3)

ax3.set_xlabel("Kategori Hari")
ax3.set_ylabel("Rata-rata Penyewaan")
ax3.set_title("Rata-rata Penyewaan Sepeda: Hari Kerja vs Akhir Pekan")

st.pyplot(fig3)