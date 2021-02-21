class Solution(object):
    def twoSum(self, nums, target):
        
        for x in range(len(nums)):
            y=x+1
            while y< len(nums):
                if nums[x]+nums[y]==target:
                    return [x,y]
                y+=1
            
def main():
    arr = [3,45,9,23,56]
    target = 12
    # ouput expected : 9 56 45 3 23 
    s = Solution()
    print(s.twoSum(arr,target))


if __name__ == "__main__":
    main()

# Accepted:
# runtime : 36 ms
# memory : 13.7mb