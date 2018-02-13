list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
win=[]
stop=1
turn=1
end=10
print("Welcome to the two squares game ")
print("Do you want to see the rules?")
print("")
o=int(input("enter 1 to see the rules and 2 to skip the rules:\n"))
if o==1:
    print(" Imagine a board of 4x4 squares represented by the numbers 1 through 16")
    print("players take turns choosing two numbers entering  representing a rectangle")
    print("A number that has been choosen can't be choosen again ")
    print("the last player to enter a rectangle wins")

print("do you have a friend to play with ?")
print("or do you have no friends ?")
print("enter 1 if you have a friend and want to play with them ")
print("or enter 2 and play with me instead :)")
choice= int(input())
if choice ==1:
 print("please make sure to enter the smallest number first")
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
              elif (a%4!=0) and (b==a+1) or (b-a==4):
                  print(a,b)
                  list.remove(a)
                  list.remove(b)
                  turn=2
                  you_win=0
              else:
                  print("invalid")




 
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
      c=int(input("enter your first number :"))
      d=int(input("enter your second number:"))
      for n in list:
          if n==c:
              if (c%4==0) and (d-c==4):
                  print(c,d)
                  list.remove(c)
                  list.remove(d)
                  turn=1
                  you_win=0
              elif (c%4!=0) and (d==c+1)or(d-c==4):
                  print(c,d)
                  list.remove(c)
                  list.remove(d)
                  turn=1
                  you_win=0
              else:
                  print ("invalid")
     
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
else:
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
                        print("",a,b)
                        list.remove(a)
                        list.remove(b)
                        turn=2
                    elif (a%4!=0) and (b==a+1) or (b-a==4):
                        print("",a,b)
                        list.remove(a)
                        list.remove(b)
                        turn=2
                    else:
                        print("invalid")
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
            if (len(list) == 2) and list[1]-list[0]!=1 and list[1]-list[0]!=4:
                print("player one wins ")
                stop=0
                break
            if list ==[2,3,4,14,15,16]: #some special cases 
                c=3
                d=4
            if list==[1,7,11,12,13,16]:
                c=11
                d=12
            if (a==13)and list !=[1,7,11,12,13,16] and list!=[2,3,4,14,15,16] :
                c=9
                d=10
                check=1
                while check==1:
                    if c not in list or d not in list:
                        c=c-4
                        d=d-4
                        if 1>=c:
                            break
                    else :
                        check=0
            if (a==15)and list !=[1,7,11,12,13,16]:
                c=11
                d=12
                check=1
                while check ==1:
                    if c not in list or d not in list:
                        c=c-4
                        d=d-4
                        if 1>=c :
                            break
                    else:
                        check=0
            if (a==4) and list!=[1,7,11,12,13,16]and list !=[2,3,4,14,15,16]:
                c=3
                d=7
                check=1
                while check==1:
                    if c not in list or d not in list:
                        c=c-1
                        d=d-1
                        if 1>=c:
                            break
                    else:
                        check=0
            if (a==12)and list !=[1,7,11,12,13,16]:
                c=11
                d=15
                check=1
                while check==1:
                    if c not in list or d not in list:
                        c=c-1
                        d=d-1
                        if 1>=c:
                            break
                    else:
                        check=0
            if (b-a==4)and list!=[1,7,11,12,13,16]and list!=[2,3,4,14,15,16]:
                c=a+1
                d=b+1
                check=1
                while check==1:
                    if c not in list or d not in list:
                        c=c+1
                        d=d+1
                        if c>=16:
                            for n in list:
                                for v in list[1:]:
                                    if v-n==4:
                                        c=n
                                        d=v
                                        break
                                    if v-n==1:
                                        c=n
                                        d=v
                                        break
                    else:
                        check=0
            elif (b-a==1)and list!=[1,7,11,12,13,16] and list!=[2,3,4,14,15,16]:
                c=a+4
                d=b+4
                
                check = 1
                while check==1:
                    if c not in list or d not in list :
                        c=c+4
                        d=d+4
                        if c >=16:
                            for n in list :
                                for v in list[1:]:
                                    if v-n==1:
                                        c=n
                                        d=v
                                        break
                                    if v-n==4:
                                        c=n
                                        d=v
                                        break
                    else:
                        check=0
            print("computer chooses:\n",c,d)
            list.remove(c)
            list.remove(d)
            turn=1


        if list == [1,7,13,16]:
            print ("computer wins ")
            stop=0
            break
        
        if list==win:
            print("computer wins")
            print("I win :)")
            print("come on that was easy try again")
            stop=0
            break
        for m in list:
            for v in list[1:]:
                if (v-m==1 ) or (v-m==4):
                    you_win=1
                    break
        if you_win==0:
            print("computer wins")
            print("I win :)")
            print("come on that was easy try again")
            stop=0
            break
