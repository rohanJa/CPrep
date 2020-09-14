def sumOfSubset(arr,sum,i):
    if(sum==0):                 #check the sum is zero if zero then subset found
        return True

    # Think about the above conditions
    if(i==len(arr)):            #if gone uptil last element 
        return False
    elif(sum!=0 and i==len(arr)):
        return False

    return (sumOfSubset(arr,sum-arr[i],i+1) or sumOfSubset(arr,sum,i+1)) 


arr=[1,5,3,4,2]
cap=7
print(sumOfSubset(arr,cap,0))