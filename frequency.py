s="aabbbccddefa"
ch=s[0]
count=1
res=""
for each in s[1:]:
    if each==ch:
        count+=1
    else:
        res+=ch+str(count)
        count=1
        ch=each
res+=ch+str(count)
print(res)