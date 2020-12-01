class Node:
    def __init__(self,data):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def EnQueue(self,new_data):
        newnode = Node(new_data)
        if self.rear is None:
            self.rear = self.front = newnode
            return
        self.rear.next = newnode
        self.rear = newnode

    def DeQueue(self):
        if self.is_empty():
            return
        temp = self.front 
        self.front = temp.next
        if(self.front == None): 
            self.rear = None
        
    def is_empty(self):
        return self.front == None
    
    def print1(self):
        if self.is_empty():
            print("Empty Queue")
            return
        temp = self.front
        while temp:
            print(temp.data)
            temp = temp.next
            

if __name__== '__main__': 
    q = Queue() 
    q.EnQueue(10) 
    q.EnQueue(20) 
    q.print1()
    q.DeQueue() 
    q.DeQueue() 
    q.EnQueue(30) 
    q.EnQueue(40) 
    q.EnQueue(50) 
    q.DeQueue() 
    
     
        