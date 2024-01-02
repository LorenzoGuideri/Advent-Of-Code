#!/usr/bin/env python3
from math import lcm
class node:
  def __init__(self, name):
    self.name = name
    self.l= None
    self.r= None

def binary_search(arr,start,end,target):
    mid = (start+end)//2
    if start > end:
        return -1
    if arr[mid].name < target:
        return binary_search(arr, mid+1, end, target)
    elif arr[mid].name > target:
        return binary_search(arr, start, mid-1, target)
    elif arr[mid].name == target:
        return arr[mid]

def part1():
    with open('input.txt') as f:
        path,data=list(filter(None,f.read().split('\n\n')))
    data=sorted(data.split('\n'))[1:]
    nodes=[node(i[:3]) for i in data]
    for i in range(len(data)):
        nodes[i].l=binary_search(nodes,0,len(nodes)-1,data[i][7:10])
        nodes[i].r=binary_search(nodes,0,len(nodes)-1,data[i][12:15])
    length=0
    now=nodes[0]
    while length<1000000:
        if now.name=="ZZZ": break
        if path[length%len(path)] == 'R': now=now.r
        else: now=now.l
        length+=1
    print(length)
    return

def part2():
    sos=[]
    with open('input.txt') as f:
        path,data=list(filter(None,f.read().split('\n\n')))
    data=sorted(data.split('\n'))[1:]
    nodes=[node(i[:3]) for i in data]
    for i in range(len(data)):
        nodes[i].l=binary_search(nodes,0,len(nodes)-1,data[i][7:10])
        nodes[i].r=binary_search(nodes,0,len(nodes)-1,data[i][12:15])
    for i in nodes:
        if i.name[2]=='A':
            length=0
            now=i
            while length<1000000:
                if now.name[2]=="Z": break
                if path[length%len(path)] == 'R': now=now.r
                else: now=now.l
                length+=1
            sos.append(length)
    lol=1 
    for ii in sos:
        lol=lcm(lol,ii)
    print(lol)
    return

if __name__ == "__main__":
    part1()
    part2()

