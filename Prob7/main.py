#!/usr/bin/env python3

def pokersort(e):
    o={}
    s=list(e[0].replace('A','Z').replace('T','B').replace('K','R'))
    for i in s: 
        if i not in o:
            o[i]=1 
        else:
            o[i]+=1 
    c=sorted(o.values(), reverse=True)
    if c[0]>3: res= c[0]+1 
    elif c[1]==2: res= 4 if c[0]==3 else 2
    elif c[0]==3: res= 3
    else: res= c[0]-1
    return str(res)+''.join(s)

def pokersort2(e):
    o={}
    js=0
    s=list(e[0].replace('A','Z').replace('T','B').replace('K','R').replace('J','1'))
    for i in s:
        if i=='1':
            js+=1
        elif i not in o:
            o[i]=1 
        else:
            o[i]+=1
    c=sorted(o.values(), reverse=True)
    if js:
        if js==5:
            return '611111'
        c[0]+=js
    if c[0]>3: res= c[0]+1 
    elif c[1]==2: res= 4 if c[0]==3 else 2
    elif c[0]==3: res= 3
    else: res= c[0]-1
    return str(res)+''.join(s)

def part1():
    with open('./input.txt') as f:
        data=[i.split() for i in list(filter(None,f.read().split('\n')))]
    data.sort(key=pokersort)
    sum=0
    for i in range(len(data)):
        sum+=int(data[i][1])*(i+1)
    print(sum)
    return

def part2():
    with open('./input.txt') as f:
        data=[i.split() for i in list(filter(None,f.read().split('\n')))]
    data.sort(key=pokersort2)
    sum=0
    for i in range(len(data)):
        sum+=int(data[i][1])*(i+1)
    print(sum)
    return

if __name__ == "__main__":
    part2()

