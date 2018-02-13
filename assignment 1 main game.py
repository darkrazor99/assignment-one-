list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
win=[]
stop=1
turn=1
end=10
print("Welcome to the two squares game ")
print("Do you want to see the rules?")
print("")
o=int(input("enter 1 to see the rules and 2 to skip the rules:\n"))
rules=0
while rules==0:
    if o==1  :
        print("Imagine a board of 4x4 squares represented by the numbers 1 through 16\n")
        print("players take turns choosing two numbers entering  representing a rectangle\n")
        print("A number that has been choosen can't be choosen again\n ")
        print("the last player to enter a rectangle wins\n")
        print("please make sure to enter the smallest number first\n")
        rules=1
        break
    elif o==2:
        break

    if o!=1 or o!=2:
        print("wrong value try again")
        o=int(input("enter 1 to see the rules and 2 to skip the rules:\n"))
    
        
while end==10:
    if stop==0:
        break
    while turn ==1:
        print ("player one")
        print("remaining numbers:",list)
        a=int(input("enter your first/smallest number :"))
        b=int(input("enter your second/biggest number:"))
        for i in list :
            if (i==a):
                if (a%4==0) and (b-a==4): # condition for input to be accepted
                    print(a,b)
                    list.remove(a)
                    list.remove(b)
                    turn=2
                    you_win=0
                    break
                elif (a%4!=0) and (b==a+1) or (b-a==4):
                    print(a,b)
                    list.remove(a)
                    list.remove(b)
                    turn=2
                    you_win=0
                    break
                else:
                    print("invalid try again ")
                    break
            elif(i!=a):
                print("invalid try again")
                break




 
        if list==win:
            print("player one wins")
            stop=0
            break
        for m in list:
            for v in list[1:]:
                if (v-m==1 ) or (v-m==4):
                    you_win=1
                    break
        if you_win==0:
            print("player one wins")
            stop=0
         
    while turn==2:
        if stop==0 :
            break
        print("player two")
        print("remaining numbers:",list)
        c=int(input("enter your first number/smallest :"))
        d=int(input("enter your second number/biggest:"))
        for n in list:
            if n==c:
                if (c%4==0) and (d-c==4):
                    print(c,d)
                    list.remove(c)
                    list.remove(d)
                    turn=1
                    you_win=0
                    break
                elif (c%4!=0) and (d==c+1)or(d-c==4):
                    print(c,d)
                    list.remove(c)
                    list.remove(d)
                    turn=1
                    you_win=0
                    break
                else:
                    print ("invalid")
                    break
            elif(n!=c):
                print("invalid try again")
                break
     
        if list==win :
            print ("player two wins")
            stop=0
            break
        for m in list:
            for v in list[1:]:
                if (v-m==1 ) or (v-m==4):
                    you_win=1
                    break
        if you_win==0:
            print("player two wins")
            stop=0
