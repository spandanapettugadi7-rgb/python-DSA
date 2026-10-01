def selectionsort(a):
  for i in range(len(a)):
    min=i
    for j in range(i+1,len(a)):
      if a[j]<a[min]:
        min=j
    a[i],a[min]=a[min],a[i]
  return a
a=[5,3,1,6,2,4]
print(selectionsort(a))
