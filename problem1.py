# Write a program to sort a string according to the frequency of character and return the final string.

# samples
# Input	output
# hello world	llloohe wrd
# tree	eetr
# Tasks


s=['hello world','tree']
for i in s:
    d={}
    for j in i:
        if j in d:
            d[j]+=1
        else:
            d[j]=1
    # print(d)
    l=sorted(d.items(),key=lambda x:x[1],reverse=True)
    # print(l)
    for i in l:
        print(i[0]*i[1],end='')
    print()
