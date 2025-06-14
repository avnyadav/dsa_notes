def inclusion(s1,s2):
    if len(s1)>len(s2): return False
    result = []
    s1Count,s2Count = [0]*26,[0]*26
    for i in range(len(s1)):
        s1Count[ord(s1[i])-ord('a')]+=1
        s2Count[ord(s2[i])-ord('a')]+=1
    
    matches = 0
    for i in range(26):
        matches+= 1 if s1Count[i]==s2Count[i] else 0
    l=0
    for i in range(len(s1),len(s2)):
        if matches==26:
            result.append(l)
        index = ord(s2[i])-ord('a')
        s2Count[index]+=1

        if s1Count[index]==s2Count[index]:
            matches+=1
        if s1Count[index]+1==s2Count[index]:
            matches-=1

        index = ord(s2[l])-ord('a')
        s2Count[index]-=1

        if s1Count[index]==s2Count[index]:
            matches+=1
        if s1Count[index]-1==s2Count[index]:
            matches-=1
        
        l+=1

    if matches==26:
        result.append(l)

    return result


if __name__=="__main__":
    s1='ab'
    s2='abab'
    print(inclusion(s1,s2))

              