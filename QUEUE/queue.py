class queue:
  def __init__(self,cap=3):
    self._a=[None for i in range(cap)]
    self._front=None
    self._rear=-1
    self._c=0
  def enqueue(self,data):
    if self._c==len(self._a):
      print('overflow')
      return
    if self._c==0:
      self._a[self._c]=data
      self._front=0
      self._c=1
    else:
      self._a[self._c]=data
      self._c+=1
  def peek(self):
    if self._c==0:
      return "no elements"
    return self._a[self._front]
  def peekLast(self):
    return self._a[self._c-1]
  def dequeue(self):
    if self._c==0:
      return 'underflow'
    ar=[None for i in range(len(self._a))]
    for i in range(1,len(self._a)):
      ar[i-1]=self._a[i]
    temp=self._a[0]
    self._a=ar
    self._c-=1
    return temp
  def isempty(self):
    return self._c==0
  def isfull(self):
    return self._c==len(self._a)
q=queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.peek())
print(q.isempty())
print(q.isfull())