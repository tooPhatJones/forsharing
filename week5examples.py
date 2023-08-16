




# class examples binary search{{{
def binary_search(the_list, target):
    lower_bound = 0
    upper_bound = len(the_list) - 1

    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = the_list[pivot]

        if pivot_value == target:
            return pivot
        if pivot_value > target:
            upper_bound = pivot - 1
        else:
            lower_bound = pivot + 1

    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(my_list, 10))
print(binary_search(my_list, 4))
print(binary_search(my_list, 33))


# }}}
# bubblesort class example{{{
unsorted_list = [101, 49, 3, 12, 56]


def bubblesort(the_list):
    high_idx = len(the_list) - 1

    for i in range(high_idx):
        list_changed = False
        for j in range(high_idx):
            item = the_list[j]
            next = the_list[j+1]

            if item > next:
                the_list[j] = next
                the_list[j+1] = item
                list_changed = True

            print(the_list, i, j)
        print(list_changed)
        if list_changed == False:
            break


bubblesort(unsorted_list)
# }}}
# linear search class example{{{
def linear_search(the_list, target):
    for x in range(len(the_list)):
        if the_list[x] == target:
            print("Found at index", x)
            return x
    print("Target is not in the list")
    return -1


my_list = [6, 3, 4, 2, 5, 7]
linear_search(my_list, 5)
linear_search(my_list, 3)
linear_search(my_list, 8)
# }}}
# quicksort class example{{{
my_list = [5, 4, 1, 2, 3]


def sort_part(the_list, low_idx, pivot_idx):
    pivot_val = the_list[pivot_idx]

    while pivot_idx != low_idx:
        low_val = the_list[low_idx]

        print(the_list, low_val, pivot_val)
        if low_val <= pivot_val:
            low_idx += 1
        else:
            the_list[low_idx] = the_list[pivot_idx-1]
            the_list[pivot_idx] = low_val
            the_list[pivot_idx-1] = pivot_val
            pivot_idx -= 1

    return pivot_idx


def quicksort(the_list, low_idx, high_idx):
    if low_idx > high_idx:
        return

    pivot_idx = sort_part(the_list, low_idx, high_idx)
    quicksort(the_list, low_idx, pivot_idx-1)
    quicksort(the_list, pivot_idx+1, high_idx)


quicksort(my_list, 0, len(my_list)-1)
print("my_list:", my_list)
# }}}
# class example constant time{{{
def const(n):
    if n < 100:
        return True
    else:
        return False
# }}}
# class example linearsearch.py{{{
mylist = [59, 76, 60, 13, 11, 83, 48, 52, 54, 41, 97, 76, 33, 9, 67]
findval = 41
cnt = 0
for item in mylist:
    cnt += 1
    if item == findval:
        print('Found', findval, 'in', cnt, 'steps')
        break
# }}}
# class example linear time{{{
def sumall(n):
    tot = 0
    for i in range(1, n):
        tot += i
    return tot

# }}}
# logarithmic time class example{{{
from random import randint


def bin_search(l, val):
    start = 0
    end = len(l)-1
    match = False
    cnt = 0

    while start <= end and not match:
        cnt += 1
        middle = (start+end)//2
        if l[middle] == val:
            match = True
        else:
            if val < l[middle]:
                end = middle-1
            else:
                start = middle+1
    return match, cnt


for i in range(10):
    # make a random list of integers using a sorted list comprehension
    listsize = 100000
    randlist = [randint(1, listsize) for n in range(listsize)]
    randlist.sort()
    print('Random List of', listsize)
    # print(randlist)

    # pick a random value and then try to find it in the list
    pickval = randlist[randint(0, listsize-1)]
    found, cnt = bin_search(randlist, pickval)
    print(
        f'Searching {cnt} times I {("found" if found else "did not find")} the value {pickval}')
# }}}
# quadratic time class example{{{
def qtime(n):
    cnt = 0
    for i in range(n):
        for j in range(n):
            cnt += 1
    return cnt


c = qtime(2)
print('Total Operations:', c)
c = qtime(4)
print('Total Operations:', c)
c = qtime(6)
print('Total Operations:', c)
c = qtime(8)
print('Total Operations:', c)
c = qtime(10)
print('Total Operations:', c)
# }}}
