import sys

def my_max(lst):
    max_num = 0
    for num in lst:
        print(num, max_num)
        sys.exit()
        if num > max_num:
            max_num = num
    return num

print(my_max([-1,-2,-4]))


