def match_words(word):
    ctr=0
    lst=[]
    for word in word:
        if len(word)>0 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)
    return ctr
count=match_words(["cfc","sdf","wmw",'xho','byb','gh','gg'])
print(count)