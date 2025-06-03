class Solution:
    def intToRoman(self, num: int) -> str:

        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symb=  ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

        roman=""
        for i in range(len(val)):

            n_time_symb = num//val[i]
            roman+=f"{symb[i]*n_time_symb}"
            num = num%val[i]
        
        return roman

    
if __name__=="__main__":
    print(Solution().intToRoman(3749))
