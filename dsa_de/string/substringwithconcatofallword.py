from typing import List


def findSubstring2(words)->List[str]:
    res = []

    #base case 
    if len(words)==1:
        return ["".join(words[:])]
    
    for i in range(len(words)):
        word = words.pop(0)

        perms = findSubstring2(words)

        for idx in range(len(perms)):
            perms[idx]= perms[idx]+word
      
        
        res.extend(perms)
        words.append(word)
    


    return res


def findSubstring(words)->List[str]:
    res = []

    #base case 
    if len(words)==1:
        return [words[:]]
    
    for i in range(len(words)):
        word = words.pop(0)

        perms = findSubstring(words)

        for perm in perms:
            perm.append(word)
        
        res.extend(perms)
        words.append(word)
    


    return res

print(findSubstring2(["ab","cd","ef"]))