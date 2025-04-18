# Print N to 1 using Recursion

def print_N_1(i,n):
    if(i>n):
        return 
    print_N_1(i+1, n)
    print(i)

print_N_1(1, 4)