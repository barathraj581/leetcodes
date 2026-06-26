x=[2,7,11,15]
target=9
def two_sum(x,target):
    y=len(x)
    for i in range(y):
        for j in range(i+1,y):
            if x[i]+x[j] == target:
                return [i,j]
print(two_sum(x,target))
