#max number without using .max()
def max(*n):
    if len(n)== 0:
        return None
    m=n[0]
    for i in n:
        if i > m:
            m=i
    print(m)
max(2,6,3,7,4,756,234,75,35,7)

#min number
def min_n(*numbers):
    if len(numbers)==0:
        return None
    min=numbers[0]
    for i in numbers:
        if i < min:
            min=i
    return min
print(min_n(2,6,3,7,4,756,234,75,35,7))
