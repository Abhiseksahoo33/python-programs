k=1
z=0
for i in range(4):
    k=i+1
    for j in range(4-i):
        print(k ,end="  ")
        k+=1

    print()


#1  2  3  4
#2  3  4
#3  4
#4
