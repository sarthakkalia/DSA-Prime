# replace pi in string

def replace_pi(s):
    if(len(s)==0 or len(s)==1):
        return s
    if(s[0]=='p' and s[1]=='i'):
        smallerOutput=replace_pi(s[2:])
        return '3.14'+smallerOutput
    else:
        smallerOutput=replace_pi(s[1:])
        return s[0]+smallerOutput
        
print(replace_pi('pippiabpi'))