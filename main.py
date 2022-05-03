from ntpath import join
import random
from room import Room
from item import Item
from character import Character, Enemy, Friend
from rpginfo import RPGInfo

passos_castle = RPGInfo("The Passos's Castle")
passos_castle.welcome()
RPGInfo.info()

# ROOM
kitchen = Room('kitchen')
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")
exit = Room("Exit")

kitchen.set_description ('A dank and dirty room buzzing with flies')
dining_hall.set_description('A large room with ornate golden decorations on each wall')
ballroom.set_description('A vast room with a shiny wooden floor; huge candlesticks guard the entrance')
exit.set_description("A hallway that leads to a big door.\nIs that the exit from this castle?")

kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(ballroom, 'west')
dining_hall.link_room(kitchen, 'north')
ballroom.link_room(dining_hall, 'east')
ballroom.link_room(exit, 'south')
exit.link_room(ballroom, 'north')

# ITEMS
cheese = Item('Cheese')
sweatshirt = Item('Sweatshirt')
key = Item('Key')

cheese.set_descreption ("A Cheese?? What I'm suposed to do with this??")
sweatshirt.set_descreption("Hmm a sweartshirt... It's better to grab it just in case gets cold in here.")
key.set_descreption("A key?? I'm wondering what it'll open")

# CHARACTER
passos = Character('Passos', 'A friendly zombie!')
kitchen.set_character(passos)

dave = Enemy('Dave', 'An angry zombie!')
dave.set_conversation('arhrhhr..... brainssss....ahhhrhrrh')
dave.set_weakness('cheese')
dining_hall.set_character(dave)

Edu = Friend('Edu', 'A very nice skeleton!')
Edu.set_conversation('Hello over there!!!')
ballroom.set_character(Edu)

# IVENTORY
backpack = []

# LIFE
dead = True

current_room = kitchen
if dead == True:
    print('\n')

    if current_room == kitchen:
        print('\n')
        current_room.get_details()
        if 'cheese' in backpack:
            print("Passos isn't here anymore.")
            command = input('Where do you wanna go? \nnorth\neast\nwest\nsouth\n-> ')
            current_room = current_room.move(command)

        else:
            passos.describe()
            command = input('What you wanna do?\nMove to other room. (press 1)\nTalk to Passos. (press 2)\n-> ')
            if command == '1':
                command = input ('Wich direction you wanna go? \nnorth\neast\nwest\nsouth\n-> ')
                current_room = current_room.move(command)
            else:
                passos.set_conversation(None)
                passos.set_conversation('Looks like you need some help. This item may de useful for you.')
                passos.talk()
                command = input('\nAccept gift(1)      Deny gift(2)\n-> ')
                if command == '1':
                    passos.set_conversation(None)
                    passos.set_conversation("Take this cheese... You'll gonna need it!")
                    backpack.append('cheese')
                    print ("A cheese was added to your backpack")
                    cheese.describe()                
                else:
                    passos.set_conversation(None)
                    passos.set_conversation("You'll regret this choice!")
                    passos.talk()

                kitchen.set_character(None)
                print('Passos vanish!')
                command = input('What you wanna do?\nMove to other room.(1)      See backpack.(2)\n-> ')
                if command == '1':
                    command = input ('Wich direction you wanna go? \nnorth\neast\nwest\nsouth\n-> ')
                    current_room = current_room.move(command)
                else:
                    print ('\n','Backpack: '+''.join(backpack),'\n--------------------')
                    command = input("Where do you wanna go? \nnorth\neast\nwest\nsouth\n-> ")
                    current_room = current_room.move(command)

    if current_room == dining_hall:
        print ('\n')
        current_room.get_details()
        if current_room == dining_hall:
            if ', sweatshirt' in backpack or ', key' in backpack:
                command = input ('Wich direction you wanna go? \nnorth\neast\nwest\nsouth\n-> ')
                current_room = current_room.move(command)

            if 'cheese' in backpack and ", sweatshirt" not in backpack and not ', key' in backpack:
                dave.describe()
                dave.set_weakness('cheese')
                dave.get_weakness()
                print('\nDave is an enemy!! You have to kill him!!')
                command = input('Do you want to use the cheese that Passos gave to you?\nYes!(1)      No!(2)\n-> ')
                if command == '1':
                    dave.fight('cheese')
                    print('Dave drop a sweatshirt!\nA sweatshirt was added to your backpack.')
                    sweatshirt.describe()
                    backpack.append(', sweatshirt')
                    command = input('What you wanna do?\nMove to other room.(1)      See backpack.(2)\n-> ')
                    if command == '1':
                        command = input ('Wich direction you wanna go? \nnorth\neast\nwest\nsouth\n-> ')
                        current_room = current_room.move(command)
                    else:
                        print ('\n','Backpack: '+ ''.join(backpack),'\n--------------------')
                        command = input("Where do you wanna go? \nnorth\neast\nwest\nsouth\n-> ")
                        current_room = current_room.move(command)
                else:
                    dave.fight('wrong')
                    print("YOU'RE DEAD!!\nGAME OVER")
            else:
                dave.describe()
                print ("You didn't take the gift from Passos and now you can't defeat Dave!")
                dave.fight('wrong')
                print("YOU'RE DEAD!!\nGAME OVER")
    
    if not ", sweatshirt" in backpack:
        dead == False           
    
    if current_room == ballroom:
        print ('\n')
        current_room.get_details()
        if ', key' in backpack:
            print("Edu isn't anymore.")
            command = input ('Wich direction you wanna go? \nnorth\neast\nwest\nsouth\n-> ')
            current_room = current_room.move(command)
        elif ", sweatshirt" in backpack:
            Edu.describe()
            command = input('What you wanna do?\nMove to other room. (press 1)      Talk to Edu. (press 2)\n-> ')
            if command == '1':
                command = input ('Wich direction you wanna go? \nnorth\neast\nwest\nsouth\n-> ')
                current_room = current_room.move(command)
            else:
                Edu.talk()
                print (" \nEdu is very cold. Maybe you have ")
                Edu.set_conversation(None)
                Edu.set_conversation("Do you have anything that can warm me up?? I have one thing that may interrest you.")
                Edu.talk()
                command = input('Trade with Edu?\nYes(1)      No(2)\n-> ')
                if command == '1':
                    Edu.set_conversation(None)
                    Edu.set_conversation("[You says]: OMG!! Finally I have a sweatshirt to warm me up!! Here a key I promess to give to you.")
                    Edu.talk()
                    backpack.remove(', sweatshirt')
                    backpack.append(', key')
                    key.describe()
                    print ('The sweatshirt was removed from your backpack.\nA key was added to your backpack')
                    command = input ('What now?\nGo to other room?(1)      See backpack(2)\n-> ')
                    if command == '1':
                        command = input("Do you want to say goodbye to Edu?\nYes, give him a hug.(1)      No(2)\n-> ")
                        if command == '1':
                            Edu.hug()
                            command = input ('Where you wanna go now? \nnorth\neast\nwest\nsouth\n-> ')
                            current_room = current_room.move(command)
                        else:
                            print('You made Edu sad :(\nHe ran away.')
                    else:
                        print ('\n','Backpack: '+ ''.join(backpack),'\n--------------------')
                        print ("Edu said goodbye and went away.")
                        command = input("Where do you wanna go? \nnorth\neast\nwest\nsouth\n-> ")
                        current_room = current_room.move(command)
                else:
                    print("Now besides feeling cold Edu is also sad:(")
                    command = input ('Wich direction you wanna go? \nnorth\neast\nwest\nsouth\n-> ')
                    current_room = current_room.move(command)
        else:
            Edu.describe()
            print("You don't have anything that Edu is interrest by.")
            command = input ('Wich direction you wanna go? \nnorth\neast\nwest\nsouth\n-> ')
            current_room = current_room.move(command)
    
    if current_room == exit:
        print('\n')
        current_room.get_details()
        if ', key' in backpack:
            print("Probably the key Edu gave to me will open it.")
            command = input("Use the key to open the door?\nYes(1)      No(2)\n-> ")
            if command == '1':
                print("You opened the Passos's Castle's door and are finally free!!")
                print("THE END")
            else:
                command = 'north'
                current_room = current_room.move(command)
        else:
            print("This is the exit of the castle but you don't have the key. Go ga back find it")
            command = 'north'
            current_room = current_room.move(command)
            
if dead == False:
    print('GAME OVER')

RPGInfo.author = "Igor Righi"
RPGInfo.credits()