def binarysearch(a,target):
  l=0
  r=len(a)-1
  m=(l+r)//2
  while l<r:
    if a[m]==target:
      print(f"{target} is found at index {m}")
      return
    elif a[m]<target:
      l=m+1
      m=(l+r)//2
    else:
      r=m-1
      m=(l+r)//2
  print("element not  found")
b=[10,11,15,17,18,20]
binarysearch(b,18)
