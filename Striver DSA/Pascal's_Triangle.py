# Program to generate Pascal's Triangle

def generate_element(r,c):
    n=r-1 # row number
    r=c-1 # column number
    # now caluclate the value of nCr
    res=1
    for i in range(r):
        res=res*(n - i)
        res=res // (i + 1)
    return res

if __name__ == '__main__':
    r = 5 # row number
    c = 3 # col number
    element = generate_element(r, c)
    print(f"The element at position (r,c) is: {element}")