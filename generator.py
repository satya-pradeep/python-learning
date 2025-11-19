def count_up_to(n):
    i=1
    while i <=n:
        yield i
        i+=1
for i in count_up_to(5):
    print(i)


def timer(m):
    if m<=0:
        print("done")
    else:
        print(m)
        return timer(m-1)
timer(5)
