# Day 3 solution

def parseFile(fileName: str) -> list[str]:
    res = []
    with open(fileName) as f:
        for line in f:
            res.append(line.strip())

    return res

def getBestTwo(numStr: str) -> int:
    prev = -1
    prevLargest = -1
    curr = -1
    currLargest = -1
    for idx, digit in enumerate(numStr):
        num = int(digit) 
        if idx == 0:
            prev = num
            continue
        curr = num
        prevLargest = max(prev, prevLargest) 
        currLargest = max(prevLargest * 10 + curr, currLargest)
        prev = curr
    
    return currLargest

def getBestTwelve(numStr: str) -> int:
    ans = numStr
    while len(ans) > 12:
        ans = deleteWorst(ans)

    return int(ans)


def deleteWorst(numStr: str) -> str:
    h = numStr[0]
    t = numStr[1::]
    if not t: return ''

    if int(h) >= int(t[0]):
        return h + deleteWorst(t)
    else:
        return t

def main():
    input = parseFile('input.txt')
    # total = 0
    bestTwelveTotal = 0
    for numStr in input:
        # total += getBestTwo(numStr)
        bestTwelveTotal += getBestTwelve(numStr)
        print(numStr, '\n', getBestTwelve(numStr))

    # print('Sum of best 2s: ', total)
    print('Sum of best 12s: ', bestTwelveTotal)


if __name__ == "__main__":
    main()
