#User function Template for python3
import functools 

class Solution:
    def printLargest(self,arr) -> str:
        
        def largest(a:str,b:str):
            if a+b > b+a:
                return -1
            elif a+b < b+a:
                return +1
            else :
                return 0

        return str(int("".join(sorted(map(str,arr),key=functools.cmp_to_key(lambda a,b : largest(a,b))))))


def main():
    arr = [3,45,9,23,56]
    # ouput expected : 9 56 45 3 23 
    s = Solution()
    print(s.printLargest(arr))


if __name__ == "__main__":
    main()