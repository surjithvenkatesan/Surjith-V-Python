#square pattern

n=5
for i in range(n):
    for j in range(n):
        print(i, end=" ")
    print()
for i in range(n):
    for j in range(n):
        print(j, end=" ")
    print()

    
#hollow square pattern

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# + pattern

for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2:
            print("$", end=" ")
        else:
            print(" ", end=" ")
    print()

#cross pattern


for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("8",end=' ')
        else:
            print(' ',end=' ')
    print()
    

#APPLE cross

u="apple"
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print(u[i],end=" ")
        else:
            print(" ",end=" ")
    print()


#apple" +" pattern

for i in range(n):
    for j in range(n):
        if i==n//2 :
            print(u[j],end=" ")
        elif j==n//2:
            print(u[i],end=" ")
        else:
            print(" ",end=" ")
    print()  


#down triangle

for i in range(n+1):
    for j in range(n):
        if i==0 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(n+1):
        if i==0 or i+j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()











    
