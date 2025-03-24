#range function 
range(1,11)
#numbers generated only from 1to10
print(list(range(1,11)))
#range(start,stop,step)
print(list(range(10,0,-2)))
#sequence
for i in range(10,0,-2):
    print(i)

for i in "kolkata":
    print(i)    

#nested loops 
rows = int(input("enter number of rows: "))
for i in range(1, rows+1):
    for j in range(0,i):
        print("*", end =" ")
    print("")
    #use pyhtontutor.com to see step by step execution 

