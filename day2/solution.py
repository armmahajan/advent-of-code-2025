# Solution to day 2
import collections

def readFile(file: str):
    with open(file) as f:
        return f.readline()

def parseInput(input):
    input = input.strip()
    return input.split(',')

def checkRange(rng: str):
    rangeTotal = 0
    # Expects range in 'x1-x2' format
    rangeArr = rng.split('-')
    x1 = int(rangeArr[0])
    x2 = int(rangeArr[1])
    for i in range(x1, (x2+1)):
        iStr = str(i)
        if len(iStr) % 2 != 0:
            continue
        
        firstpart, secondpart = iStr[:len(iStr)//2], iStr[len(iStr)//2:]
        if firstpart == secondpart: rangeTotal += i

    return rangeTotal

def checkRange2(rng: str):
    rangeTotal = 0
    # Expects range in 'x1-x2' format
    rangeArr = rng.split('-')
    x1 = int(rangeArr[0])
    x2 = int(rangeArr[1])
    for i in range(x1, (x2+1)):
        iStr = str(i)
        for length in range(len(iStr) // 2 + 1):
            if length == 0 or len(iStr) % length != 0:
                continue
            split = splitString(iStr, length)
            if len(set(split)) == 1:
                print(split)
                rangeTotal += i
                break

    return rangeTotal

def splitString(string: str, partLength: int) -> list[str]:
    split = []
    q = collections.deque(list(string))
    counter = 0
    portion = []
    while q:
        portion.append(q.popleft())
        counter += 1
        if counter == partLength: 
            split.append(portion)
            portion = []
            counter = 0
    splitStr = []
    for arr in split:
        splitStr.append(''.join(arr))
    return splitStr


def main():
    input = readFile('input.txt')
    ranges = parseInput(input)
    
    total = 0
    for rng in ranges:
        total += checkRange2(rng)
    print('Summed invalid product IDs: ', total)

if __name__ == "__main__":
    main()
