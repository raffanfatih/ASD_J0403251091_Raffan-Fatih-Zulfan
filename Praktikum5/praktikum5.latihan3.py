# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================

def cari_maks(data, index=0):
    # Base case
    if index == len(data) - 1: # jika indeks sudah mencapai elemen terakhir dalam list, maka tidak ada lagi angka untuk dibandingkan
        return data[index] # mengembalikan nilai terakhir untuk menjadi perbandingan dengan nilai-nilai yang lain
    # Recursive case
    maks_sisa = cari_maks(data, index + 1) # fungsi memanggil dirinya sendiri untuk melihat elemen berikutnya (index + 1), program akan terus maju sampai ke ujung list sebelum mulai membandingkan
    if data[index] > maks_sisa: # membandingkan nilai naksimal (maks_sisa) dengan angka pada indeks saat ini data[indeks]
        return data[index] # jika angka saat ini lebih besar, maka angka ini menjadi nilai maksimum baru untuk digunakan ke bagian pengulangan berikutnya
    else:
        return maks_sisa # jika angka saat ini lebih kecil atau sama, maka nilai maksimum dari sisa list tetap dipertahankan
    
angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))

# alur keja 
# Fungsi ini bekerja dari belakang ke depan setelah mencapai ujung list.
# Mencapai Ujung: Fungsi masuk terus sampai index ke-4 (angka 5). Karena ini elemen terakhir, ia akan mengembalikan 5.
# 1. Bandingkan 9 & 5: Kembali ke indeks ke-3 (angka 9). Apakah 9>5? Ya. Maka kembalikan 9.
# 2. Bandingkan 2 & 9: Kembali ke indeks ke-2 (angka 2). Apakah 2>9? Tidak. Maka tetap kembalikan 9.
# 3. Bandingkan 7 & 9: Kembali ke indeks ke-1 (angka 7). Apakah 7>9? Tidak. Maka tetap kembalikan 9.
# 4. Bandingkan 3 & 9: Kembali ke indeks ke-0 (angka 3). Apakah 3>9? Tidak. Maka hasil akhirnya adalah 9.
