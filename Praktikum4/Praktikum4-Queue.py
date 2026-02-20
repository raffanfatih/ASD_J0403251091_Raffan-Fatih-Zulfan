# ============================
# Nama  : Raffan Fatih Zulfan
# NIM   : J0403251091
# Kelas : A2
# ============================

# ============================
# Implementasi Dasar : Queue
# ============================

class Node:
    # konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self,data):
        self.data = data # menyimpan nilai atau data pada list
        self.next = None # pointer ini menunjuk ke note berikutnya (awal = none)

class queue:
    # buat konstruktor untuk inisialisasi variabel front and rear
    def __init__(self):
        self.front = None # Node paling depan
        self.rear = None # Node paling belakang 
    
    def empty(self):
        return self.front is None

    # membuat fungsi untuk menambahkan data baru
    def enqueue(self,data):
        nodeBaru = Node(data)

        # jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.empty():
            self.front = nodeBaru
            self.rear = nodeBaru

        # jika queue tidak kosong, maka letakkan dat abaru ke rear    
        self.rear.next = nodeBaru # letakkan data baru pada setelahnya rear
        self.rear = nodeBaru # jadikan data baru sebagai rear

    def dequeue(self):
        # mebghapus data dari depan/front
        data_terhapus = self.front.data # lihat data paling depan
        
        # geser front ke node berikutnya
        self.front = self.front.next

        # jika setelah geser front menjadi node, maka queue kosong
        # rear juga harus jadi none
        if self.front is self.rear:
            self.rear = None
        return data_terhapus

    def tampilkan(self):
        current = self.front
        print("Front ->", end=" ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("Rear")

# instantiasi class queue
q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()