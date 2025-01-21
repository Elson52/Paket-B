import getpass

# Menu Pengguna
def menu_pengguna():
    print("\n--- Menu Pengguna ---")
    print("1. Lihat Menu Katering")
    print("2. Pesan Makanan")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")
    
    if pilihan == '1':
        print("\nMenu Katering: ")
        print("1. Nasi Goreng")
        print("2. Ayam Penyet")
        print("3. Sate")
    elif pilihan == '2':
        print("\nSilakan pilih makanan yang ingin dipesan.")
        # Implementasi pemesanan
    elif pilihan == '3':
        print("Terima kasih telah menggunakan layanan kami!")
        exit()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        menu_pengguna()

# Menu Admin
def menu_admin():
    print("\n--- Menu Admin ---")
    print("1. Tambah Menu Makanan")
    print("2. Lihat Pesanan")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")
    
    if pilihan == '1':
        print("\nTambah menu makanan baru.")
        # Implementasi tambah menu
    elif pilihan == '2':
        print("\nLihat daftar pesanan.")
        # Implementasi lihat pesanan
    elif pilihan == '3':
        print("Keluar dari aplikasi.")
        exit()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        menu_admin()

# Fungsi untuk login Admin
def login_admin():
    print("\n--- Login Admin ---")
    email = input("Masukkan email: ")
    password = getpass.getpass("Masukkan password: ")
    
    # Cek email dan password (misal email: admin@example.com, password: admin123)
    if email == "admin@example.com" and password == "admin123":
        print("Login berhasil.")
        menu_admin()
    else:
        print("Email atau password salah. Coba lagi.")
        login_admin()

# Fungsi utama
def main():
    print("--- Aplikasi Katering ---")
    print("Pilih tipe pengguna:")
    print("1. Pengguna")
    print("2. Admin")
    
    tipe_user = input("Pilih (1/2): ")
    
    if tipe_user == '1':
        menu_pengguna()
    elif tipe_user == '2':
        login_admin()
    else:
        print("Pilihan tidak valid. Silakan pilih 1 untuk Pengguna atau 2 untuk Admin.")
        main()

# Menjalankan program
if __name__ == "__main__":
    main()
