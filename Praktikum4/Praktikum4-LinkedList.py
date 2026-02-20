# ============================
# Nama  : Raffan Fatih Zulfan
# NIM   : J0403251091
# Kelas : A2
# ============================

# ==========================================
# Implementasi Dasar : Node pada Linked List
# ==========================================

class Node:
    # konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self,data):
        self.data = data # menyimpan nilai atau data pada list
        self.next = None # pointer ini menunjuk ke note berikutnya (awal = none)

# 1) membuat node dengan instantiasi class Node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) mendefinisikan head dan menghubungkan Node : A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

# 3) Transversal : menelusuri node dari head samoai ke None
current = head
while current is not None:
    print(current.data) # menampilkan data pada node saat ini
    current = current.next # pindah ke node setelahnya
