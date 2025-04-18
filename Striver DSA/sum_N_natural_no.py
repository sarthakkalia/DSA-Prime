# Sum of first N Natural Numbers

def sum_natural_no(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
print(sum_natural_no(6))
