
def Display(self):
    temp = self.head
    while(temp):
        print (temp.data , "->", endn= "")
        temp=temp.next_node
        print(" ")