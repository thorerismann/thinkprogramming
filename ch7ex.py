#ch7exercises

import sys

#7.1
def count_odd(x):
    count = 0
    for i in x:
        if(i%2==1):
            count +=1
    return count
#7.2
def count_even(x):
    count = 0
    for i in x:
        if(i%2==0):
            count += 1
    return count
#7.3
def sum_neg(x):
    subtotal = 0
    for i in x:
        if(i<0):
            subtotal += i
    return -subtotal
#7.4
def word_length(x):
    count = 0
    for i in x:
        if (len(i)==5):
            count += 1
    return count

#7.5
def sum_odd(x):
    subtotal = 0
    for i in x:
        if (i%2 == 0):
            return subtotal
        subtotal += i
    return subtotal

#7.6
def to_sam(x):
    count = 0
    for i in x:
        if(i == "sam"):
            return count
        count += 1
    return count

#7.7
def sqrt(n):
    approx = n/2.0     # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        if abs(approx - better) < 0.001:
            return better
        approx = better
        print("better")

#7.9
def print_triangular_numbers(n):
    count = 0
    total = 0
    for i in range(n):
        count += 1
        total = total + count
        print(total)
    return

