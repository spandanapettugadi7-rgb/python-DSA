def longest_unique_substring(s):
    char_index={}
    max_length=0
    start=0
    for i in range(len(s)):
        if s[i] in char_index:
            start=char_index[s[i]]+1
        char_index[s[i]]=i
        max_length=max(max_length,i-start+1)
    return max_length

print(longest_unique_substring("spanspa"))


def maxofsubarrays(arr,k):
    result=[]
    for i in range(len(arr)-k+1):
        a=max(arr[i:i+k])
        result.append(a)
    return result
b=[1, 3, -1, -3, 5, 3, 6, 7]
print(maxofsubarrays(b,3))


def maxofsubarray(a,k):
    list=[]
    for i in range(k,len(a)+1):
        list.append(maximum(a,i-k,i))
    return list
def maximum(a,st,end):
    max=0
    for i in range(st,end):
        if max<a[i]:
            max=a[i]
    return max

a=[1, 3, -1, -3, 5, 3, 6, 7]
print(maxofsubarray(a,3))

def longest_unique_substring(s):
  char_index={}
  max_length=0
  start=0
  for i in range(len(s)):
      if s[i] in char_index:
          start=char_index[s[i]]+1
      char_index[s[i]]=i
      max_length=max(max_length,i-start+1)
  return max_length

print(longest_unique_substring("sssss"))

