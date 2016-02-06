

def lambda_fib():
    print '\nfib:'
    hops = 2
    f = (lambda a, b: a(b-1) + a(b-2) if b > 1 else b)
    print [ (f(f,hops)) ]


if __name__ == "__main__":
    lambda_fib()
