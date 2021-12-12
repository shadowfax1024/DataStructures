def max_heapify(A,i):
    print("----IN MAX HEAPIFY---",A,i)
    length = len(A)
    left = 2*i + 1
    right = 2*i + 2
    print("left_right",left,right)
    largest = -10000
    if ((left <length) and (A[left] > A[i])):
        largest= left
    else:
        largest = i
    if((right <length) and (A[right] > A[largest])):
        largest = right
    if(largest != i):
        p,q = A[i],A[largest]
        A[i] = q
        A[largest] = p
        max_heapify(A,largest)
    return A
def max_heapify2(A,i,length):
    print("----IN MAX HEAPIFY---",A,i)
    #length = len(A)
    left = 2*i + 1
    right = 2*i + 2
    print("left_right",left,right)
    largest = -10000
    if ((left <length) and (A[left] > A[i])):
        largest= left
    else:
        largest = i
    if((right <length) and (A[right] > A[largest])):
        largest = right
    if(largest != i):
        p,q = A[i],A[largest]
        A[i] = q
        A[largest] = p
        max_heapify(A,largest)
   

A = [16,4,10,14,7,9,3,2,8,1,17]
print("------PREVIOUS----",A)
for i in range(len(A)//2,-1,-1):
    print("in LOOP",i)
    max_heapify(A,i)
print("------AFTER----",A)
print("---NOW TO SORTING----")
length = len(A)
sorted = []
for i in range(1,len(A),1):
    print("in SORTING",i,A[0],A[-i])
    print("BEFORE SWAP",A)
    p,q = A[0],A[-i]
    A[0]= q
    A[-i] =p
    print("AFTER SWAP",A)
    length -=1
    A[:-i] = max_heapify(A[:-i],0)
print("---DONE SORTING----",A)