# Data mahasiswa disimpan dalam bentuk dictionary
mahasiswa = []

# Fungsi untuk menambah data
def tambah():
    print("\nTambah Data Mahasiswa")
    nama = input("Nama: ")
    nim = input("NIM: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
    mahasiswa.append({"Nama": nama, "NIM": nim, "Tugas": tugas, "UTS": uts, "UAS": uas, "Akhir": nilai_akhir})
    print(f"Data mahasiswa {nama} berhasil ditambahkan!\n")

# Fungsi untuk menampilkan data
def tampilkan():
    print("\nDaftar Nilai Mahasiswa")
    print("===================================================================")
    print("| No |     Nama      |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
    print("===================================================================")
    if not mahasiswa:
        print("|                          Tidak ada data                          |")
    else:
        for i, data in enumerate(mahasiswa, start=1):
            print(f"| {i:<2} | {data['Nama']:<12} | {data['NIM']:<9} | {data['Tugas']:<5} | {data['UTS']:<5} | {data['UAS']:<5} | {data['Akhir']:<6.2f} |")
    print("===================================================================")

# Fungsi untuk menghapus data berdasarkan nama
def hapus(nama):
    global mahasiswa
    mahasiswa = [data for data in mahasiswa if data['Nama'].lower() != nama.lower()]
    print(f"Data mahasiswa dengan nama '{nama}' telah dihapus.\n")

# Fungsi untuk mengubah data berdasarkan nama
def ubah(nama):
    for data in mahasiswa:
        if data['Nama'].lower() == nama.lower():
            print("\nData ditemukan. Masukkan data baru:")
            data['NIM'] = input("NIM: ")
            data['Tugas'] = float(input("Nilai Tugas: "))
            data['UTS'] = float(input("Nilai UTS: "))
            data['UAS'] = float(input("Nilai UAS: "))
            data['Akhir'] = (data['Tugas'] * 0.3) + (data['UTS'] * 0.35) + (data['UAS'] * 0.35)
            print(f"Data mahasiswa {nama} berhasil diperbarui!\n")
            return
    print(f"Data dengan nama '{nama}' tidak ditemukan.\n")

# Menu utama
while True:
    print("\nProgram Daftar Nilai Mahasiswa")
    print("==============================")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")
    pilihan = input("Pilih menu (1/2/3/4/5): ")
    
    if pilihan == '1':
        tambah()
    elif pilihan == '2':
        tampilkan()
    elif pilihan == '3':
        nama_hapus = input("Masukkan nama mahasiswa yang akan dihapus: ")
        hapus(nama_hapus)
    elif pilihan == '4':
        nama_ubah = input("Masukkan nama mahasiswa yang akan diubah: ")
        ubah(nama_ubah)
    elif pilihan == '5':
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
