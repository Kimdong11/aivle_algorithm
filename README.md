
# Q3 

### 삽입정렬로 오름차순 정렬(List a), 선택정렬로 내림차순 정렬해(List b) 
### 서로 같은 인덱스끼리 k번 만큼 교환 했습니다!


```
def solution(k, a, b):
    answer = 0
    n1 = len(a)
    n2 = len(b)
#삽입정렬 (오름차순)
    for i in range(1, n1) :
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp :
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp 
        
#선택정렬 (내림차순)
    for i in range(n2 - 1) :
        max = i
        for j in range(i  + 1, n2) :
            if b[j] > b[max] :
                max = j
        b[i] , b[max] = b[max], b[i]
        
    for i in range(k) :
        a[i], b[i] = b[i], a[i]
    
    answer = sum(a)
    return answer

```