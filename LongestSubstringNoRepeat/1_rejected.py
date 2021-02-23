class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        len(set(s)) 
        #read the problem again!!. We have to find the longest possible substring and not unique chars.
    
def main():
    # instr = "abcabcbb"  #pass
    instr = "pwwkew"  #fails
    # ouput expected : 3 (wke) 
    s = Solution()
    print(s.lengthOfLongestSubstring(instr))


if __name__ == "__main__":
    main()

