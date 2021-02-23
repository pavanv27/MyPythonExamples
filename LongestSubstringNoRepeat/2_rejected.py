class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        repeatdetect = False
        lastchar =""
        tempout,output = 0,0
        for i,v in enumerate(s):
            if v in d:
                if v==lastchar  :
                    repeatdetect = True
                    tempout = 1
                elif not repeatdetect :
                    tempout = i-d[v]
                elif repeatdetect :
                    tempout += 1
            else:
                tempout += 1
            
            d[v] = i
            lastchar = v
            output = max(tempout,output)

        return output
    #len(set(s))
    
def main():
    instr = "pwwkew"
    # ouput expected : 3 (wke) 
    s = Solution()
    print(s.lengthOfLongestSubstring(instr))


if __name__ == "__main__":
    main()

# inputs:
#     "dvdf"
#     "pwwkew"
#     "bbbb"
#     "bbaabb"
#     "anviaj"
#     "ckilbkd"
#     "tmmzuxt"
# Output :
#     3
#     4
#     1
#     2
#     5
#     5
#     5
# Expected:
#     3
#     3
#     1
#     2
#     5
#     5
#     5
