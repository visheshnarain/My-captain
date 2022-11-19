n= int(input("number of terms: "))
n1,n2=0,1
count=0
if n<=0:
   print ("Please print a positive integer")
else:
    print ("Fibonacci sequence:")
    while count<n :
        print (n1)
        nth= n1 + n2
        n1=n2
        n2=nth        
        count +=1
        
        
