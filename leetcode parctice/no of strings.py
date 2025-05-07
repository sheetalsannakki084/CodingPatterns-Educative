def solution(pat,w):
  c=0


  for p in pat:
      if p in w:
        c+=1
  return c





p=["a","abc","bc","d"]
w="abc"
obj=solution(p,w)
print(obj)