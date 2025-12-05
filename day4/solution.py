import argparse

def parseFile(fileName: str, res: list[str]):
    with open(fileName) as f:
        for line in f:
            line = line.strip()
            res.append(line)

def convertTo2DArr(input):
    for idx, string in enumerate(input):
        input[idx] = list(string)

def getRolls(input: list[str]) -> int:
    total = 0
    dirs = ([0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1])
    changed = []
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == '.': continue
            
            adjRolls = 0
            for dir in dirs:
                adjI, adjJ = i + dir[0], j + dir[1]
                if i + dir[0] not in range(len(input)) or j + dir[1] not in range(len(input[0])): continue
                
                if input[adjI][adjJ] == '@': adjRolls += 1
            if adjRolls < 4: 
                changed.append([i, j])
                total += 1 

    for i, j in changed:
        input[i][j] = '.'
    return total

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='fileName', default='input.txt')
    args = parser.parse_args()

    input = []
    parseFile(args.fileName, input)
    convertTo2DArr(input)

    grandTotal = 0
    while roundTotal := getRolls(input):
        print(roundTotal)
        grandTotal += roundTotal
    # print('Total Rolls: ', getRolls(input))
    print('Grand total rolls: ', grandTotal)

if __name__ == "__main__":
    main()
