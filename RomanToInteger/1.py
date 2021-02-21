class Solution(object):
    def romanToInt(self, s:str)-> int:
        lookup = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        
        output = 0
        for i,v in enumerate(s):
            if i<len(s)-1 and lookup[v] < lookup[s[i+1]]:
                output -= lookup[v]
            else:
                output += lookup[v]
                
        return output
            
def main():
    romanstr = "LVIII"
    # ouput expected : 58 
    s = Solution()
    print(s.romanToInt(romanstr))


if __name__ == "__main__":
    main()