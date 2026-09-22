def prefix(a):
  ar=[]
  sum=a[0]
  ar.append(sum)
  for i in range(1,len(a)):
    ar.append(i)
    sum+=a[i]
  return ar

a=[3,1,4,1,5,9,2,6]
res=prefix(a)
print(res)
print(res[5]-res[2-1])

def equilibrium_index(arr):
  total_sum = sum(arr)
  left_sum = 0
  
  for i in range(len(arr)):
      right_sum = total_sum - left_sum - arr[i]
      
      if left_sum == right_sum:
          return i
      
      left_sum += arr[i]
  
  return -1

numbers = [-7, 1, 5, 2, -4, 3, 0]
print(equilibrium_index(numbers))  

s='spandana'
print(a[0:2])
print(s[0:2])

#strings

st='abbabbb'
sub='ab'
def check(st,sub,i):
  temp=i
  for k in range(len(sub)):
    if st[i]!=sub[k]:
      return -1
    i+=1
  return temp
for i in range(len(st)):
  j=0
  if sub[j]==st[i]:
    print(check(st,sub,i))
  j+=1

#anagrams

def is_anagram(s1,s2):
  if len(s1)!=len(s2):
    return False
  a=[""for _ in range(len(s1))]
  b=[""for _ in range(len(s2))]
  for i in range(len(s1)):
    a[i]=s1[i]
  for i in range(len(s2)):
    b[i]=s2[i]

  a.sort()
  b.sort()
  for i in range(len(a)):
    if a[i]!=b[i]:
      return False
    return True
s='hello'
s2='olleh'
print(is_anagram(s,s2))


