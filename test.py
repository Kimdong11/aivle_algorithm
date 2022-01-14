# selection_sort

def selection_sort(a) :
    n = len(a)
    
    for i in range(n) :
        min = i
        for j in range(i + 1, n) :
            if a[j] < a[min] :
                min = j
            a[min], a[i] = a[i], a[min]
            
          
            


def inseration_sort(a) :
    n = len(a)
    for i in range(1, n) :
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] < tmp :
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

x = [9, 8, 7, 6, 5, 4, 3, 2, 1]  
selection_sort(x)
print(x)