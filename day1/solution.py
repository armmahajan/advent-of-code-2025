# Day 1 Solution

def fileToArr(file: str):
    arr = []
    with open(file) as f:
        while curr := f.readline():
            arr.append(curr)
    return arr
    
def parseArr(arr):
    zeroCount = 0
    curr = 50 
    for string in arr:
        if not string: continue

        string = string.strip()
        direction = ''
        countStr = ''
        for char in string:
            if not char: continue 
            if char.isalpha():
                direction = char
            else:
                countStr += char
        count = int(countStr)
        trueCount = count * -1 if direction == 'L' else count

        curr = (curr + trueCount) % 100
        if curr == 0: zeroCount += 1
    
    return zeroCount

def parseArr2(arr):
    zeroCount = 0
    curr = 50 
    for string in arr:
        string = string.strip()
        direction = ''
        countStr = ''
        for char in string:
            if not char: continue 
            if char.isalpha():
                direction = char
            else:
                countStr += char
        count = int(countStr)
        trueCount = count * -1 if direction == 'L' else count
        absTrueCount = abs(trueCount)
        
        while absTrueCount > 100:
            absTrueCount -= 100
            zeroCount += 1

        trueCount = absTrueCount * -1 if direction == 'L' else absTrueCount

        next = (curr + trueCount)
        if (next >= 100 or next <= 0) and curr != 0:
            zeroCount += 1

        curr = next % 100
    
    return zeroCount


def main():
    arr = fileToArr('input.txt')
    answer = parseArr(arr)
    print('ANSWER: ', answer)
    
    arr2 = fileToArr('input2.txt')
    answer2 = parseArr2(arr2)
    print('ANSWER2: ', answer2)

if __name__ == "__main__":
    main()
