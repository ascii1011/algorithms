
def partition(array, begin, end):
    pivot = begin
    print '\nP: %d-%d = [%s]' % ( begin, end, str(array) )
    for i in xrange(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    
    print 'pivot:', str(pivot)
    return pivot


def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    if begin >= end:
        return 
    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot-1)
    quicksort(array, pivot+1, end)

    print array

array = [97, 200, 100, 101, 211, 107]
quicksort(array)
# array -> [97, 100, 101, 107, 200, 211]
