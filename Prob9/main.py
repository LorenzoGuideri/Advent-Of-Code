#!/usr/bin/env python3

def part1():
    with open('input.txt') as f:
        data=list(filter(None,f.read().split('\n')))
    sum=0
    for i in data:
        nums,depth,go=[],0,True
        nums.append(i.split())
        while go:
            temps=[]
            for ii in range(len(nums[depth])-1):
                temps.append(int(nums[depth][ii+1])-int(nums[depth][ii]))
            depth+=1
            if temps==[0]*len(temps): go=False
            nums.append(temps)
        for ii in nums:
            sum+=int(ii[-1])
        # print(nums)
    print(sum)
    return

def part2():
    with open('input.txt') as f:
        data=list(filter(None,f.read().split('\n')))
    sum=0
    for i in data:
        nums,depth,go=[],0,True
        nums.append(i.split())
        while go:
            temps=[]
            for ii in range(len(nums[depth])-1):
                temps.append(int(nums[depth][ii+1])-int(nums[depth][ii]))
            depth+=1
            if temps==[0]*len(temps): go=False
            nums.append(temps)
        for ii in range(len(nums)):
            sum+=int(nums[ii][0])*((-1)**(ii%2))
    print(sum)
    return
if __name__ == "__main__":
    part2()

