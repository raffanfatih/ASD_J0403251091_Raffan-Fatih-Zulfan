# ==============================
# Nama  : Raffan Fatih Zulfan
# NIM   : J0403251091
# Kelas : A2
# ==============================

def matrixToList(matrix):
    # Dapatkan jumlah node/vertex dari ukuran matriks
    V = len(matrix)

    # Menyiapkan dictionary kosong untuk Adjacency List
    adj_list = {}

    # Proses konversi
    for i in range(V):
        tetangga = []
        for j in range(V):
            # Jika bernilai 1, berarti ada hubungan, tambahkan ke daftar tetangga
            if matrix[i][j] == 1:
                tetangga.append(j)
        
        # Menyimpan daftar tetangga ke node yang sesuai
        adj_list[i] = tetangga

    return adj_list

if __name__ == "__main__":
    # Adjacency Matrix yang diberikan dari soal
    matrix = [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 0, 1, 0]
    ]

    # Konversi matriks adjacency ke adjacency list menggunakan fungsi
    hasil_adj_list = matrixToList(matrix)

    # Menampilkan hasil
    print("Hasil Konversi ke Adjacency List:")
    for node, daftar_tetangga in hasil_adj_list.items():
        print(f"Node {node} -> {daftar_tetangga}")