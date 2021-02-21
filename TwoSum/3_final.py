class Solution:
    def twoSum(self, nums, target):

        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

#logic:
# create a map of 
def main():
    # arr = [3,45,9,23,56]
    # target = 12
    
    # arr = [3,2,4]
    # target = 6
    
    arr = [3,3]
    target = 6
    # ouput expected : 9 56 45 3 23 
    s = Solution()
    print(s.twoSum(arr,target))


if __name__ == "__main__":
    main()

# Accepted:
# runtime : 28 ms
# memory : 13.4mb