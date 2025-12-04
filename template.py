import argparse

def parseFile(fileName: str, res: list[str]):
    with open(fileName) as f:
        for line in f:
            line = line.strip()
            res.append(line)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='fileName', default='input.txt')
    args = parser.parse_args()

    input = []
    parseFile(args.fileName, input)
    print(input)

if __name__ == "__main__":
    main()
