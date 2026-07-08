
y=input("enter:")
z=y[::-1]
if(y==z):
    print('True')
else:
    print('False')
    

# using function
def my_pal(x):
    if x==x[::-1]:
        return True
    else:
        return False
print(my_pal("good"))
print(my_pal("malayalam"))