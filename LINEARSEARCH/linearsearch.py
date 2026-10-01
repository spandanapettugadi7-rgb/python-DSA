def linearsearch(ar,target):
  for i in range(len(ar)):
    if ar[i]==target:
      print(f"{target} is not found at index {i}")
      return
  print("element not found")
  return
a=[23,12,22,45,7,8]
linearsearch(a,12)
