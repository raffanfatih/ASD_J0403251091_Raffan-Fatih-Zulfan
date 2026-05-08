# ==============================
# Nama  : Raffan Fatih Zulfan
# NIM   : J0403251091
# Kelas : A2
# ==============================

def createGraph(V, edges):
    # Inisialisasi matriks 4x4 dengan nilai 0
    mat = [[0 for _ in range(V)] for _ in range(V)]

    # Memasukkan hubungan ke dalam matriks (Undirected Graph)
    for it in edges:
        u = it[0]
        v = it[1]
        mat [u][v] = 1
        mat [v][u] = 1
    return mat

if __name__ == "__main__":
    V = 4

    # Daftar edge (hubungan antar node)
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
    
    # Build the graph using edges
    mat = createGraph(V, edges)
    
    # Menampilkan hasil matriks
    print("Adjacency Matrix Representation:")
    for i in range(V): 
        for j in range(V):
            print(mat[i][j], end=" ")
        print()