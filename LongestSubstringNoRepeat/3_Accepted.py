class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        output = 0
        d = {}
        i = 0
        # sliding window concept - window of j to i
        for j,v in enumerate(s):
            if v in d:
                i = max(d[v], i)

            output = max(output, (j + 1) - i)
            d[v] = j + 1

        return output

def main():
    s = Solution()
    instr = "pwwkew"
    # ouput expected : 3 (wke) 
    print(s.lengthOfLongestSubstring(instr))


if __name__ == "__main__":
    main()

# Runtime: 48 ms, faster than 74.56% of Python online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 13.5 MB, less than 87.66% of Python online submissions for Longest Substring Without Repeating Characters.