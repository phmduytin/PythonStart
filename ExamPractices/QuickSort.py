def paritition(lst, lo, hi):
    pivot = lst[lo]
    i = lo + 1
    j = hi
    while i <= j:
        if lst[i] <= pivot:
            i += 1
        else:
            if lst[j] < pivot:
                lst[i], lst[j] = lst[j], lst[i]
            else:
                j -= 1
    lst[lo], lst[j] = lst[j], lst[lo]
    return j

def QuickSort(lst, lo, hi):
    if lo < hi:
        mid = paritition(lst, lo, hi)
        QuickSort(lst, lo, mid-1)
        QuickSort(lst, mid+1, hi)

lst = [23, 6, 44, 22, 8, 5, 11, 40, 34, 18]
n = len(lst)

QuickSort(lst, 0, n-1)

print(lst)