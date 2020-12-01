# --- Day 1: Report Repair ---

f = open('input.txt')
known = [1721, 979, 366, 299, 675, 1456]
comparisons = 0

def int_array(arr):
    temp = []
    for i in arr:
        temp.append(int(i))
    return temp

def compare_all(i, arr):
    for n in arr:
        if n + i == 2020:
            return n * i

def brute_force(arr):
    for i in arr:
        result = compare_all(i, arr)
        if result:
            return result

lines = f.readlines()
numbers = int_array(lines)
print(brute_force(numbers))