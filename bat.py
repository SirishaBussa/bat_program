patients_escaped=int(input('enter no.of patients escaped: '))
steps=int(input('enter the step where batman started: '))
'''
3 patients 5 steps then
1 patient 5 steps
 then 2 patient 10 steps
 third patient 5*3=15 (5+10+15=30)

 4 steps 4 patients then
 1=4
 2=8
 3=12
 4=16

 3 pat , 10 steps
 1=10
 2=20
 2=30

 if all those steps are to be added then,
def findnumofsteps(n,m):
    sum=0
    for i in range(1,n+1,1):
        sum=sum+(i*m)
    return sum

u=findnumofsteps(patients_escaped,steps)
print(u)
'''
def findNumOfstepsRequired(n,m):
    return n*m
      
p=findNumOfstepsRequired(patients_escaped,steps)
print('the steps required= ',p)
    
