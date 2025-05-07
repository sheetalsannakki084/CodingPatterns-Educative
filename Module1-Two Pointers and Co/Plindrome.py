

def Pali(a):
    n=len(a)
    l=0
    r=n-1
    while l<r and r<n:
        if a[l]!=a[r]:
            return False

        l+=1
        r-=1
    return True




a="mtrtamatrtm"
obj=Pali(a)
print(obj)
