# Write a program to sort a string according to the frequency of character and return the final string.

# samples
# Input	output
# hello world	llloohe wrd
# tree	eetr
# Tasks

def sort_s(s):
    d={}
    for j in s:
        if j in d:
            d[j]+=1
        else:
            d[j]=1
    # print(d)
    l=sorted(d.items(),key=lambda x:x[1],reverse=True)
    ans=''
    for s in l:
        # print(s[0]*s[1],end='')
        ans+=s[0]*s[1]
    # print()
    return ans
