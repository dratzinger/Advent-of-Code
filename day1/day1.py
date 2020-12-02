# --- Day 1: Report Repair ---

f = open('input.txt')
known = [1721, 979, 366, 299, 675, 1456]
lines = f.readlines()

def int_array(arr):
    temp = []
    for i in arr:
        temp.append(int(i))
    return temp

numbers = int_array(lines)

# --- Part One ---
def compare_all(i, arr):
    for n in arr:
        if n + i == 2020:
            return n * i

def brute_force(arr):
    for i in arr:
        result = compare_all(i, arr)
        if result:
            return result

print(brute_force(numbers))

#--- Part Two ---
def compare_three(i, arr):
    for n in arr:
        for m in arr:
            if n + m + i == 2020:
                return n * m * i

def brute_force_three(arr):
    for i in arr:
        result = compare_three(i, arr)
        if result:
            return result

print(brute_force_three(numbers))