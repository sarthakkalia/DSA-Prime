# Remove Duplicates Recursively

def remove_duplicates(s):
    if(len(s)==0 or len(s)==1):
        return s
    if(s[0]==s[1]):
        smallerOutput=remove_duplicates(s[2:])
        return s[0]+smallerOutput
    else:
        smallerOutput=remove_duplicates(s[1:])
        return s[0]+smallerOutput
print(remove_duplicates('ssabccb'))