class LinkedList:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.len = 1
    def find(self, val):
        temp = self
        pos = 0
        while temp is not None:
            if temp.value == val:
                return pos
            pos += 1
            temp = temp.next
        else:
            return -1
    def insert(self, val, pos):
        temp_pos = 1
        if pos == 0:
            temp = LinkedList(self.value)
            temp.next = self.next
            self.value = val
            self.next = temp
            self.len += 1
        else:
            temp = self
            while temp is not None:
                #print(pos,temp_pos,val,temp.value)
                if pos == temp_pos:
                    nuevo = LinkedList(val)
                    nuevo.next = temp.next
                    temp.next = nuevo
                    self.len += 1
                    break
                temp_pos += 1
                temp = temp.next
            else:
                print("Error:Cannot insert in index " + str(pos))
    def remove(self, val):
        pos = self.find(val)
        if pos == -1:
            return None
        elif pos == 0:
            self.value = self.next.value
            self.next = self.next.next
            self.len -= 1
        else:
            temp_pos = 1
            temp = self
            while temp is not None:
                if pos == temp_pos:
                    temp.next = temp.next.next
                    self.len -= 1
                temp_pos += 1
                temp = temp.next
    def length(self):
        return self.len
    def printlist(self):
        temp = self
        while temp is not None:
            print(temp.value,end=", ")
            temp = temp.next
        print()

a = LinkedList(1)
print(a.length())
a.insert(2,1)
print(a.length())
a.insert(3,2)
print(a.length())
a.insert(4,3)
print(a.length())
a.insert(5,4)
print(a.length())
a.printlist()
a.remove(1)
print(a.length())
a.printlist()
a.remove(3)
print(a.length())
a.printlist()
