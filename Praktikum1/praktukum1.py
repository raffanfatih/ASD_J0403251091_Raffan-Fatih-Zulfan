# LD: 1
print("===== MEMBUKA FILE DALAM SATU STRING =====\n")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read() # mengambil & menyimpan data dalam satu variabel
print(isi_file)

print("\nTipe Data: ", type(isi_file))

# LD: 2
print("\n===== MEMBUKA FILE PERBARIS =====\n")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip()
        print("baris ke-", jumlah_baris)
        print("isinya: ", baris)
        
# LD: 3
# Parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom-kolom data
data_list = [] # inisialisasi list untuk menampung data
print("\n===== PARSING BARIS =====\n")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() # menghilangkan karakter baris baru (padetin)
        nim, nama, nilai = baris.split(",") # pecah data menjadi satuan dan menyimpan ke variabel
        print(f"NIM: {nim} | Nama: {nama} | Nilai: {nilai}") 
        data_list.append([nim,nama,int(nilai)]) # menyimpan data ke list

print("\n===== MENAMPILKAN LIST =====\n")
print(data_list)
print(" ")
print("contoh record ke 1", data_list[0])
print("contoh record ke 2", data_list[1])
print("jumlah record", len(data_list))

# LD: 4
# dictionary

data_dict = {}

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() # menghilangkan karakter baris baru (padetin)
        nim, nama, nilai = baris.split(",")
        data_dict [nim] = {
            "nama: ", nama,
            "nilai: ", int(nilai)
        }
print("\n===== MENAMPILKAN DATA DICTIONARY =====\n")
print(data_dict)