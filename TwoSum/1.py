class Solution(object):
    def twoSum(self, nums, target):
                    
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for x in range(len(nums)-1,-1,-1):
            for y in range(x):
                if nums[x]+nums[y]==target:
                    return [x,y]


def main():
    arr = [3,45,9,23,56]
    target = 12
    # ouput expected : 9 56 45 3 23 
    s = Solution()
    print(s.twoSum(arr,target))


if __name__ == "__main__":
    main()

# Accepted:
# runtime : 388 ms
# memory : 13.7mb