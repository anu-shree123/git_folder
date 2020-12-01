def is_empty():
    global rear,front
    if front == -1 and rear == -1:
        return True
    return False

def is_full():
    global rear,front
    if (rear+1)%n == front:
        print("QUEUE FULL")
        return True
    return False

def Enqueue(x):
    global rear,front
    if is_empty():
        front = rear = 0
        arr[rear] = x

    elif is_full():
        return

    else:
        rear = (rear+1) % n
        arr[rear] = x

def dequeue():
    global rear,front
    if is_empty():
        return

    elif front == rear:
        front = rear = -1

    else:
        front = (front+1) % n

def front():
    global rear,front
    if is_empty():
        return
    return arr[front]

def is_print():
    global rear,front
    if is_empty():
        print("Queue is empty")
    else:
        print("Queue :",end = " ")
        for i in range(front,rear+1):
            print(arr[i],end = " ")
        print()


if __name__ == "__main__":
    n = int(input())
    arr = [0]*n
    front = rear = -1

    Enqueue(2)
    Enqueue(2)
    Enqueue(2)
    Enqueue(2)
    Enqueue(2)
    dequeue()
    dequeue()
    is_print()
    Enqueue(3)
    Enqueue(3)
    is_print()

    
    
    
    

