


word = 'a1b1'


def letter_case_permutation(s:str):

    res = []

    def backtrack(sub="",i=0):
        if len(sub)==len(s):
            res.append(sub)
            return
        
        if s[i].isalpha():
            backtrack(sub+s[i].swapcase(),i+1)
        backtrack(sub+s[i],i+1)

    backtrack()
    return res 


res = letter_case_permutation(word)
print(res)

        