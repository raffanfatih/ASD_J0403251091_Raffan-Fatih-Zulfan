# ====================================
# Praktikum 2 = Konsep ADT dan File Handling (Studi Kasus)
# Latihan 1 = Membuat Fungsi Load Data
# ====================================

nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {} #inisiasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #ambil data perbaris dan hilangkan new line
            nim, nama, nilai = baris.split(",") #ambil data per item data
            data_dict[nim] = {"nama" : nama, "nilai" : int(nilai)} #masukkan dalam 
    return data_dict

buka_data = baca_data(nama_file)
# print("Jumlah data terbaca: ", len(buka_data)) #jumlah data yang di load

# ====================================
# Praktikum 2 = Konsep ADT dan File Handling (Studi Kasus)
# Latihan 2 = Membuat Fungsi Menampilkan Data
# ====================================

def tampilkan_data(data_dict):
    #membuat header tabel
    print("\n======== Daftar Mahasiswa ========")
    print(f"{'NIM' : <10} | {'Nama' : <12} | {'Nilai' :>5}")
    """
    untuk tampilan yang rapi, atur lebar kolom
    {'NIM' : <10} artinya nim rata kiri dengan lebar kolom <10
    {'Nama' : <12} artinya nama rata kiri dengan lebar kolom <12
    {'Nilai' :>5} artinya nilai rata kiri dengan lebar kolom >5
    """
    print("-" * 34) #membuat garis panjang secara otomatis

    #menampilkan isi data
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {int(nilai):>5}")

# tampilkan_data(buka_data) #memanggil fungsi untuk menampilkan data

# ====================================
# Praktikum 2 = Konsep ADT dan File Handling (Studi Kasus)
# Latihan 3 = Membuat Fungsi Mencari Data
# ====================================

#membuat fungsi untuk mencari data
def cari_data(data_dict):
    #mencari data berdasarkan nim sebagai key dictionary
    #membuat input untuk mencari nim yang diinginkan
    nim_cari = input("Masukkan NIM Mahasiswa: ").strip().capitalize()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("===== Data Mahasiswa Ditemukan =====")
        print(f"NIM     : {nim_cari}")
        print(f"Nama    : {nama}")
        print(f"Nilai   : {nilai}")
    else:
        print("Data Mahasiswa Tidak Ditemukan")

#memanggil fungsi mencari data
# cari_data(buka_data)

# ====================================
# Praktikum 2 = Konsep ADT dan File Handling (Studi Kasus)
# Latihan 4 = Membuat Fungsi Update Data
# ====================================

#membuat fungsi update data
def ubah_data(data_dict):

    #awali dengan mencari nim mahasiswa yang ingin diubah
    nim = input("Masukkan NIM Mahasiswa: ").strip().capitalize()

    if nim not in data_dict:
        print("NIM Tidak Ditemukan")
        return
    
    try:
        nilai_baru = int(input("Masukkan Nilai Baru (0-100): ").strip())
    except ValueError:
        print("ERRORR | Nilai Harus Berupa Angka")

    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai Harus Diantara 0-100") 

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#memanggil fungsi ubah data
# ubah_data(buka_data)

# ====================================
# Praktikum 2 = Konsep ADT dan File Handling (Studi Kasus)
# Latihan 5 = Membuat Fungsi Menyimpan Data pada File
# ====================================

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

# #memanggil fungsi simpan data 
# simpan_data(nama_file, buka_data)
    print("\nData Berhasil Disimpan ke File: ", nama_file)

# ====================================
# Praktikum 2 = Konsep ADT dan File Handling (Studi Kasus)
# Latihan 6 = Membuat Fungsi Menyimpan Data pada File
# ====================================

def main():
    #load data otomatis saat program dijalankan
    buka_data = baca_data(nama_file)

    while True:
        print("\n===== Menu Data Mahasiswa =====")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Simpan Data ke File")
        print("0. Keluar")

        pilihan = input("Pilih Menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            ubah_data(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
        elif pilihan == "0":
            print("Program Selesai")
            break
        else:
            print("Pilihan Tidak Valid, Coba Lagi")

main()