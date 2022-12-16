import argparse

def printPasTriangle(rows:int):
    row = [1]
    for i in range(rows):
        print(row)
        row = [sum(x) for x in zip([0]+row, row+[0])]
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pascal Triangle")
    parser.add_argument("rows", help="rows number")

    args = parser.parse_args()

    printPasTriangle(int(args.rows))