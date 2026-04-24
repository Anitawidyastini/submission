import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Judul dashboard
st.title("Dashboard Analisis Penyewaan Sepeda")

st.write("Dashboard ini menampilkan analisis penyewaan sepeda berdasarkan cuaca, jam, dan jenis hari.")

# Load data
base_path = os.path.dirname(__file__)

main_data_path = os.path.join(base_path, "main_data.csv")
data1_path = os.path.abspath(os.path.join(base_path, "../data/data_1.csv"))
data2_path = os.path.abspath(os.path.join(base_path, "../data/data_2.csv"))

df = pd.read_csv(main_data_path)

#Tahun
df_2011 = df[df['year'] == 2011]
df_2012 = df[df['year'] == 2012]

# Tampilkan data
st.subheader("Akses Dataset")

st.write("Dataset yang Digunakan Dalam Analisis:")

# Download clean data
with open(main_data_path, "rb") as file:
    st.download_button(
        label="Download Data Clean",
        data=file,
        file_name="main_data.csv",
        mime="text/csv"
    )

# Download data 1/day.df
with open(data1_path, "rb") as file:
    st.download_button(
        label="Download Raw Day.df",
        data=file,
        file_name="data_1.csv",
        mime="text/csv"
    )

# Download raw data 2
with open(data2_path, "rb") as file:
    st.download_button(
        label="Download Raw Hour.df",
        data=file,
        file_name="data_2.csv",
        mime="text/csv"
    )

st.write("---")

# ========================
# 📊 GRAFIK 1: CUACA (2011)
# ========================
weather_analysis = df_2011.groupby('weathersit')['daily_rentals'].mean().sort_values(ascending=False)

st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca Tahun 2011")

fig, ax = plt.subplots()
sns.barplot(x=weather_analysis.index, y=weather_analysis.values, ax=ax)

ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Rata-rata Penyewaan")
ax.set_title("Pengaruh Cuaca terhadap Penyewaan Sepeda (2011)")

st.pyplot(fig)

# ========================
# 📊 GRAFIK 2: JAM (2012)
# ========================
hourly_analysis = df_2012.groupby('hr')['hourly_rentals'].mean()

st.subheader("Pola Penyewaan Sepeda Berdasarkan Jam Tahun 2012")

fig2, ax2 = plt.subplots()
hourly_analysis.plot(ax=ax2)

ax2.set_xlabel("Jam")
ax2.set_ylabel("Rata-rata Penyewaan")
ax2.set_title("Puncak Penyewaan Sepeda per Jam (2012)")

st.pyplot(fig2)

# ========================
# 📊 GRAFIK 3: WORKINGDAY (2011)
# ========================
workingday_analysis = df_2011.groupby('workingday')['daily_rentals'].mean()

st.subheader("Perbandingan Penyewaan Sepeda: Hari Kerja vs Akhir Pekan Tahun 2011")

fig3, ax3 = plt.subplots()
sns.barplot(x=workingday_analysis.index, y=workingday_analysis.values, ax=ax3)

ax3.set_xlabel("Kategori Hari (0 = Weekend, 1 = Hari Kerja)")
ax3.set_ylabel("Rata-rata Penyewaan")
ax3.set_title("Perbandingan Penyewaan Sepeda (2011)")

st.pyplot(fig3)