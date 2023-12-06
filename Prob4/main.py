#!/usr/bin/env python3

def part1():
    with open('input.txt') as f:
        data=list(filter(None,f.read().split('\n')))
    sum=0
    for row in data:
        w,a=row.split(":")[1].split(" | ")
        y=len(set(w.split()) & set(a.split()))
        sum+=2**(y-1) if y>0 else 0
    print(sum)
    return

def part2():
    with open('input.txt') as f:
        data=list(filter(None,f.read().split('\n')))
    res=[1]*len(data)
    for row in range(len(data)):
        w,a=data[row].split(":")[1].split(" | ")
        y=len(set(w.split()) & set(a.split()))
        for i in range(row+1,row+y+1):
            res[i]+=res[row]
    print(sum(res))
    return


if __name__ == "__main__":
    part2()

