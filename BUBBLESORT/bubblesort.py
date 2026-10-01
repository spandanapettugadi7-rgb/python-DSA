def bubblesort(a):
  for i in range(len(a)):
    for j in range(i+1,len(a)):
      if a[i]>a[j]:
        a[i],a[j]=a[j],a[i]
  return a
a=[5,3,1,6,2,4]
print(bubblesort(a))