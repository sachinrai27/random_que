def sol(a):
    #Sorting the list (Complexity O(nlogn))
    
    a.sort()
    print(a)
    incr=a[0]

    #Iterating over loop to find the next min integer
    for i in range(len(a)):
        if a[i]==incr:
            if i==len(a)-1:
                return 'Next minimum positive integer : '+str(incr+1)
            continue
        elif a[i]==(incr+1):
            incr+=1
            if i==len(a)-1:
                return 'Next minimum positive integer : '+str(incr+1)
        else:
            return 'Next minimum positive integer : '+str(incr+1)        


#Different function calls to check the result.
print(sol([1,3,1,6,2,4,1]))
print(sol([1,0]))
print(sol([-1,-1]))
print(sol([-1,-2]))
print(sol([-1,1,2,0,-2]))
print(sol([1,3]))
print(sol([-35,38]))
