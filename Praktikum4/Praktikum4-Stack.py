# ============================
# Nama  : Raffan Fatih Zulfan
# NIM   : J0403251091
# Kelas : A2
# ============================

# ============================
# Implementasi Dasar : Stack
# ============================

class Node:
    # konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self,data):
        self.data = data # menyimpan nilai atau data pada list
        self.next = None # pointer ini menunjuk ke note berikutnya (awal = none)

# stack ada operasi push (memasukkan head baru) and pop (menghapus head)

class stack:
    def __init__(self):
        self.top = None # top menunjuk ke node paling atas (awalnya kosong)

    def is_empty(self):
        return self.top is None # stack kosong jika = none
    
    def push(self,data):
        # 1) membuat node baru
        nodeBaru = Node(data) # instantiasi/memanggil konstruktor pada class node

        # 2) node baru menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top

        # 3) geser top pindah ke node baru
        self.top = nodeBaru

    def pop(self): # mengambil/menghapus node paling atas (top/head)
        if self.is_empty():
            print("Stack is Empty")
            return None
        data_terhapus = self.top.data # soroti bagian top dan simpan di variabel
        self.top = self.top.next # geser top ke node beriktnya
        return data_terhapus
        
    def peek(self):
        # melihat data ang paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data

    def tampilkan(self):
        current = self.top
        print("Top", end=" -> ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# instansiasi class stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
print("Peek (Lihat Top): ", s.peek())
s.pop()
print("Peek (Lihat Top): ", s.peek())