a = [1, 3, 6, 9, 13, 47]
b = [2, 4, 8, 24, 52]

# Classic way
# 1. Merge the two arrays
c = a + b
print(c)
# 2. Sort the merged array
c.sort()
print(c)

# Using the sorted() function
# 1. Merge the two arrays
c = a + b
print(c)
# 2. Sort the merged array
c = sorted(c)
print(c)

# Using the sorted() function with a lambda function
# 1. Merge the two arrays
c = a + b
print(c)
# 2. Sort the merged array
c = sorted(c, key=lambda x: x)
print(c)

# using while loop in a function that has two arrays as parameters
def merge_and_sort(a, b):
    while b:
        a.append(b.pop())
    return sorted(a)

print("Using the while loop", merge_and_sort(a, b))
