def repl(inp):
    a=[("one","on1ne"),("two","tw2o"),("three","th3ree"),("four","fo4ur"),("five","fi5ve"),("six","si6x"),("seven","se7ven"),("eight","eig8ht"),("nine","ni9ne")]
    print(inp)
    for x,y in a:
        inp=inp.replace(x,y)
    print(inp)
    return inp

def main():
    with open('input.txt') as f:
        data=f.read().split('\n')
    sum=0
    problem=2
    for i in data:
        if problem==2:
            f=repl(i)
        try:
            x=[int(j) for j in f if j.isdigit()]
            sum+=10*x[0]+x[-1]
        except:
            pass
        print(sum)
    print(sum)

if __name__ == "__main__":
    main()
