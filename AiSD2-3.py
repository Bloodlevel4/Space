def binary_search(arr,key,start,end):
    arr=arr
    key=key
    start=start
    end=end
    avr=(start+end)//2
    if start>end:
        return -start-1
    if arr[avr]==key:
        return avr
    elif arr[avr]>key:
        return binary_search(arr,key,start,avr-1)
    else:
        return binary_search(arr,key,avr+1,end)

def swap(x,old,new):
    x=x
    var=x.pop(old)
    x.insert(new,var)
    return x

def sort(x): #сортировка вставками из презентации
    n=len(x)
    for i in range(1,n):
        j=i
        while x[j-1]>x[j] and j>0:
            swap(x,j-1,j)
            j-=1
    return x
#с двоичным поиском
def sort2(x):
    x=x
    n=len(x)
    for i in range(1,n):
        pos=binary_search(x,x[i],0,i-1)
        if pos<0:
            pos=(binary_search(x,x[i],0,i-1)+1)*(-1)
            x=swap(x,i,pos)
        else: 
            x=swap(x,i,pos)
    return x

x=[4,1,30,6,8,2,30,2,1]
x2=[1,4,6,8,30,2,1]
y=[2,4,6]
print((binary_search(x2,6,0,1)+1)*(-1))
#print(swap(y,0,1))
print(x)
print(sort(x))
print(sort2(x))
