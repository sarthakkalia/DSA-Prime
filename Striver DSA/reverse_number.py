def check_pallindrome(num):
    original_num=num
    rev_no=0
    while num>0:
        digit=num%10
        rev_no=rev_no*10+digit
        num=num//10
    if(original_num==rev_no):
        return True
    else:
        return False
print(check_pallindrome(121))