

def int2bit_recursive_function(num):
    if num == 0:
        return ""
    return int2bit_recursive_function(num // 2) + str(num % 2)

def get_bits(integer, format_str, delimiter):
    print '\nrecursive function:'
    return delimiter.join( ( [format_str.format((recursive_function(i))) for i in range(integer)] ) )
    

def int2bit_range_lambda_recursion(integer, format_str, delimiter):
    print '\nrecursive lambda:'
    f = (lambda a, num: "" if num==0 else a(a, num//2) + str(num%2))
    return delimiter.join( ( [format_str.format(f(f,p)) for p in range(integer)] ) )


def int2bit_xrange_lambda_recursion(integer, format_str, delimiter):
    print '\nrecursive lambda xrange:'
    f = (lambda a, num: "" if num==0 else a(a, num//2) + str(num%2))
    return delimiter.join( ( [format_str.format(f(f,p)) for p in xrange(integer)] ) )

    
def int2bit_range_lambda_recursion_pkg():
    """This function changes an integer into bit"""
    integer = 14
    bits = 4
    format_str = "{0:0>%d}" % bits
    delimiter = ","
    f = (lambda a, num: "" if num==0 else a(a, num//2) + str(num%2))
    return delimiter.join( ( [format_str.format(f(f,p)) for p in range(integer)] ) )

def different_runs():

    print '\nAdditional int2binary trails:'
    integer = 1024
    bits = 8
    format_str = "{0:0>%d}" % bits
    delimiter = "," # "\n"

    git_bits(integer, format_str, delimiter)

    int2bit_range_lambda_recursion(integer, format_str, delimiter)
    int2bit_xrange_lambda_recursion(integer, format_str, delimiter)
    

if __name__ == "__main__":
    int2bit_range_lambda_recursion_pkg()

    different_runs()



