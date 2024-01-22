# # # # # # # # # # # # # # mylist=[2,7,3,9,5,7]
# # # # # # # # # # # # # # mytuple=(2,7,3,9,5,7)
# # # # # # # # # # # # #
# # # # # # # # # # # # # # droids=["C3P0","R2D2","BB8","K2SO"]
# # # # # # # # # # # # # # num_items=len(droids)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print(num_items)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # for i in range(len(droids)):
# # # # # # # # # # # # # #     print(droids[i])
# # # # # # # # # # # # #
# # # # # # # # # # # # # # lists=[2,5,8,4,9,5]
# # # # # # # # # # # # # # for i in range(len(lists)):
# # # # # # # # # # # # # #     print(lists[i]**2)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # list=[[1,2],[3,4],[5,6]]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print(list[2][0])
# # # # # # # # # # # # #
# # # # # # # # # # # # # # list=[2,5,8,4,9,5]
# # # # # # # # # # # # # # # list=[[1,2],[3,4],[5,6]]
# # # # # # # # # # # # # # list.append(8) #add item to list
# # # # # # # # # # # # # # #len is length
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print(len(list))
# # # # # # # # # # # # # # print(list)
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # mylist=[]
# # # # # # # # # # # # # # total=0
# # # # # # # # # # # # # # for i in range(5):
# # # # # # # # # # # # # #     num = int(input("enter a number bro:"))
# # # # # # # # # # # # # #     mylist.append(num)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print(mylist)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # for item in mylist:
# # # # # # # # # # # # # #     total+=item
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print(total/len(mylist))
# # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # list = [2,4,8,4,9,4]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # for i in range(len(list)):
# # # # # # # # # # # # # #     if list[i]==4:
# # # # # # # # # # # # # #         list[i]=7
# # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # #         pass
# # # # # # # # # # # # # # print(list)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # uhs_slogan="My school is the best"
# # # # # # # # # # # # # # # print(len(uhs_slogan))
# # # # # # # # # # # # # # print(uhs_slogan[:13]+'awesome')
# # # # # # # # # # # # # # print(len(uhs_slogan))
# # # # # # # # # # # # # # words=0
# # # # # # # # # # # # # # for letter in uhs_slogan:
# # # # # # # # # # # # # #     if letter ==" ":
# # # # # # # # # # # # # #         words+=1
# # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # #         pass
# # # # # # # # # # # # # # print(words)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # for letter in uhs_slogan:
# # # # # # # # # # # # # #     print(ord(letter))
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # num=1000000
# # # # # # # # # # # # # # print(f"There are {num:10,} things")
# # # # # # # # # # # # # # print(num)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # a_list = [3,12,3,5,3,4,6,8,5,3,5,6,3,2,4]
# # # # # # # # # # # # # # b_list = [4,15,2,7,8,3,1,10,9]
# # # # # # # # # # # # # # c_list = [5,10,13,12,5,9,2,6,1,8,8,9,11,13,14,8,2,2,6,3,9,8,10]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # total=0
# # # # # # # # # # # # # # done=False
# # # # # # # # # # # # # # while not done:
# # # # # # # # # # # # # #     user_input=input("Enter a list")
# # # # # # # # # # # # # #     if user_input.lower()=="a":
# # # # # # # # # # # # # #         list=a_list
# # # # # # # # # # # # # #     if user_input.lower()=="b":
# # # # # # # # # # # # # #         list=b_list
# # # # # # # # # # # # # #     if user_input.lower()=="c":
# # # # # # # # # # # # # #         list=c_list
# # # # # # # # # # # # # #     for item in list:
# # # # # # # # # # # # # #         total += item
# # # # # # # # # # # # # #     print("Sum:",total)
# # # # # # # # # # # # # #     print("Average:",total/len(list))
# # # # # # # # # # # # # #     total=0
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # done=False
# # # # # # # # # # # # # # while not done:
# # # # # # # # # # # # # #     user_input=input("what is your e-mail address")
# # # # # # # # # # # # # #     for item in user_input:
# # # # # # # # # # # # # #         if item=="@":
# # # # # # # # # # # # # #             print("")
# # # # # # # # # # # # # #             break
# # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # #             print(item,end="")
# # # # # # # # # # # # #
# # # # # # # # # # # # # # score = 41237
# # # # # # # # # # # # # # highscore = 1023407
# # # # # # # # # # # # # # print(f"Score:{score:16,}")
# # # # # # # # # # # # # # print(f"High score:{highscore:11,}")
# # # # # # # # # # # # #
# # # # # # # # # # # # # # done=False
# # # # # # # # # # # # # # months = "JanFebMarAprMayJunJulAugSepOctNovDec"
# # # # # # # # # # # # # # while not done:
# # # # # # # # # # # # # #     month_input=int(input("Enter a month number 1-12:"))
# # # # # # # # # # # # # #     if month_input>=1 and month_input<=12:
# # # # # # # # # # # # # #         print(months[(month_input*3)-3:month_input*3])
# # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # #         print("Thats not an option!")
# # # # # # # # # # # # # #         done=True
# # # # # # # # # # # # # Secret_Message="Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*"
# # # # # # # # # # # # #
# # # # # # # # # # # # # for j in range(-20,21):
# # # # # # # # # # # # #     for i in Secret_Message:
# # # # # # # # # # # # #         i=ord(i)
# # # # # # # # # # # # #         i+=j
# # # # # # # # # # # # #         print(chr(i), end="")
# # # # # # # # # # # # #
# # # # # # # # # # # # #     print("",j)
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # a_list = [3,12,3,5,3,4,6,8,5,3,5,6,3,2,4]
# # # # # # # # # # # # b_list = [4,15,2,7,8,3,1,10,9]
# # # # # # # # # # # # c_list = [5,10,13,12,5,9,2,6,1,8,8,9,11,13,14,8,2,2,6,3,9,8,10]
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # total=0
# # # # # # # # # # # # done=False
# # # # # # # # # # # # while not done:
# # # # # # # # # # # #     user_input=input("Enter a list (a,b,or c)")
# # # # # # # # # # # #     if user_input.lower()=="a":
# # # # # # # # # # # #         list=a_list
# # # # # # # # # # # #     if user_input.lower()=="b":
# # # # # # # # # # # #         list=b_list
# # # # # # # # # # # #     if user_input.lower()=="c":
# # # # # # # # # # # #         list=c_list
# # # # # # # # # # # #     for item in list:
# # # # # # # # # # # #         total += item
# # # # # # # # # # # #     print("Sum:",total)
# # # # # # # # # # # #     print(f"Average:{total/len(list):.2f}")
# # # # # # # # # # # #     total=0
# # # # # # # # # # #
# # # # # # # # # # # done=False
# # # # # # # # # # # while not done:
# # # # # # # # # # #     user_input=input("what is your e-mail address")
# # # # # # # # # # #     for item in user_input:
# # # # # # # # # # #         if item=="@":
# # # # # # # # # # #             print("")
# # # # # # # # # # #             break
# # # # # # # # # # #         else:
# # # # # # # # # # #             print(item,end="")
# # # # # # # # # #
# # # # # # # # # # done=False
# # # # # # # # # # while not done:
# # # # # # # # # #     user_input=input("what is your e-mail address? ")
# # # # # # # # # #     for item in user_input:
# # # # # # # # # #         if item=="@":
# # # # # # # # # #             print("")
# # # # # # # # # #             break
# # # # # # # # # #         else:
# # # # # # # # # #             print(item,end="")
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # score = 41237
# # # # # # # # # highscore = 1023407
# # # # # # # # # print(f"Score:{score:16,}")
# # # # # # # # # print(f"High score:{highscore:11,}")
# # # # # # # # done=False
# # # # # # # # months = "JanFebMarAprMayJunJulAugSepOctNovDec"
# # # # # # # # while not done:
# # # # # # # #     month_input=int(input("Enter a month number 1-12:"))
# # # # # # # #     if month_input>=1 and month_input<=12:
# # # # # # # #         print(months[(month_input*3)-3:month_input*3])
# # # # # # # #     else:
# # # # # # # #         print("Thats not an option!")
# # # # # # # #         done=True
# # # # # # # # Secret_Message="Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*"
# # # # # # # #
# # # # # # # # for j in range(-20,21):
# # # # # # # #     for i in Secret_Message:
# # # # # # # #         i=ord(i)
# # # # # # # #         i+=j
# # # # # # # #         print(chr(i), end="")
# # # # # # # #     print("",j)
# # # # # # #
# # # # # # #
# # # # # # # #
# # # # # # # # Secret_Message="Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*"
# # # # # # # #
# # # # # # # # spaces=0
# # # # # # # # for j in range(-20,21):
# # # # # # # #     for i in Secret_Message:
# # # # # # # #         i=ord(i)
# # # # # # # #         i+=j
# # # # # # # #         if i==32:
# # # # # # # #             spaces+=1
# # # # # # # #         print(chr(i), end="")
# # # # # # # #         if spaces>=3:
# # # # # # # #             print("", j)
# # # # # # # #         else:
# # # # # # # #             break
# # # # # # #
# # # # # # # Secret_Message="Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*"
# # # # # # # for j in range(-20,21):
# # # # # # #     for i in Secret_Message:
# # # # # # #         i=ord(i)
# # # # # # #         i+=j
# # # # # # #         print(chr(i), end="")
# # # # # # #     print("",j)
# # # # # # #
# # # # # # a_list = [3,12,3,5,3,4,6,8,5,3,5,6,3,2,4]
# # # # # # b_list = [4,15,2,7,8,3,1,10,9]
# # # # # # c_list = [5,10,13,12,5,9,2,6,1,8,8,9,11,13,14,8,2,2,6,3,9,8,10]
# # # # # #
# # # # # #
# # # # # #
# # # # # # total=0
# # # # # # done=False
# # # # # # while not done:
# # # # # #     user_input=input("Enter a list (a,b,or c)")
# # # # # #     if user_input.lower()=="a":
# # # # # #         list=a_list
# # # # # #     if user_input.lower()=="b":
# # # # # #         list=b_list
# # # # # #     if user_input.lower()=="c":
# # # # # #         list=c_list
# # # # # #     for item in list:
# # # # # #         total += item
# # # # # #     print("Sum:",total)
# # # # # #     print(f"Average:{total/len(list):.2f}")
# # # # # #     total=0
# # # # # done=False
# # # # # while not done:
# # # # #     user_input=input("what is your e-mail address? ")
# # # # #     for item in user_input:
# # # # #         if item=="@":
# # # # #             print("")
# # # # #             break
# # # # #         else:
# # # # #             print(item,end="")
# # # # done=False
# # # # while not done:
# # # #     user_input=input("what is your e-mail address? ")
# # # #     for item in user_input:
# # # #         if item=="@":
# # # #             print("")
# # # #             break
# # # #         else:
# # # #             print("Your username is:",end="")
# # # #             print(item,end="")
# # # #
# # # done=False
# # # while not done:
# # #     user_input=input("what is your e-mail address? ")
# # #     for item in user_input:
# # #         if item=="@":
# # #             print("")
# # #             break
# # #         else:
# # #             print("your username is",item,end="")
# # score = 41237
# # highscore = 1023407
# # print(f"Score:{score:16,}")
# # print(f"High score:{highscore:11,}")
# done=False
# months = "JanFebMarAprMayJunJulAugSepOctNovDec"
# while not done:
#     month_input=int(input("Enter a month number 1-12:"))
#     if month_input>=1 and month_input<=12:
#         print(months[(month_input*3)-3:month_input*3])
#     else:
#         print("Thats not an option!")
#         done=True

Secret_Message="Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*"
for j in range(-20,21):
    for i in Secret_Message:
        i=ord(i)
        i+=j
        print(chr(i), end="")
    print("",j)
