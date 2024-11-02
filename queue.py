#QUEUE
s=[]
c="y"
while (c=="y"):
    print("1. PUSH")
    print("2. POP")    	
    print("3. Display")   
    choice=int(input("enter your choice:  "))    
    if (choice==1):
        a=input("Enter any number :")
        s.append(a)    
    elif (choice==2):
        if (s==[]):
            print("QUEUE empty")
        else:
            print("Deleted element is : ",s.pop())   
    elif(choice==3):
        l=len(s)
        for i in range(0,l):
            print (s[i])  
    else:
        print("Wrong input")
        c=input("Do you want to continue or not? ")
