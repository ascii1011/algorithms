qsort = lambda x=None, *xs: [97, 200, 100, 101, 211, 107] if x is None else qsort(*[a for a in xs if a<x]) + [x] + qsort(*[a for a in xs if a>=x])

print qsort
