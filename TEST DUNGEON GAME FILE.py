import random

print("\033[1;31;40mTHE QUARTERS OF THE CRIMSON DRAGON")
print("")



done=False


#Room Setups/Class Setups

room_list = []
class_list= []
inventory= []

#Spawn 00
room = ["Spawn",1,None,None,None]
room_list.append(room)

#Hall 01
room = ["Hall 1",2,None,None,None]
room_list.append(room)

#Room 02
room= ["Room 2",3,None,None,None]
room_list.append(room)

#Hall 03 (First area of upgrade/shop)
room=["Hall 3",6,4,None,5]
room_list.append(room)

#Shop 04
room=["Shop",None,None,None,3]
room_list.append(room)

#Upgrade_05
room=["Upgrade 5",None,3,None,None]
room_list.append(room)

#Room 06
room=["Room 6",None,7,None,8]
room_list.append(room)

#Room 07
room=["Room 7",10,None,None,None]
room_list.append(room)

#Room 08
room=["Room 8",9,None,None,None]
room_list.append(room)

#Hall 9
room=["Hall 9",None,10,None,None]
room_list.append(room)

#Room 10
room=["Room 10",13,None,None,None]
room_list.append(room)

#Shop 11
room=["Shop",None,None,None,13]
room_list.append(room)

#Upgrade 12
room=["Upgrade",None,13,None,None]
room_list.append(room)

#Hall 13 (second area of upgrade/shop before final boss)
room=["Hall 13",14,11,None,12]
room_list.append(room)

#Boss room 14
room=["Room 14",15,None,None,None]
room_list.append(room)

#Final Room / LOOT
room=["Room 15",None,None,None]
room_list.append(room)


#classes = ["class",health,bot damage,top damage, defense,"ability"]
archer=["Archer",50,40,50,30,"Arrow Bomb"]
class_list.append(archer)

warrior=["Warrior",75,20,30,80,"War Cry"]
class_list.append(warrior)

assassin=["Assassin",30,65,75,30,"Shurikens"]
class_list.append(assassin)

#Variables

current_room=0
current_class=0

input_class="placeholder"
x=0
y=0
health=100
coins=0
defense=0
ability="user_ability"
token = 2 #for upgrade rooms minus one token each time passing through
user_score = 0
computer_score = 0



#inventory_items
Hall01_Key="Hall 1 Key"
Room02_Key="Room 2 Key"
Room06_Key="Room 6 key"
Room07_Key = "Room 7 Key"
Room08_Key ="Room 8 Key"
Room10_Key = "Room 10 Key"
Room14_Key="Room 14 Key"



display_secret_message = "Note: iwfltsx"
decoder = "Decoder (press s to use)"
secret_message="iwfltsx"











while not done: #begining of game, choosing class

    while input_class=="placeholder":
        print("\033[1;32;40mChoose your class: Archer, Warrior or Assassin.")
        user_input=input("\n")

        if user_input.lower()=="archer" or user_input=="1":
            print("You choose Archer")
            input_class="Archer"
            print("")
            current_class=class_list[0]
            print("Health:",current_class[1])
            print("Damage:",current_class[2],"-",current_class[3])
            print("Defense:",current_class[4])
            print("Ability:",current_class[5])

        if user_input.lower()=="warrior" or user_input=="2":
            print("You choose Warrior")
            input_class="Warrior"
            print("")
            current_class=class_list[1]
            print("Health:",current_class[1])
            print("Damage:",current_class[2],"-",current_class[3])
            print("Defense:",current_class[4])
            print("Ability:",current_class[5])

        if user_input.lower() == "assassin" or user_input=="3":
            print("You choose Assassin")
            input_class="Assassin"
            print("")
            current_class=class_list[2]
            print("Health:",current_class[1])
            print("Damage:",current_class[2],"-",current_class[3])
            print("Defense:",current_class[4])
            print("Ability:",current_class[5])

        health = current_class[1]
        x = current_class[2]
        y = current_class[3]
        defense = current_class[4]
        ability = current_class[5]

        user_input=input("\nIs this the class you want to play? y/n\n")

        if user_input.lower()=="no" or user_input.lower()=="n":
            input_class="placeholder"
            continue

        elif user_input.lower()=="yes" or user_input.lower()=="y":
            print("\n\033[1;33;40mAlright lets get started. Good Luck! Hopefully we will meet again soon.")
            break



#main game
    print("\n\033[1;32;40mYou are currently at",room_list[current_room][0])
    print("-------------------------------")
    print("Choose a direction N,E,S,W")
    print("1: Status")
    print("2: Inventory")
    print("Q: Quit")
    print("-------------------------------")


    user_input=input("")


    if user_input=="2":
        print("\033[1;34;40m-----------Backpack------------")


        for item in inventory:
            print(item)


        print("")
        print("")
        user_input=input("press x to go back\n")

        if user_input.lower() == "r":
            health += 50
            print("You gained 50 health!")
            inventory.remove(health_potion)

        if user_input.lower() == "t":
            x += 10
            y += 10
            print("You gained 10 damage!")
            inventory.remove(strength_potion)

        if user_input.lower() == "y":
            defense += 10
            print("You gained 10 defense!")
            inventory.remove(defense_potion)

        if user_input=="x":
            continue
        if user_input=="s":
            if secret_message in inventory:
                print("You used the decoder... enter a number to shift the message by:")
                j=int(input(""))

                for i in secret_message:
                    i = ord(i)
                    i += j
                    print(chr(i), end="")
                print("", j)
        else:
            pass

    if user_input=="1":
        print("\033[1;34;40m------------Status-------------")
        print("Health:", health)
        print("Damage:", x, "-",y)
        print("Defense:", defense)
        print("Ability:", ability)
        print("-------------------------------")

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

    if current_room==1: #HALL 01
        print("")
        print("\033[1;37;40mYou walk down an eerie hall, unsure of what lies ahead....")
        print("You suddenly hear a sound coming farther down the hall or maybe it was just your imagination.")
        print("Out of the corner of your eye, you spot something.")

        user_input=input("\n\033[1;32;40mApproach the mysterious figure? y/n\n")


        if user_input.lower() == "no" or user_input.lower() == "n":
            print("\nYou decide to not approach it, and moved on")

        if user_input.lower() == "yes" or user_input.lower() == "y":
            print("\nYou decide to approach it and found a \033[1;33;40mKey!")
            print("\033[1;32;40m")
            inventory.append(Hall01_Key)

        print("You approach the haunted looking door, however there is a lock on it.") #locked door opening

        if Hall01_Key in inventory:
            print("You quickly remembered that you found a key earlier, and used it to open the door.")
            inventory.remove(Hall01_Key)
            next_room = room_list[current_room][1]

            user_input = input("\n\033[3;35;40mpress enter to continue\n")
            if user_input == "" \
                             "":
                pass
            else:
                continue


            if next_room==None:
                print("You can't go that way!")
            else:
                current_room=next_room

        else:
            print("The door won't budge open, perhaps I missed something?")

            user_input=input("\nApproach the mysterious figure again? y/n\n")

            if user_input.lower() == "no" or user_input.lower() == "n":
                print("\n\033[1;31;40mYou decide to not approach it, and starved to death in the halls")
                done=True

            if user_input.lower() == "yes" or user_input.lower() == "y":
                print("You decide to approach it and found a \033[1;33;40mKey!")
                print("\033[1;32;40mYou used the key to open the door\n")
                inventory.append(Hall01_Key)

                next_room = room_list[current_room][1]
                if next_room == None:
                    print("You can't go that way!")
                else:
                    current_room = next_room

    if current_room==2: #ROOM 2

        if Room02_Key in inventory:
            uk=0
            pass
        else:
            uk=1
        # Undying Knight Settings
        undyingk_health = 300
        undyingk_topdmg = 5
        undyingk_botdmg = 1

        #user stats
        ability_charges = 2

        while uk==1:



            if health<1:
                print("You lost to the Undying Knight!")
                break


            print("\033[1;31;40mROOM 2\nTHE UNDYING KNIGHT")
            print("""                       _.--.    .--._
                     ."  ."      ".  ".
                    ;  ."    /\    ".  ;
                    ;  '._,-/  \-,_.`  ;
                    \  ,`  / /\ \  `,  /
                     \/    \/  \/    \/
                     ,=_    \/\/    _=,
                     |  "_   \/   _"  |
                     |_   '"-..-"'   _|
                     | "-.        .-" |
                     |    "\    /"    |
                     |      |  |      |
             ___     |      |  |      |     ___
         _,-",  ",   '_     |  |     _'   ,"  ,"-,_
       _(  \  \   \\"=--"-.  |  |  .-"--="/   /  /  )_
     ,"  \  \  \   \      "-'--'-"      /   /  /  /  ".
    !     \  \  \   \                  /   /  /  /     !
    :      \  \  \   \                /   /  /  /      TK
    """)
            print("Undying Knight HP:",undyingk_health)
            print("------------------------")
            print("\033[1;33;40mYour HP:",health)
            print("\033[1;31;40mActions:")
            print("1. Attack")
            print("2. Ability")
            print("3. Inventory")
            user_input = input("\n")


            if user_input=="1":
                player_damage=random.randint(x,y)
                uk_damage=random.randint(undyingk_botdmg,undyingk_topdmg)

                undyingk_health-=player_damage
                health-=uk_damage

                print("\033[1;33;40mYou did",player_damage,"dmg to the Undying Knight!")
                print("\033[1;32;40m------------------------")
                print("\033[1;31;40mThe Undying Knight did",uk_damage,"dmg to you!")

            if user_input=="2":

                if ability_charges>0:

                    if ability=="Arrow Bomb":
                        player_damage=60
                        uk_damage = 9
                        undyingk_health-=player_damage
                        health -= uk_damage
                        print("\033[1;33;40mYou used",ability,"and rained arrows on the Undying Knight!")
                        print("\033[1;32;40m------------------------")
                        print("\033[1;31;40mThe Undying Knight used sword swing and did",uk_damage, "dmg to you!")
                        ability_charges-=1

                    if ability=="War Cry":
                        uk_damage = 6
                        health -= uk_damage
                        health+=50
                        print("\033[1;33;40mYou used",ability,"and healed for 50 hp!")
                        print("\033[1;32;40m------------------------")
                        print("\033[1;31;40mThe Undying Knight used sword swing and did",uk_damage, "dmg to you!")
                        ability_charges-=1

                    if ability=="Shurikens":
                        player_damage = 80
                        uk_damage = 9
                        undyingk_health -= player_damage
                        health -= uk_damage
                        print("\033[1;33;40mYou used", ability, "and threw shurikens at the Undying Knight")
                        print("\033[1;32;40m------------------------")
                        print("\033[1;31;40mThe Undying Knight used sword swing and did", uk_damage, "dmg to you!")
                        ability_charges-=1
                else:
                    print("You have no energy left to use an ability!")

            if undyingk_health<0 or undyingk_health==0:
                print("You defeated the Undying Knight!")
                print("\033[1;33;40mYou gained 20 coins!")
                coins+=20
                inventory.append(Room02_Key)
                uk=0


            if user_input=="3":
                print("\033[1;34;40m-----------Backpack------------")

                for item in inventory:
                    print(item)

                print("")
                print("")
                user_input = input("press x to go back\n")
                if user_input == "x":
                    continue
                else:
                    pass




    if current_room==3: #3rd room
        health_potion="Health Potion (press r to use)"
        strength_potion="Strength Potion (press t to use)"
        defense_potion="Defense Potion (press y to use)"

        print("")
        print("\033[1;34;40mWelcome to the resting center.\nTo your east, we have a shop.\nTo your west, there is an upgrade center.\nIf you want to preceed, please go north.")
        print("")

    if current_room==4: #shop
        print("")
        print("\033[1;35;40m--------------SHOP--------------")
        print("1.Health Potion--------------$20")
        print("2.Strength Potion------------$20")
        print("3.Defense Potion-------------$20")
        print("4.Ability Charge-------------$20")
        print("--------------------------------")
        print("\033[1;33;40mYou have: $",coins,)


        user_input=input("Press x to go back or the corresponding number to buy the item.")
        if user_input == "x":
            continue
        else:
            pass

        if user_input=="1":
            if coins>=20:
                coins-=20
                inventory.append(health_potion)
            else:
                print("You don't have enough coins!")
                pass

        if user_input=="2":
            if coins>=20:
                coins-=20
                inventory.append(strength_potion)
            else:
                print("You don't have enough coins!")
                pass

        if user_input=="3":
            if coins>=20:
                coins-=20
                inventory.append(defense_potion)
            else:
                print("You don't have enough coins!")
                pass

        if user_input=="4":
            if coins>=20:
                coins-=20
                ability_charges+=1
            else:
                print("You don't have enough coins!")
                pass

    if current_room==5: #Upgrade Room
        if token==2:
            print("")
            print("\033[1;35;40mHello Traveler, Pick an upgrade below....")
            print("\033[1;34;40m-----------------------------------------")
            print("\033[1;34;40mGain 50 Hp-------------1")
            print("\033[1;34;40mGain 10 Damage---------2")
            print("\033[1;34;40mGain 10 Defense--------3")
            print("\033[1;34;40m-----------------------------------------")
            user_input=input("")

            if user_input=="1":
                health+=50
                token-=1

            if user_input=="2":
                x+=10
                y+=10
                token-=1

            if user_input=="3":
                defense+=10
                token-=1
        else:
            pass

    if current_room==6: #Room 6
        if Room06_Key in inventory:
            pass
        else:
            print("")
            print("\033[1;36;40mHello Traveler, lets play a game shall we? Beat me 2 times and I will let you through...\nThe game is simple, \033[1;34;40mWater\033[1;36;40m > \033[1;31;40mFire\033[1;36;40m, \033[1;31;40mFire\033[1;36;40m > \033[1;32;40mGrass\033[1;36;40m and \033[1;32;40mGrass\033[1;36;40m > \033[1;34;40mWater\033[1;36;40m.")



            while user_score<=1:


                print("")
                user_input = int(input("\033[1;35;40mChoose an option, 1 for a \033[1;34;40mwater \033[1;35;40mspell, 2 for a \033[1;31;40mfire \033[1;35;40mspell, 3 for a \033[1;32;40mgrass \033[1;35;40mspell\n"))
                print("")

                if user_input == 1 or user_input == 2 or user_input == 3:
                    if user_input == 1:
                        print("\033[1;34;40mYou casted a water spell!")
                    elif user_input == 2:
                        print("\033[1;31;40mYou casted a fire spell!")
                    else:
                        print("\033[1;32;40mYou casted a grass spell!")
                    computer_input = random.randint(1, 3)
                    if computer_input == 1:
                        print("\033[1;34;40mThe Dark Wizard casted a water spell!")
                        print("-------------------------------------")
                    elif computer_input == 2:
                        print("\033[1;31;40mThe Dark Wizard casted a fire spell!")
                        print("------------------------------------")
                    else:
                        print("\033[1;32;40mThe Dark Wizard casted a grass spell!")
                        print("-------------------------------------")
                    if computer_input == user_input:
                        print("\n\033[1;36;40mThe Arena clashed with the same spell!")
                    elif user_input == 1 and computer_input == 2:
                        print("\n\033[1;36;40mYou gained a point! The water spell extinguished the flames.")
                        user_score+=1
                    elif user_input == 1 and computer_input == 3:
                        print("\n\033[1;36;40mThe Dark Wizard casted a grass spell to absorb the water.")
                        computer_score+= 1
                    elif user_input == 2 and computer_input == 3:
                        print("\n\033[1;36;40mYou gained a point! The fire spell burned the grass.")
                        user_score += 1
                    elif user_input == 2 and computer_input == 1:
                        print("\n\033[1;36;40mThe Dark Wizard casted a water spell to drown out your fire.")
                        computer_score += 1
                    elif user_input == 3 and computer_input == 1:
                        print("\n\033[1;36;40mYou gained a point! The power of nature neutralizes the water.")
                        user_score += 1
                    elif user_input == 3 and computer_input == 2:
                        print("\n\033[1;36;40mThe Dark Wizard casted a fire spell to combust the grass spell.")
                        computer_score += 1
                    else:
                        print("Hey that's not an option!")

        if Room06_Key not in inventory:
            print("\033[1;33;40mYou beat the Dark Wizard!")
            print("\033[1;33;40mYou gained 20 coins!")
            coins += 20
            inventory.append(Room06_Key)

    if current_room==7: #Room 7
        correct_number=random.randint(0,100)

        if Room07_Key in inventory:
            pass
        else:
            print("\033[1;36;40mI will let you pass if you can guess the correct number between 0-100...")

            while Room07_Key not in inventory:
                user_input=int(input("\033[1;35;40mEnter a number.\n"))
                if user_input<correct_number:
                    print("\n\033[1;32;40mThe number is \033[1;31;40mhigher...\n")

                elif user_input>correct_number:
                    print("\n\033[1;32;40mThe number is \033[1;36;40mlower...")

                elif user_input==correct_number:
                    print("\033[1;36;40mYou guessed it! Here is the \033[1;33;40mkey...")
                    inventory.append(Room07_Key)
                    break

    if current_room == 8:  # Room 8
        correct_number = random.randint(0, 100)
        if Room08_Key in inventory:
            pass
        else:
            print("\033[1;36;40mI will let you pass if you can guess the correct number between 0-100...")

            while Room08_Key not in inventory:
                user_input = int(input("\033[1;35;40mEnter a number.\n"))
                if user_input < correct_number:
                    print("\n\033[1;32;40mThe number is \033[1;31;40mhigher...\n")

                elif user_input > correct_number:
                    print("\n\033[1;32;40mThe number is \033[1;36;40mlower...")

                elif user_input == correct_number:
                    print("\033[1;36;40mYou guessed it! Here is the \033[1;33;40mkey...")
                    inventory.append(Room08_Key)
                    break

    if current_room==9: #Hall 9
        print("")
        print("\033[1;37;40mYou cautiously walk down the lit up hall...")
        print("From the corner of your eye, you spot a mysterious hole.")

        user_input = input("\n\033[1;32;40mApproach the mysterious hole? y/n\n")

        if user_input.lower() == "no" or user_input.lower() == "n":
            print("\nYou decide to not approach it, and moved on")

        if user_input.lower() == "yes" or user_input.lower() == "y":
            print("\nYou decide to approach it and realized it was a trap!\n\033[1;31;40mYou lost 20 coins!")
            coins-=20


    if current_room==10: #Room 10 Puzzle room
        while Hall01_Key in inventory:
            inventory.remove(Hall01_Key)
        while Room02_Key in inventory:
            inventory.remove(Room02_Key)
        while Room06_Key in inventory:
            inventory.remove(Room06_Key)
        while Room07_Key in inventory:
            inventory.remove(Room07_Key)
        while Room08_Key in inventory:
            inventory.remove(Room08_Key)
        while Room10_Key in inventory:
            inventory.remove(Room10_Key)


        decoderuse=0
        print("\033[1;35;40mYou approach a darkly lit room. Unsure of where to go next.\n")

        while Room10_Key not in inventory:
            print("\n\033[1;32;40m1) Approach the door.")
            print("2) Explore the coffin.")
            print("3) Explore the bookcase.")
            print("4) Explore the rocks.")
            print("5) Inventory")
            user_input=input("")

            if user_input=="1":
                print("\033[1;37;40mYou approached the door, it says \033[1;31;40mEnter the code:")
                user_input = input("")

                if user_input.lower()=="dragons":
                    print("\033[1;33;40mThe door cracks open....")
                    inventory.append(Room10_Key)

                else:
                    print("\033[1;31;40mThe door does not budge open...")

            if user_input=="2":
                print("\033[1;37;40mYou explored the coffin in the corner of the room.")
                print("You found a tiny slip of paper hanging out of the coffin....")
                print("It reads:", display_secret_message)
                inventory.append(display_secret_message)

            if user_input=="3":
                print("\033[1;37;40mYou explored the bookcase near the candle.")
                print("There is no books to lying around, but something was left on the bookshelf.")
                print("You found a \033[1;33;40mdecoder!")
                inventory.append(decoder)

            if user_input=="4":
                print("\033[1;37;40mYou explored near the rock.")
                print("You were hoping to be something near the rock, but you honestly found nothing except 5 tiny rock pieces.")

            if user_input == "5":
                print("\033[1;34;40m-----------Backpack------------")

                for item in inventory:
                    print(item)

                print("")
                print("")
                user_input = input("press x to go back\n")

                if user_input == "x":
                    continue
                if user_input == "s":
                    if display_secret_message in inventory:
                        decoderuse=1
                        while decoderuse==1:
                            print("You used the decoder...enter a number to shift the message by:")
                            j = int(input(""))

                            for i in secret_message:
                                i = ord(i)
                                i += j
                                print(chr(i), end="")
                            print("")

                            print("Use decoder again?")
                            user_input=input("").lower()

                            if user_input=="y" or user_input=="yes":
                                decoderuse=1
                            else:
                                decoderuse=0
                    else:
                        print("\nThere is nothing to decode!")
                else:
                    pass


    if current_room==13: #hall 13
        print("")
        print("\033[1;34;40mWelcome to the resting center.\nTo your east, we have a shop.\nTo your west, there is an upgrade center.\nIf you want to preceed, please go north.")
        print("")


    if current_room==12: #upgrade 12
        if token==1:
            print("")
            print("\033[1;35;40mHello Traveler, Pick an upgrade below....")
            print("\033[1;34;40m-----------------------------------------")
            print("\033[1;34;40mGain 50 Hp-------------1")
            print("\033[1;34;40mGain 10 Damage---------2")
            print("\033[1;34;40mGain 10 Defense--------3")
            print("\033[1;34;40m-----------------------------------------")
            user_input=input("")

            if user_input=="1":
                health+=50
                token-=1

            if user_input=="2":
                x+=10
                y+=10
                token-=1

            if user_input=="3":
                defense+=10
                token-=1
        else:
            pass

    if current_room==11:
        print("")
        print("\033[1;35;40m--------------SHOP--------------")
        print("1.Health Potion--------------$20")
        print("2.Strength Potion------------$20")
        print("3.Defense Potion-------------$20")
        print("4.Ability Charge-------------$20")
        print("--------------------------------")
        print("\033[1;33;40mYou have: $", coins, )

        user_input = input("Press x to go back or the corresponding number to buy the item.")
        if user_input == "x":
            continue
        else:
            pass

        if user_input == "1":
            if coins >= 20:
                coins -= 20
                inventory.append(health_potion)
            else:
                print("You don't have enough coins!")
                pass

        if user_input == "2":
            if coins >= 20:
                coins -= 20
                inventory.append(strength_potion)
            else:
                print("You don't have enough coins!")
                pass

        if user_input == "3":
            if coins >= 20:
                coins -= 20
                inventory.append(defense_potion)
            else:
                print("You don't have enough coins!")
                pass

        if user_input == "4":
            if coins >= 20:
                coins -= 20
                ability_charges += 1
            else:
                print("You don't have enough coins!")
                pass

    if current_room==14:# FINAL BOSS ROOM
        while Hall01_Key in inventory:
            inventory.remove(Hall01_Key)
        while Room02_Key in inventory:
            inventory.remove(Room02_Key)
        while Room06_Key in inventory:
            inventory.remove(Room06_Key)
        while Room07_Key in inventory:
            inventory.remove(Room07_Key)
        while Room08_Key in inventory:
            inventory.remove(Room08_Key)
        while Room10_Key in inventory:
            inventory.remove(Room10_Key)
        while decoder in inventory:
            inventory.remove(decoder)
        while display_secret_message in inventory:
            inventory.remove(display_secret_message)


        if Room14_Key in inventory:
            cd=0
            pass
        else:
            cd=1
        # Crimson Dragon Settings
        crimsond_health = 400
        crimsond_topdmg = 10
        crimsond_botdmg = 1

        while cd==1:
            ability_charges+=2

            if health<1:
                print("\033[1;31;40mYou lost to the Crimson Dragon!")
                done=True


            print("\033[1;31;40mROOM 2\nTHE CRIMSON DRAGON")
            print("""                                
                         ( _)                ( _)
                        / / \\\\              / /\_\_
                       / /   \\\\            / / | \ \\
                      / /     \\\\          / /  |\ \ \\
                     /  /   ,  \ ,       / /   /|  \ \\
                    /  /    |\_ /|      / /   / \   \_\\
                   /  /  |\/ _ '_|\    / /   /   \    \\\\
                  |  /   |/  0 \\0\ \  / |    |    \    \\\\
                  |    |\|      \_\_ /  /    |     \    \\\\
                  |  | |/    \.\ o\o)  /      \     |    \\\\
                  \    |     /\\\\`v-v  /        |    |     \\\\
                   | \/    /_| \\\\_|  /         |    | \    \\\\
                   | |    /__/_     /   _____  |    |  \    \\\\
                   \|    [__]  \_/  |_________  \   |   \    ()
                    /    [___] (    \         \  |\ |   |   //
                   |    [___]                  |\| \|   /  |/
                  /|    [____]                  \  |/\ / / ||
             snd (  \   [____ /     ) _\      \  \    \| | ||
                  \  \  [_____|    / /     __/    \   / / //
                  |   \ [_____/   / /        \    |   \/ //
                  |   /  '----|   /=\____   _/    |   / //
               __ /  /        |  /   ___/  _/\    \  | ||
              (/-(/-\)       /   \  (/\/\)/  |    /  | /
                            (/\/\)           /   /   //
                                   _________/   /    /
                                  \____________/    (""")
            print("Crimson Dragon HP:",crimsond_health)
            print("------------------------")
            print("\033[1;33;40mYour HP:",health)
            print("\033[1;31;40mActions:")
            print("1. Attack")
            print("2. Ability")
            print("3. Inventory")
            user_input = input("\n")


            if user_input=="1":
                player_damage=random.randint(x,y)
                cd_damage=random.randint(crimsond_botdmg,crimsond_topdmg)

                crimsond_health-=player_damage
                health-=cd_damage

                print("\033[1;33;40mYou did",player_damage,"dmg to the Crimson Dragon!")
                print("\033[1;32;40m------------------------")
                print("\033[1;31;40mThe Crimson Dragon did",cd_damage,"dmg to you!")

            if user_input=="2":

                if ability_charges>0:

                    if ability=="Arrow Bomb":
                        player_damage=60
                        cd_damage = 12
                        crimsond_health-=player_damage
                        health -= cd_damage
                        print("\033[1;33;40mYou used",ability,"and rained arrows on the Crimson Dragon!")
                        print("\033[1;32;40m------------------------")
                        print("\033[1;31;40mThe Crimson Dragon breathed fire on you and did",cd_damage, "dmg to you!")
                        ability_charges-=1

                    if ability=="War Cry":
                        cd_damage = 6
                        health -= cd_damage
                        health+=50
                        print("\033[1;33;40mYou used",ability,"and healed for 50 hp!")
                        print("\033[1;32;40m------------------------")
                        print("\033[1;31;40mThe Crimson Dragon used lava breath and did",cd_damage, "dmg to you!")
                        ability_charges-=1

                    if ability=="Shurikens":
                        player_damage = 80
                        cd_damage = 12
                        crimsond_health -= player_damage
                        health -= cd_damage
                        print("\033[1;33;40mYou used", ability, "and threw shurikens at the Crimson Dragon")
                        print("\033[1;32;40m------------------------")
                        print("\033[1;31;40mThe Crimson Dragon used fire breath and did", cd_damage, "dmg to you!")
                        ability_charges-=1
                else:
                    print("You have no energy left to use an ability!")

            if crimsond_health<=0:
                print("You defeated the Undying Knight!")
                inventory.append(Room14_Key)
                cd=0


            if user_input=="3":
                print("\033[1;34;40m-----------Backpack------------")

                for item in inventory:
                    print(item)

                print("")
                print("")
                user_input = input("press x to go back\n")

                if user_input.lower()=="r":
                    health+=50
                    print("You healed for 50 hp!")
                    inventory.remove(health_potion)

                if user_input.lower()=="t":
                    x+=10
                    y+=10
                    print("You gained 10 damage!")
                    inventory.remove(strength_potion)

                if user_input.lower()=="y":
                    defense+=10
                    print("You gained 10 defense!")
                    inventory.remove(defense_potion)

                if user_input.lower() == "x":
                    continue
                else:
                    pass

    if current_room==15:
        print("\033[1;33;40mYou found the treasure room! Congrats on winning!")
        print("\033[1;34;40mI told you we will meet again traveler..... See you next time!")
        done= True

print("\033[1;35;40mThanks for playing!")