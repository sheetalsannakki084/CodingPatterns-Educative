def solution(w):
    sl=w.split()
    count=0

    for i ,word in enumerate(sl):
        valid=True
        hypencount=0
        for j ,w in  enumerate(word):
            if w.isdigit():
                valid=False
                break
            if w =='-' and (j==len(word)-1 or j==0) or(w=='-' and (not word[j - 1].isalpha() or not word[j + 1].isalpha())):
                valid=False
                break
            if w in  (",",".","!")and j!=len(word)-1 :
                valid=False
                break
            if w=='-':
                hypencount+=1
                if hypencount>1:
                    valid=False
                    break
        if valid:
            count+=1

    return count















w="sheet wt nt"
obj=solution(w)
print(obj)