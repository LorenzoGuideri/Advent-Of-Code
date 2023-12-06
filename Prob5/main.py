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
    s=[int(i) for i in data[0].split() if i!="seeds:"]
    seeds=[]
    for i in range(0,len(s),2):
        seeds+=[i for i in range(s[i],s[i]+s[i+1])]
        
    
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

if __name__ == "__main__":

    part2()

