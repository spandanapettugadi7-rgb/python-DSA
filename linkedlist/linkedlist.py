class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class Linkedlist:
  def __init__(self):
    self.head=None
    self.size=0
  def add(self,data):
    obj=Node(data)
    if self.head==None:
      self.head=obj
      self.size+=1
      return

    cn=self.head
    while cn.next is not None:
      cn=cn.next
    cn.next=obj
    self.size+=1

  def traverse(self):
    cn=self.head
    while cn.next is not None:
      print(cn.data,end="->")
      cn=cn.next
    print(cn.data)

  def delfirst(self):
    self.head=self.head.next
  def delLast(self):
    cn=self.head
    if cn.next is None:
      cn=None
    while cn.next.next is not None:
      cn=cn.next
    cn.next=None
    self.size-=1
  
  def len(self):
    return self.size
  def ins_at(self,data,pos):
    if pos==0:
      obj=Node(data)
      obj.next=self.head
      self.head=obj
      return
    if pos<self.len() and pos>0:
      ind=0
      cn=self.head
      while cn.next is not None:
        if ind+1==pos:
          break
        cn=cn.next
        ind+=1
      obj=Node(data)
      obj.next=cn.next
      cn.next=obj
      self.size+=1
  def ins_start(self,data):
    if self.head==None:
      self.head=Node(data)
      return
    else:
      obj=Node(data)
      obj.next=self.head
      self.head=obj
  def count(self,data):
    if self.head is None:
      return 0
    c=0
    cn=self.head
    while cn.next is not None:
      if cn.data==data:
        c+=1
      cn=cn.next
    if cn.data==data:
      c+=1
    return c
   
ll=Linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)
ll.traverse()
ll.delfirst()
ll.traverse()
ll.delLast()
ll.traverse()
print(ll.len())
ll.ins_at(50,2)
ll.traverse()
ll.ins_start(10)
ll.traverse()
ll.add(20)
ll.traverse()
print(ll.count(20))