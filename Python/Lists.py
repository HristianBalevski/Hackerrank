# Consider a list (list = []). You can perform the following commands:
# 1. insert i e: Insert integer  at position.
# 2. print: Print the list.
# 3. remove e: Delete the first occurrence of integer e.
# 4. append e: Insert integer e at the end of the list.
# 5. sort: Sort the list.
# 6. pop: Pop the last element from the list.
# 7. reverse: Reverse the list.

# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. 
# Iterate through each command in order and perform the corresponding operation on your list.

# Input Format
# The first line contains an integer,n, denoting the number of commands. 
# Each line  of the  subsequent lines contains one of the commands described above.

# Constraints
# The elements added to the list must be integers.

# Output Format
# For each command of type print, print the list on a new line.

# Sample Input 0
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# Sample Output 0
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

N = int(input())
arr = []

for i in range(N):
    data = input().split(' ')

    if data[0] == 'insert':
        index = int(data[1])
        value = int(data[2])
        arr.insert(index, value)
    elif data[0] == 'print':
        print(arr)
    elif data[0] == 'remove':
        index = int(data[1])
        if index in arr:
            arr.remove(index)
    elif data[0] == 'append':
        value = int(data[1])
        arr.append(value)
    elif data[0] == 'sort':
        arr.sort()
    elif data[0] == 'pop':
        arr.pop(-1)
    elif data[0] == 'reverse':
        arr.reverse()
