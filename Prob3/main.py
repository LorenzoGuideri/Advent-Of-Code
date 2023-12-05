def part1():
    with open('input.txt') as f:
        data=list(filter(None,f.read().split('\n')))
    sum=0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x]!='.' and not data[y][x].isnumeric():
                neig=[(y+j,x+i) for j,i in [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]]
                for j,i in neig:
                    if data[j][i].isnumeric():
                        l,r=i,i
                        while l>0 and data[j][l-1].isnumeric():
                            l-=1
                        while r+1<len(data[0]) and data[j][r+1].isnumeric():
                            r+=1
                        sum+=int(data[j][l:r+1])
                        print(data[j])
                        data[j]=data[j][:l]+"."*(r-l+1)+data[j][r+1:]
                        print(data[j])


    print(sum)

def part2():
    with open('input.txt') as f:
        data=list(filter(None,f.read().split('\n')))
    sum=0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x]=="*":
                ratio=1
                wheels=0
                neig=[(y+j,x+i) for j,i in [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]]
                for j,i in neig:
                    if data[j][i].isnumeric():
                        l,r=i,i
                        while l>0 and data[j][l-1].isnumeric():
                            l-=1
                        while r+1<len(data[0]) and data[j][r+1].isnumeric():
                            r+=1

                        ratio*=int(data[j][l:r+1])
                        wheels+=1
                        print(data[j])
                        data[j]=data[j][:l]+"."*(r-l+1)+data[j][r+1:]
                        print(data[j])
                if wheels==2:
                    sum+=ratio


    print(sum)

if __name__ == "__main__":
    part2()

