
def minimumDifferenence(arr,i,sumCalculated,sumTotal):
    if (i==0): 
        return abs((sumTotal-sumCalculated) - sumCalculated); 
  
    return min(minimumDifferenence(arr, i-1, sumCalculated+arr[i-1], sumTotal),minimumDifferenence(arr, i-1, sumCalculated, sumTotal))


arr=[3, 1, 4, 2, 2, 1]
print(minimumDifferenence(arr,len(arr)-1,0,sum(arr)))