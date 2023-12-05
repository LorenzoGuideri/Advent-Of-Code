def main():
    with open('input.txt') as f:
        data=f.read().split('\n')
    massi,total=[0,0,0],0
    for i in data:
        if i=='':
            massi=massi+[total]
            massi.sort()
            massi=massi[1:]
            total=0
        else:
            total+=int(i)
    print(sum(massi))
    
if __name__ == "__main__":
    main()
