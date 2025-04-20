# nth row of Pascal’s triangle calculate

def nCr(n,r):
    # now caluclate the value of nCr
    res=1
    for i in range(r):
        res=res*(n - i)
        res=res // (i + 1)
    return res

def pascalTriangle(n):
    for r in range(n):
        print(nCr(n-1,r),end=",")
    print()


# Optimal Solution
def PascalTriange(n):
    ans=1
    print(ans, end=" ")
    for i in range(1,n):
        ans = ans * (n - i)
        ans = ans // i
        print(ans, end=" ")
    print()

if __name__ == '__main__':
    n = 5
    PascalTriange(n)