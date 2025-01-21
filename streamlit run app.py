
import streamlit as st
import pandas as pd



def tampilkan_menu_pengguna():
  print("\n--- Menu Pengguna ---")
  print("1. Lihat Menu")
  print("2. Pesan Makanan")
  print("3. Lihat Riwayat Pesanan")
  print("4. Keluar")

def tampilkan_menu_admin():
  print("\n--- Menu Admin ---")
  print("1. Tambah Menu")
  print("2. Edit Menu")
  print("3. Hapus Menu")
  print("4. Lihat Pesanan")
  print("5. Keluar")

def main():
  print("Selamat datang di Aplikasi Katering!")

  while True:
    print("\nSilakan pilih tipe pengguna:")
    print("1. Pengguna")
    print("2. Admin")
    print("3. Keluar")

    pilihan_tipe = input("Pilihan Anda: ")

    if pilihan_tipe == "1":
      tampilkan_menu_pengguna()
      pilihan_menu = input("Pilihan Anda: ")
      # Tambahkan logika untuk setiap pilihan menu pengguna di sini
    elif pilihan_tipe == "2":
      username = input("Username: admin ")
      password = input("Password: admin123 ")
      # Tambahkan logika untuk verifikasi username dan password di sini
      # Jika verifikasi berhasil, tampilkan menu admin
      if username == "admin" and password == "password":  # Ganti dengan username dan password yang sesuai
        tampilkan_menu_admin()
        pilihan_menu = input("Pilihan Anda: ")
        # Tambahkan logika untuk setiap pilihan menu admin di sini
      else:
        print("Username atau password salah!")
    elif pilihan_tipe == "3":
      print("Terima kasih telah menggunakan aplikasi kami!")
      break
    else:
      print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
  main()