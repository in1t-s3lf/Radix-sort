def Counting_Sort(array, p_v):
    n = len(array) 
    new = [1 for i in range(n)]
    c = [0] * (10)
    for i in range(0, n): 
        index = (array[i]//p_v) 
        c[(index)%10] += 1
    for i in range(1,10): 
        c[i] += c[i-1]
    i = n-1
    while i>=0: 
        index = (array[i]//p_v) 
        new[ c[ (index)%10 ] - 1] = array[i] 
        c[ (index)%10 ] -= 1
        i -= 1
    i = 0
    for i in range(0,len(array)): 
        array[i] = new[i]
def Radix_Sort(array):
    largest_number = max(array) 
    place_value = 1
    while largest_number/place_value > 0: 
        Counting_Sort(array,place_value) 
        place_value *= 10
lim= int(input('set lim:'))
dt = input('').split(' ')
array = list([int(x) for x in dt]) 
Radix_Sort(array)

print(array)
