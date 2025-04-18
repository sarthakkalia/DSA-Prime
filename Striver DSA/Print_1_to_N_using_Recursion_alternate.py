# Print 1 to N using Recursion

def fun(i,n):
    if(i<1):
        return 
    fun(i-1,n)
    print(i)
fun(4,4)
