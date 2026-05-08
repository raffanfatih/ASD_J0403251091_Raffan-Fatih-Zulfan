# ==============================
# Nama  : Raffan Fatih Zulfan
# NIM   : J0403251091
# Kelas : A2
# ==============================

def buat_graph(V, edges, nama_user):
    # Inisialisasi Adjacency Matrix (ukuran VxV)
    matrix = [[0 for _ in range(V)] for _ in range(V)]
    
    # Inisialisasi Adjacency List menggunakan dictionary
    adj_list = {nama_user[i]: [] for i in range(V)}

    for u, v in edges:
        # Nama untuk indexing list
        nama_u = nama_user[u]
        nama_v = nama_user[v]
        
        # Karena hubungan mutualan (Undirected), isi di kedua sisi
        # Update Matrix
        matrix[u][v] = 1
        matrix[v][u] = 1
        
        # Update List
        adj_list[nama_u].append(nama_v)
        adj_list[nama_v].append(nama_u)
    
    return matrix, adj_list

if __name__ == "__main__":
    # 1. Definisi Vertex (Node)
    nama_user = {
        0: "Ihsan",
        1: "Raxen",
        2: "Ivan",
        3: "Aulia",
        4: "Ibra"
    }
    V = len(nama_user)

    # 2. Definisi 6 Edge (Hubungan Mutualan)
    edges = [[0, 1], [0, 2], [0, 4], [1, 3], [2, 3], [3, 4]]

    # Membangun graph
    matrix, hasil_adj_list = buat_graph(V, edges, nama_user)

    # 3. Menampilkan Output
    print("Daftar Node (User):")
    for i in range(V):
        print(f"  - {nama_user[i]}")

    print("\nHubungan (Mutualan):")
    for u, v in edges:
        print(f"  {nama_user[u]} - {nama_user[v]}")

    print("\nAdjacency List:")
    for user, teman in hasil_adj_list.items():
        print(f"  {user}\t: {teman}")

    print("\nAdjacency Matrix:")
    for i in range(V):
        print(matrix[i])