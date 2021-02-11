
# Part - 1

# Python program to print all prime numbers between given two input values
# Prime Number Generator
# Using Sieve of Eratosthenes algorithm

# math module for using sqrt() method
import math

# Input two values start and end 
start,end = input().split(' ')

start = int(start)
end = int(end)

# maintain a temporary list
temp = [True]*(end + 1)

# 0 and 1 are not prime so marking them False
temp[0] = False
temp[1] = False

# Check all the values from 2 to sqrt(end) and
# mark every multiple of them False
# Note that we are considering values only from i*i upto end
for i in range(2,int(math.sqrt(end)+1)):
    if temp[i] != False:
        for j in range(i*i,end+1,i):
            temp[j] = False
            
# Finally Print the values from start to end if they are True
for i in range(start,end+1):
    if temp[i] == True:
        print(i,end=' ')
