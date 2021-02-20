#User function Template for python3
class Solution:

    def printLargest(self,arr) -> str:
	    
	    #if inpupt is [0,0] it would return '00'.so ,
	    #if not any(map(bool,arr)):
	    #    return '0'
	     
	    #map executes a specified function for each item in an iterable
	    #arr = list(map(str,arr)) #convert all elements of arr to string
	    
	    #if arr has only one item?
	    #if len(arr) < 2:
	    #    return arr[0]
	    
        #main logic : string cat + sort by int compare
        for x in range(len(arr)-1,-1,-1):
            for y in range(x):
                if int(str(arr[y])+str(arr[y+1])) < int(str(arr[y+1])+str(arr[y])):
                    arr[y],arr[y+1]= arr[y+1],arr[y]

        return str(int("".join(map(str,arr))))

def main():
    arr = [3,45,9,23,56]
    # ouput expected : 9 56 45 3 23 (index : 2,4,1,0,3)
    s = Solution()
    print(s.printLargest(arr))

if __name__ == "__main__":
    main()