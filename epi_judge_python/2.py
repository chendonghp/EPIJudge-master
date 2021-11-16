#in place
def bubble(alist):
    for end in range(len(alist)-1,0,-1):
        for i in range(end):
            if alist[i]>alist[i+1]:
                alist[i], alist[i+1] = alist[i+1],alist[i]

#inplace
def selection(alist):
    for i in range(len(alist)-1):
        _min,_min_index=alist[i],i
        for j in range(i+1,len(alist)):
            if alist[j]<alist[_min_index]:
                _min_index=j
        alist[i],a[_min_index]=a[_min_index],a[i]

#space complexity
def insertion(alist):
    _len=len(alist)
    i=1
    while i<_len:
        insert_value=alist[i]
        j=i-1
        while j>=0:
            #insertion
            if alist[j]>insert_value:
                alist[j+1]=alist[j]
            else:
                alist[j+1]=insert_value
                break
            j-=1
        if j==-1:
            alist[j+1]=insert_value
        i+=1

def runtime(funcs,arguments):
    import time
    import random
    random.shuffle(arguments)
    # print(arguments,'\n')
    for func in funcs:
        s=time.process_time()
        func(arguments.copy())
        e=time.process_time()
        print(f'{func.__name__} sort running time is : {e-s}s.')


# x = list(range(2 ** 12))
# funcs=[bubble,selection,insertion]
# runtime(funcs,x)
a=[5,6,7,4,3,2,1]
insertion(a)
print(a)
