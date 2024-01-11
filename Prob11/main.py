#!/usr/bin/env python3

def part1(coeff=2):
    with open('input.txt') as f:
        data=list(filter(None,f.read().split('\n')))
    galaxies,expGals,sum=[],[],0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j]=='#':
                galaxies+=[(i,j)]
    emptyRows,emptyCols=[1]*len(data),[1]*len(data[0])
    for i,j in galaxies:
        emptyRows[i]=0
        emptyCols[j]=0
    for gal in galaxies:
        expGals.append((gal[0]+emptyRows[:gal[0]].count(1)*(coeff-1),gal[1]+emptyCols[:gal[1]].count(1)*(coeff-1)))
    # print(expGals)
    for i,j in expGals:
        for ii,jj in expGals:
            sum+=abs(i-ii)+abs(j-jj)
    print(sum//2)
    return

def part2():
    return part1(1000000)

if __name__ == "__main__":
    part1()
    part2()

