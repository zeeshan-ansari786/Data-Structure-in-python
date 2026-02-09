# 1. Implement a normal (linear) queue using an array with the following operations:
# ● Enqueue
# ● Dequeue
# ● Peek / Front
# ● Display
# ● IsEmpty
# ● IsFull

queue = None
item = None
rear = None
front = None
max_size=None

def q_init(size):
    global queue,item,rear,front,count,max_size
    max_size = size
    queue =[]
    front = rear = -1
    return "Success"

def is_empty():
    global front , rear
    return front == -1 or rear == -1

def is_full():
    global rear
    return rear == max_size

def enqueue(d):
    global queue, front, rear
    if is_full():
        return "Overflow"
    if front == -1:
        rear +=1
        front +=1
        queue.append(d)
        return "Sucessess"
    rear +=1
    queue.append(d)
    return "Sucessess"

def dequeue():
    global queue, front , rear,item
    if is_empty():
        return "Underflow"
    if rear > front:
        item = queue[front]
        front +=1
        return item
    if rear == front:
        item = queue[front]
        front +=1
        rear = -1
        return item

def display():
    global queue,rear,front,item
    if is_empty():
        return "Queue is empty.....!"
    for item in range(front , rear):
        print(queue[item],end=" ")

def peak():
    global front,queue
    if is_empty():
        return "empty queue"
    return queue[front]

while(True):
    print("Enter your choice...... \n 1.init \n 2. is_empty \n 3.is_full \n 4. Enque() \n 5. dequeue() \n 6. display() \n 7. peak()")
    ch = int(input("Enter your choice .......:"))

    if ch == 1:
        s=int(input("Enter the size of queue.......:"))
        print(q_init(s))
    elif ch == 2:
        if is_empty():
            print("queue is empty .......!")
        else:
            print("there is some value .......!")
    elif ch == 3:
        if is_full():
            print("queue is full .......!")
        else:
            print("there is some spaces.........!")
    elif ch == 4:
        v=int(input("Enter the value.......:"))
        print(enqueue(v))
    elif ch == 5:
        print(dequeue())
    elif ch == 6 :
        print(display())
    elif ch == 7 :
        print(peak())
    else:
        print("Enter valid choice ............!")
