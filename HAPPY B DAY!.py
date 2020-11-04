def print_fib(n):
    happy = 'happy'
    birthday = 'birthday'
    dad = 'dad'
    hope = 'i'
    you = 'hope'
    u = 'you'
    h = 'have'
    t = 'the'
    b = 'best'
    bi = 'birthday'
    e = 'ever'
    th = 'thank you for '
    ta = 'taking care of us'
    an = 'and working really hard'
    to = 'to saticfy what i need and want'
    al = 'also to send me to the wonderful school and make me live in the best condo'
    ald = 'and giving me all the love i need '
    i = 'i hope we can meet soon and celebrate together'
    ih = 'and please do not forget how much i miss you!'
    ha = 'HAPPY BIRTHDAY!!!'


    print(happy)
    print(birthday)
    print(dad)
    print(hope)
    print(you)
    print(u)
    print(h)
    print(t)
    print(b)
    print(bi)
    print(e)
    print(th)
    print(ta)
    print(an)
    print(to)
    print(al)
    print(ald)
    print(i)
    print(ih)
    print(ha)
    for i in range(n-1):
        dad = happy + birthday
        print(dad)
        happy=birthday
        birthday=dad
        dad=hope
        hope=you
        you=u
        u=h
        h=t
        t=b
        b=bi
        bi=e
        e=th
        th=ta
        ta=an
        an=to
        to=al
        al = ald
        ald =i
        i=ih
        ih=ha

print_fib(1)