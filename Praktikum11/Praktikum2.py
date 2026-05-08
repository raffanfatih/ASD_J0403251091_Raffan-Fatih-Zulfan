# ==============================
# Nama  : Raffan Fatih Zulfan
# NIM   : J0403251091
# Kelas : A2
# ==============================

def createGraph(V, edges):
    # Membuat list kosong sebanyak V
    adj = [[]for _ in range(V)]

    # Memasukkan setiap edge ke adjacency list
    for it in edges:
        u = it[0]
        v = it[1]
        adj [u].append(v)
        # Karena undirected graph, masukkan bolak-balik        
        adj [v].append(u)
    return adj

if __name__ == "__main__":
    V = 4

    # Dictionary penerjemah angka menjadi huruf
    huruf = {
            0 : 'A',
            1 : 'B',
            2 : 'C',
            3 : 'D'
        }
    # List edges (u, V)
    edges = [[0, 1], [0, 2], [2, 3], [1, 3]]

    # Membangun graph
    adj = createGraph(V, edges)

    print("Adjacency List Representation:")
    for i in range(V):

        # Mencetak Node utamanya (diterjemahkan ke huruf)
        print(f"{huruf[i]}:", end=" ")
        for j in adj[i]:
            
            # Mencetak tetangganya (diterjemahkan ke huruf)
            print(huruf[j], end=" ")
        print()