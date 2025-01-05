def sizw(self):
    current=self.head
    count=0
    while current:
        count += 1
        current=current.next_node
        return count

