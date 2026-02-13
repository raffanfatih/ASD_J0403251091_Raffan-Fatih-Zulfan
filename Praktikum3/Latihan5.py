class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: 
            self.head = new_node
            self.tail = new_node 
        else:
            self.tail.next = new_node 
            self.tail = new_node 

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head 

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev 


elemen = input("Masukkan elemen untuk Linked List: ").strip().split(" ")

ll = LinkedList()

for i in elemen:
    ll.insert_at_end(i)

print("\nLinked List sebelum dibalik: ", end="")
ll.display_forward()

ll.reverse()
print("Linked List setelah dibalik: ", end="")
ll.display_forward()