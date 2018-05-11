# TITLE : Find the Runner-Up Score! 

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
    # sort the input
    arr.sort(reverse=True)
    # iterate and find the runner up score
    winnerScore = arr[0]
    runnerUpScore = 0
    for i in range(len(arr)):
        if arr[i] < winnerScore :
            runnerUpScore = arr[i]
            break
    
    print runnerUpScore