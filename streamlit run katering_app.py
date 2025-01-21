import streamlit as st
import pandas as pd

# Menu Pengguna
def menu_pengguna():
    st.subheader("Menu Pengguna")
    option = st.selectbox("Pilih Menu", ["Lihat Menu Katering", "Pesan Makanan", "Keluar"])
    
    if option == "Lihat Menu Katering":
        st.write("Menu Katering: ")
        st.write("1. Nasi Goreng")
        st.write("2. Ayam Penyet")
        st.write("3. Sate")
    elif option == "Pesan Makanan":
        makanan = st.selectbox("Pilih makanan yang ingin dipesan", ["Nasi Goreng", "Ayam Penyet", "Sate"])
        st.write(f"Anda memesan: {makanan}")
    elif option == "Keluar":
        st.write("Terima kasih telah menggunakan layanan kami!")
        st.stop()

# Menu Admin
def menu_admin():
    st.subheader("Menu Admin")
    option = st.selectbox("Pilih Menu", ["Tambah Menu Makanan", "Lihat Pesanan", "Keluar"])
    
    if option == "Tambah Menu Makanan":
        makanan_baru = st.text_input("Masukkan nama makanan baru")
        if st.button("Tambah"):
            st.write(f"Menu makanan '{makanan_baru}' telah ditambahkan.")
    elif option == "Lihat Pesanan":
        # Contoh pesanan
        st.write("Pesanan Hari Ini:")
        st.write("1. Nasi Goreng - 2 Porsi")
        st.write("2. Sate - 1 Porsi")
    elif option == "Keluar":
        st.write("Keluar dari aplikasi.")
        st.stop()

# Fungsi Login Admin
def login_admin():
    st.subheader("Login Admin")
    email = st.text_input("Masukkan Email:")
    password = st.text_input("Masukkan Password:", type="password")
    
    if st.button("Login"):
        if email == "admin@example.com" and password == "admin123":
            st.success("Login berhasil!")
            menu_admin()
        else:
            st.error("Email atau password salah. Coba lagi.")

# Fungsi Utama
def main():
    st.title("Aplikasi Katering")
    
    # Pilih tipe pengguna
    tipe_user = st.selectbox("Pilih Tipe Pengguna", ["Pengguna", "Admin"])
    
    if tipe_user == "Pengguna":
        menu_pengguna()
    elif tipe_user == "Admin":
        login_admin()

if __name__ == "__main__":
    main()
