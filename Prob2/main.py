def main():
    with open('input.txt') as f:
        data=list(filter(None,f.read().split('\n')))
    sum=0
    problem=2
    limits={
        'red':12,
        'green':13,
        'blue':14
    }
    for row in data:
        id,plays=row.replace(";",",").replace("Game ","").split(":")
        shouldAdd=1
        maxi={'red':0, 'green':0, 'blue':0}
        for record in plays.split(", "):
            cubes,color=record.split()
            if problem==1 and int(cubes)>limits[color]:
                shouldAdd=0
            if problem==2:
                maxi[color]=max(maxi[color],int(cubes))
        if problem==1:
            sum+=int(id)*shouldAdd
        else:
            sum+=maxi['red']*maxi['blue']*maxi['green']
    print(sum)

if __name__ == "__main__":
    main()
