#!/usr/bin/env python3

def part1():
    with open('input.txt') as f:
        data=list(filter(None,f.read().split('\n')))
    tot=1
    times=list(map(int,data[0].split()[1:]))
    lens=list(map(int,data[1].split()[1:]))
    for i in range(len(times)):
        valids=0
        for j in range(times[i]):
            if (times[i]-j)*j>lens[i]:
                valids+=1 
        tot*=valids
    print(tot)
    return

def part2():
    with open('input.txt') as f:
        data=list(filter(None,f.read().split('\n')))
    time=int("".join(data[0].split()[1:]))
    lens=int("".join(data[1].split()[1:]))
    low,high=0,time
    while True:
        i=(high+low)//2
        if (time-i)*i>=lens:
            if (time-i-1)*(i-1)<lens:
                tot=time+1-2*i
                break
            else:
                high=i
        else:
            low=i
    print(tot)
    return

if __name__ == "__main__":
    part2()

