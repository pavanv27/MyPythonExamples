
def main():
    s = ["this","is","a","sample","input"]
    print(s)
    reverseList(s)
    print(s)

    s = [1,2,3,4,5]
    print(s)
    reverseList(s)
    print(s)

def reverseList(s):
    first = 0
    last = len(s) - 1
    while first < last :
        s[first], s[last] = s[last], s[first]
        first+=1
        last-=1

if __name__ == "__main__":
    main()