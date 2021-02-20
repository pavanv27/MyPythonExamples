#User function Template for python3
class Solution:

    def printLargest(self,arr) -> str:
        
        def largest(a:str,b:str)->bool:
            if a+b < b+a:
                return True
	    
        #main logic : string cat + sort by int compare        
        for x in range(len(arr)-1,-1,-1):
            for y in range(x):
                if largest(str(arr[y]),str(arr[y+1])):
                    arr[y],arr[y+1]= arr[y+1],arr[y]

        return str(int("".join(map(str,arr))))
                
def main():
    arr = [3,45,9,23,56]
    # ouput expected : 9 56 45 3 23 
    s = Solution()
    print(s.printLargest(arr))

if __name__ == "__main__":
    main()      

