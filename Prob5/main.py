#!/usr/bin/env python3


def part1():
    with open("./input.txt") as f:
        data=list(filter(None,f.read().split('\n')))
    seeds=[int(i) for i in data[0].split() if i!="seeds:"]
    data=data[1:]+["foo bar"]
    M=[]
    for row in data:
        numbers=row.split()
        if len(numbers)==2:
            if M:
                for i in range(len(seeds)):
                    for j in M:
                        if seeds[i]>=int(j[1]) and seeds[i]<int(j[1])+int(j[2]):
                            seeds[i]=seeds[i]-int(j[1])+int(j[0])
                            break
            M=[]
        else:
            M+=[numbers]
    print(min(seeds))
    return

def part2():
    with open("./input.txt") as f:
        data=list(filter(None,f.read().split('\n')))
    seeds=[int(i) for i in data[0].split() if i!="seeds:"]
    seeds=[(seeds[i],seeds[i]+seeds[i+1]) for i in range(0,len(seeds),2)]
    data=data[1:]+["foo bar"]
    M=[]
    for row in data:
        numbers=row.split()
        if len(numbers)==2:
            if M:
                new = []
                while len(seeds) > 0:
                    s, e = seeds.pop()
                    for a, b, c in M:
                        os = max(s, b)
                        oe = min(e, b + c)
                        if os < oe:
                            new.append((os - b + a, oe - b + a))
                            if os > s:
                                seeds.append((s, os))
                            if e > oe:
                                seeds.append((oe, e))
                            break
                    else:
                        new.append((s, e))
                seeds = new
            M=[]
        else:
            M+=[list(map(int,numbers))]
    print(min(seeds))
    return


if __name__ == "__main__":

    part2()

