# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama  : Raffan Fatih Zulfan
# NIM   : J0403251091
# Kelas : A2
# ==========================================================

# -------------------------------
# Konstanta nama file
# -------------------------------

nama_file = "stok_barang.txt"

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------

def baca_stok(nama_file): 
    """
    Membaca Stok Barang dari file.
    Format per baris: Kode Barang, Nama Barang, Jumlah Barang
    """

    stok_dict = {} #inisiasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #ambil data perbaris dan hilangkan new line
            kode, barang, jumlah = baris.split(",") #ambil data per item data
            stok_dict[kode] = {"barang" : barang, "jumlah" : int(jumlah)}
        return stok_dict

stock = baca_stok(nama_file)

# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------

def tampilkan_data(stok_dict):
    """
    Menampilkan semua barang di stok_dict.
    """

    print("\n======== Stok Barang ========")     #membuat header tabel
    print(f"{'Kode' : <7} | {'Barang' : <10} | {'Jumlah' :>3}")
    print("-" * 29) #membuat garis panjang secara otomatis

    #menampilkan isi data
    for kode in sorted(stok_dict.keys()):
        barang = stok_dict[kode]["barang"]
        jumlah = stok_dict[kode]["jumlah"]
        print(f"{kode:<7} | {barang:<10} | {int(jumlah):>6}")

# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------

def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode barang.
    """
    kode = input("Masukkan kode barang yang ingin dicari: ").strip().upper()
    
    if kode in stok_dict: #mencari barang berdasarkan kodenya
        barang = stok_dict[kode]["barang"]
        jumlah = stok_dict[kode]["jumlah"]

        print("\n===== Stok Barang Ditemukan =====") #tampilan yang akan muncul jika kode barang ditemukan
        print(f"Kode    : {kode}")
        print(f"Barang  : {barang}")
        print(f"Jumlah  : {jumlah}")
    else:
        print("Barang Tidak Ditemukan") #tampilan yang akan muncul jika kode barang tidak ditemukan

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------

def tambah_barang(stok_dict):
    """
    Menambah barang baru ke stok_dict.
    """
    kode = input("Masukkan kode barang baru: ").strip().upper()

    if kode in stok_dict: #mengecek jika kode barang sudah ada, maka user diminta memasukkan kode lain
        print("Kode barang sudah ada. Silahkan gunakan menu update stok.")
        return

    nama_barang = input("Masukkan nama barang: ").strip()

    try:
        jumlah = int(input("Masukkan jumlah awal stok: "))
        if jumlah < 0:
            print("Jumlah stok tidak boleh kurang dari nol.")
            return
        
    except ValueError:
        print("Jumlah harus berupa angka.")
        return

    #menambahkannya langsung ke dictionary dan simpan permanen di file stok_barang.txt
    stok_dict[kode] = {
        "barang": nama_barang,
        "jumlah": jumlah
    }
    
    simpan_stok(nama_file, stok_dict)
    print("Barang baru berhasil ditambahkan dan disimpan otomatis kedalam file.")

# -------------------------------
# Fungsi: Update stok barang
# -------------------------------

def update_stok(stok_dict):
    """
    Mengubah stok barang (tambah, kurangi, atau hapus).
    Menampilkan info barang terlebih dahulu.
    Stok tidak bisa negatif
    """

    kode = input("Masukkan kode barang: ").strip().upper()

    if kode not in stok_dict: #jika kode tidak ada dalam stok_dict maka kode ini akan berjalan
        print("Barang tidak ditemukan.")
        return
    
    #memunculkan data barang yang ingin kita update agar memudahkan user dalam melihat stoknya
    barang = stok_dict[kode]["barang"]
    stok_sekarang = stok_dict[kode]["jumlah"]

    print("\n===== DATA BARANG =====")
    print(f"Kode   : {kode}")
    print(f"Barang : {barang}")
    print(f"Stok   : {stok_sekarang}")
    
    #menu untuk pilihan update
    print("\nPilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")
    print("3. Hapus barang")

    pilihan = input("Masukkan pilihan (1/2/3): ").strip()

    #fungsi untuk menghapus barang
    if pilihan == "3":
        konfirmasi = input(f"Yakin ingin menghapus '{barang}'? (y/n): ").strip().lower()

        if konfirmasi == "y":
            del stok_dict[kode]
            print("Barang berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
        return
    
    #fungsi untuk menambahkan atau mengurangi stok
    try:
        jumlah = int(input("Masukkan jumlah: "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0.")
            return

        if pilihan == "1":
            stok_dict[kode]["jumlah"] += jumlah #fungsi untuk menambahkan stok
            print("Stok berhasil ditambahkan.")
            print(f"Stok sekarang: {stok_dict[kode]['jumlah']}")

        elif pilihan == "2":
            #jika user memasukkan angka lebih besar dari stok, maka stok akan negatif sehingga stok tidak akan berubah
            if stok_dict[kode]["jumlah"] < jumlah: 
                print("Stok tidak mencukupi. Update dibatalkan.")
            else:
                stok_dict[kode]["jumlah"] -= jumlah #fungsi untuk mengurangi stok
                print("Stok berhasil dikurangi.")
                print(f"Stok sekarang: {stok_dict[kode]['jumlah']}")

        else:
            print("Pilihan tidak valid.")

    except ValueError:
        print("Input jumlah harus berupa angka.")

# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------

def simpan_stok(nama_file, stok_dict):
    """
    Menyimpan seluruh data stok ke file teks.
    Format per baris: Kode Barang, Nama Barang, Jumlah Barang
    """

    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in sorted(stok_dict.keys()):
            barang = stok_dict[kode]["barang"]
            jumlah = stok_dict[kode]["jumlah"]
            file.write(f"{kode},{barang},{jumlah}\n") #menulis data stok dengan tambahan newline

# -------------------------------
# Program Utama
# -------------------------------

def main():
    # Membaca data dari file saat program mulai
    stock = baca_stok(nama_file)

    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            tampilkan_data(stock)
        elif pilihan == "2":
            cari_barang(stock)
        elif pilihan == "3":
            tambah_barang(stock)
        elif pilihan == "4":
            update_stok(stock)
        elif pilihan == "5":
            simpan_stok(nama_file, stock)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()