# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================

def kombinasi(n, hasil=""):
    if len(hasil) == n: # fungsi memeriksa apakah panjang string hasil saat ini sudah sama dengan panjang target n (2)
        print(hasil)
        return
    kombinasi(n, hasil + "A") # fungsi memanggil dirinya sendiri dengan menambahkan huruf "A" ke string hasil, ini akan terus menelusuri cabang kiri sampai mencapai n, dalam kode ini n-nya adalah 2
    kombinasi(n, hasil + "B") # setelah cabang "A" selesai, fungsi akan menambahkan huruf "B"
kombinasi(2) # memanggil fungsi untuk mencari semua kombinasi dengan panjang 2 karakter

# bagaimana jumlah kombinasi yang dihasilkan?
# Di dalam kode Latihan 4, pada setiap langkah rekursi, fungsi bercabang menjadi 2 pilihan, yaitu menambahkan huruf "A" atau huruf "B".
# Oleh karena itu, rumus untuk menghitung total kombinasinya adalah: Total Kombinasi=(Jumlah Pilihan)^n
# Karena jumlah pilihannya ada 2 ("A" dan "B"), maka rumusnya menjadi 2^n 
