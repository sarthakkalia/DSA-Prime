# Print N to 1 using Recursion

def print_N_1(i,n):
    if(i<1):
        return
    print(i)
    print_N_1(i-1, n)

print_N_1(4, 4)