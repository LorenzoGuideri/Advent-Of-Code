'''
def main():
    with open('input.txt') as f:
        data=[i for i in f.read().split('\n') if i]
    tot=0
    for i in data:
        a,b=i.split()
        if b=='X': #rock
            tot+=1
            if a=="A": #rock
                tot+=3 
            elif a=="C": #scissor
                tot+=6

        elif b=='Y': #paper
            tot+=2
            if a=="A": #rock
                tot+=6
            elif a=="B": #paper
                tot+=3
            
        else: #scissor
            tot+=3
            if a=="B": #paper
                tot+=6
            elif a=="C": #scissor
                tot+=3
    print(tot)
'''
def main():
    with open('input.txt') as f:
        data=[i for i in f.read().split('\n') if i]
    tot=0
    for i in data:
        a,b=i.split()
        if b=='X': #lose
            if a=="A": #rock
                tot+=3 
            elif a=="B": #paper
                tot+=1
            else: #scissor
                tot+=2

        elif b=='Y': #draw
            tot+=3
            if a=="A": #rock
                tot+=1
            elif a=="B": #paper
                tot+=2
            else:
                tot+=3
            
        else: #win
            tot+=6
            if a=="B": #paper
                tot+=3
            elif a=="C": #scissor
                tot+=1 
            else:
                tot+=2
    print(tot)

if __name__ == "__main__":
    main()
