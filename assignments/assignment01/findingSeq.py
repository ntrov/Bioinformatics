from itertools import product
import re

def genRE(string, pos):
    res = ''
    for i in range(len(string)):
        if (i == pos):
            res += '.'
        else:
            res += string[i]

    return res


def findSeq(seq):
    allPosSeq = []
    index = 0
    ans = []


    # seq = input("enter the sequence:")
    seq = seq.split(" ")
    N = seq[0]
    seq.remove(N)
    k = seq[0]
    seq.remove(k)

    N = int(N)
    k = int(k)

    for i in product(['A', 'C', 'G', 'T'], repeat = k):
        allPosSeq.append("")
        for j in i:
            allPosSeq[index] += j
        index += 1

    for i in allPosSeq:
        count = 0
        for j in seq:
            for l in range(k):
                regex = genRE(i, l)
                if re.search(regex, j):
                    count += 1
                    break
        
        if count == N:
            ans.append(i)

    return ans


def main():

    with open('inputFile.txt', 'r') as file:
        file.read(2)
        cases = 0
        for line in file:
            cases += 1
            line = line.strip('\n')
            print('Case ' + str(cases) + ':', end = " ")

            for i in findSeq(line):
                print(i, end = " ")
            
            print('')



    # findSeq()

main()
