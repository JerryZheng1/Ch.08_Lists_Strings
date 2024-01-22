import random

print("\033[1;31;40mTHE QUARTERS OF THE CRIMSON DRAGON")
print("")
print("\033[1;32;40mChoose your class: Assassin, Warrior or Archer.")


done=False


#Room Setups

room_list = []

#Spawn 00
room = ["Spawn_0",1,None,None,None]
room_list.append(room)

#Hall 01
room = ["Hall_1",2,None,None,None]
room_list.append(room)

#Room 02
room= ["Room_2",3,None,None,None]
room_list.append(room)

#Hall 03 (First area of upgrade/shop)
room=["Hall_3",6,4,None,5]
room_list.append(room)

#Shop 04
room=["Shop_4",None,None,None,3]
room_list.append(room)

#Upgrade_05
room=["Upgrade_5",None,3,None,None]
room_list.append(room)

#Room 06
room=["Room_6",None,7,None,8]
room_list.append(room)

#Room 07
room=["Room_7",10,None,None,None]
room_list.append(room)

#Room 08
room=["Room_8",9,None,None,None]
room_list.append(room)

#Hall 9
room=["Hall_9",None,10,None,None]
room_list.append(room)

#Room 10
room=["Room_10",13,None,None,None]
room_list.append(room)

#Shop 11
room=["Shop_11",None,None,None,13]
room_list.append(room)

#Upgrade 12
room=["Upgrade_12",None,13,None,None]
room_list.append(room)

#Hall 13 (second area of upgrade/shop before final boss)
room=["Hall_13",14,11,None,12]
room_list.append(room)

#Boss room 14
room=["Room_14",15,None,None,None]
room_list.append(room)

#Final Room / LOOT
room=["Room_15",None,None,None]
room_list.append(room)

#Variables


current_room=0

while not done:
    user_input=input("Choose a direction N, E, S, W or Q for quit\n")
    if user_input.lower()=="n" or user_input.lower()=="north":
        next_room=room_list[current_room][1]
        if next_room==None:
            print("You can't go that way!")
        else:
            current_room=next_room

    if user_input.lower()=="e" or user_input.lower()=="east":
        next_room=room_list[current_room][2]
        if next_room==None:
            print("You can't go that way!")
        else:
            current_room=next_room

    if user_input.lower()=="s" or user_input.lower()=="south":
        next_room=room_list[current_room][3]
        if next_room==None:
            print("You can't go that way!")
        else:
            current_room=next_room

    if user_input.lower()=="w" or user_input.lower()=="west":
        next_room=room_list[current_room][4]
        if next_room==None:
            print("You can't go that way!")
        else:
            current_room=next_room

    if user_input.lower()=="q":
        done=True







