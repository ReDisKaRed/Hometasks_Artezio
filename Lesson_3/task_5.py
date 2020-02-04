def f(a):
    d=[]
    s=[]
    for i in a.split():
        s.append(float(i))
        d.append(abs(float(i)))
    return s[d.index(min(d))]
p=input()
print(f(p))





