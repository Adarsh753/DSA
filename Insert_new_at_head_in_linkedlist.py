'''Insertnew node at head '''
def Insert_at_head(self,data):
    new_node=new_node(data)
    new_node.next_node=self.head
    self.head=new_node

'''Insertnew node at begning'''

def Insert_at_begin(self,  new_data):
    new_node=new_node(new_data)
    new_node.next_node=self.head
    self.head=new_node

'''Insertnew node at end'''
def Insert_at_end(self,new_data):
    new_node=Node(new_data)
    if self.head is None:
        self.head=new_node
        return
    last=self.head
    while(last.next):
        last=last.next
        last.next=new_node
