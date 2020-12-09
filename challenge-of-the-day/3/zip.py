def zipped(a,b):
    if len(a)!=len(b):
        return "these strings are different lengths!"
    else:
        a1=list(a)
        b1=list(b)
        c = [i + j for i, j in zip(a1, b1)]
        space=""
        d=space.join(c)
        return d
