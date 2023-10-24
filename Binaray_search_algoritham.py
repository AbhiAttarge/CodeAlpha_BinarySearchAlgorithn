# Code Alpha Python Programing
# TASK 02
# Binary Search Algoritham

# Take user input 
start = int(input("Enter the start of range : "))
end = int(input("Enter the end of range : "))

if start / 2 != 0:
    for num in range(start, end + 1,2):
        print(num, end=" ")
else:
    for num in range(start+1, end + 1, 2):
        print(num, end=" ")