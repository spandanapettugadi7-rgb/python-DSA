[3:01 pm, 08/09/2026] 🦋: class Stack:
  def _init_(self):
    self._a=[]
    self._top=None
  def push(self,data):
    if self._top is not None:
        if self._top+1==self._size:
            return "stack overflow"
    if self._top is None:
      ar=[0]
      self._top=0
      ar[self._top]=data
      self._a=ar
    else:
      ar=[]
      for i in self._a:
        ar.append(i)
      ar.append(data)
      self._top+=1
      self._a=ar
  def peek(self):
    if self._top is None:
        return "stack underflow"
    return self._a[self._top]
  def isEmpty(self):
      if self._top is None:
          return True
      return False
          
stack=Stack(3)
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.peek())

