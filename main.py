from classes.game import player
from classes.items import items
import random
import time
print("""
************************************************************************************************************************
WELCOME TO COMMAND-LINE WRESTLING GAME
COPYRIGHT(C) 2019 SHAIKH AQUIB
************************************************************************************************************************
""")
print("STARTING...")
time.sleep(3)
finisher=[{"name":"F5","power":144,"message":"+++ Here Comes Brock Lesnar +++ \nBANG..!!"},
          {"name":"Rock Bottom","power":147,"message":"+++ Here Comes The RockBottom +++ \nBANG..!!"},
          {"name":"Tombstone","power":150,"message":"+++ Here Comes The UnderTaker +++ \nBANG..!!"},
          {"name":"RKO","power":148,"message":"+++ Here Comes The RKO +++ \nBANG..!!"},
          {"name":"619","power":100,"message":"+++ Here Comes 619 +++ \nBANG..!!"},
          {"name":"ChokeSlam","power":133,"message":"+++ Here Comes The ChokeSlam +++ \nBANG..!!"},
          {"name":"ShowStopper","power":141,"message":"+++ Here Comes The ShowStopper +++ \nBANG..!!"},
          {"name":"Ass to Face","power":137,"message":"+++ Here Comes The Ass to Face +++ \nBANG..!!"},
          {"name":"Pedigree","power":142,"message":"+++ Here Comes The Pedigree +++ \nBANG..!!"},
          {"name":"Attitude Adjustment","power":124,"message":"+++ Here Comes The Attitude Adjustment +++ \nBANG..!!"},
          {"name":"Batista Bomb","power":131,"message":"+++ Here Comes The Batista Bomb +++ \nBANG..!!"},
          {"name":"Spear","power":122,"message":"+++ Here Comes The Spear +++ \nBANG..!!"},
          {"name":"S.O.S","power":143,"message":"+++ Here Comes The S.O.S +++ \nBANG..!!"},
          {"name":"Vise Grip","power":113,"message":"+++ Here Comes The Great Khali +++ \nBANG..!!"},
          {"name":"Stone Cold Stunner","power":149,"message":"+++ Here Comes The Steve Austin +++ \nBANG..!!"},
          {"name":"The Swanton Bomb","power":136,"message":"+++ Here Comes The Swanton Bomb +++ \nBANG..!!"},
          {"name":"Sweet Chin Music","power":114,"message":"+++ Here Comes The Shawn Michaels +++ \nBANG..!!"},
          {"name":"Brogue Kick","power":108,"message":"+++ Here Comes The Kick +++ \nBANG..!!"},
          {"name":"Moonsault Side Slam","power":139,"message":"+++ Here Comes The Moonsault Slam +++ \nBANG..!!"},
          {"name":"Angle Slam","power":120,"message":"+++ Here Comes The Angle Slam +++ \nBANG..!!"}]





player_1 = player("Brock Lesnar",600,50,24,"F5")
player_2 = player("Rock",600,50,30,"Rock Bottom")
player_3 = player("Undertaker",600,50,39,"Tombstone")
player_4 = player("Randy Orton",600,50,22,"RKO")
player_5 = player("Rey Mysterio",600,50,28,"619")
player_6 = player("Kane",600,50,27,"ChokeSlam")
player_7 = player("Big Show",600,50,25,"ShowStopper")
player_8 = player("Rikishi",600,80,40,"Ass to Face")
player_9 = player("Triple H",600,50,32,"Pedigree")
player_10 = player("John Cena",600,50,37,"Attitude Adjustment")
player_11 = player("Batista",600,50,12,"Batista Bomb")
player_12 = player("Roman Reigns",600,50,33,"Spear")
player_13 = player("Kofi Kingston",600,50,16,"S.O.S")
player_14 = player("Great Khali",600,50,35,"Vise Grip")
player_15 = player("Stone Cold",600,50,21,"Stone Cold Stunner")
player_16 = player("Jeff Hardy",600,50,18,"The Swanton Bomb")
player_17 = player("Shawn Michaels",600,50,39,"Sweet Chin Music")
player_18 = player("Shemas",600,50,20,"Brogue Kick")
player_19 = player("Sincara",600,50,23,"Moonsault Side Slam")
player_20 = player("Kurt Angle",600,50,29,"Angle Slam")



hammer = items("Hammer","Object","Used to Hit Enemy",70)
table = items("Table","Object","Can be used with finishers",40)
chair = items("Chair","Object","Used for sitting and hitting",50)
rod = items("Rod","Object","Used for Hitting",45)
stairs = items("stairs","Object","Used for Hitting",57)

#list for storing the names of players
nameDict=[]
nameDict.append(player_1.get_Name())
nameDict.append(player_2.get_Name())
nameDict.append(player_3.get_Name())
nameDict.append(player_4.get_Name())
nameDict.append(player_5.get_Name())
nameDict.append(player_6.get_Name())
nameDict.append(player_7.get_Name())
nameDict.append(player_8.get_Name())
nameDict.append(player_9.get_Name())
nameDict.append(player_10.get_Name())
nameDict.append(player_11.get_Name())
nameDict.append(player_12.get_Name())
nameDict.append(player_13.get_Name())
nameDict.append(player_14.get_Name())
nameDict.append(player_15.get_Name())
nameDict.append(player_16.get_Name())
nameDict.append(player_17.get_Name())
nameDict.append(player_18.get_Name())
nameDict.append(player_19.get_Name())
nameDict.append(player_20.get_Name())



#function to choose player and enemy
def choose_Player():
    n=1
    for i in nameDict:
        print(n,i)
        n+=1
    choice=int(input("Enter the number of the player you want"))
    return choice

def choose_Opponent():
    choice=int(input("Enter the number of the opponent you want"))
    return choice

def generate_Random_Number(s,e):
    return random.randrange(s,e)

def finisher_Number(n):
    if n == 'Brock Lesnar':
        u=0
    elif n == 'Rock':
        u=1
    elif n == 'Undertaker':
        u=2
    elif n == 'Randy Orton':
        u=3
    elif n == 'Rey Mysterio':
        u=4
    elif n == 'Kane':
        u=5
    elif n == 'Big Show':
        u=6
    elif n == 'Rikishi':
        u=7
    elif n == 'Triple H':
        u=8
    elif n == 'John Cena':
        u=9
    elif n == 'Batista':
        u=10
    elif n == 'Roman Reigns':
        u=11
    elif n == 'Kofi Kingston':
        u=12
    elif n == 'Great Khali':
        u=13
    elif n == 'Stone Cold':
        u=14
    elif n == 'Jeff Hardy':
        u=15
    elif n == 'Shawn Michaels':
        u=16
    elif n == 'Shemas':
        u=17
    elif n == 'Sincara':
        u=18
    elif n == 'Kurt Angle':
        u=19
    return u

#boxes for storing the number of player and enemy that we got from the above functions
box1=choose_Player()
box2=choose_Opponent()
box3=generate_Random_Number(1,21)

player_name="null"
opponent_name="null"
partner_name="null"
#for storing the name of the chosen player
def generate_Player_Name(selection_of_flag,var_selection):
    if selection_of_flag==1:
        var_selection=player_1
    elif selection_of_flag==2:
        var_selection=player_2
    elif selection_of_flag==3:
        var_selection=player_3
    elif selection_of_flag==4:
        var_selection=player_4
    elif selection_of_flag==5:
        var_selection=player_5
    elif selection_of_flag==6:
        var_selection=player_6
    elif selection_of_flag==7:
        var_selection=player_7
    elif selection_of_flag==8:
        var_selection=player_8
    elif selection_of_flag==9:
        var_selection=player_9
    elif selection_of_flag==10:
        var_selection=player_10
    elif selection_of_flag==11:
        var_selection=player_11
    elif selection_of_flag==12:
        var_selection=player_12
    elif selection_of_flag==13:
        var_selection=player_13
    elif selection_of_flag==14:
        var_selection=player_14
    elif selection_of_flag==15:
        var_selection=player_15
    elif selection_of_flag==16:
        var_selection=player_16
    elif selection_of_flag==17:
        var_selection=player_17
    elif selection_of_flag==18:
        var_selection=player_18
    elif selection_of_flag == 19:
        var_selection = player_19
    elif selection_of_flag == 20:
        var_selection = player_20
    return var_selection

name_of_player=generate_Player_Name(box1,player_name)
name_of_opponent=generate_Player_Name(box2,opponent_name)
name_of_partner=generate_Player_Name(box3,partner_name)


def generate_Finisher(i):
   return finisher[i]['power']

def print_Stats():
    print("")
    print("%s           %s"%(name_of_player.get_Name(),name_of_opponent.get_Name()))
    print(name_of_player.get_HP(),"\t\t\t",name_of_opponent.get_HP())



def Object_Attack(you,opponent,naemo):
    #you are the person who attacks and opponent is the one u wish to hit
    #naemo means the the string which will be used in print statement to either you or opponent
    #nothing deep just had no clue what else to keep the name
    if opponent==name_of_opponent:
        if you==name_of_partner:
            object_choice = generate_Random_Number(0, 6)
        else:
            object_choice = int(input("Which object you wish to choose enter 0 to continue without object? Enter number: "))
    elif opponent==name_of_player:
        object_choice = generate_Random_Number(0,6)
    elif opponent==name_of_partner:
        object_choice = generate_Random_Number(0, 6)

    if object_choice == 1:
        opponent.take_Damage(hammer.get_Item_Points())
        print(naemo," Used Hammer to Attack",opponent.get_Name()," With Points", hammer.get_Item_Points())

    elif object_choice == 2:
        opponent.take_Damage(table.get_Item_Points())
        print(naemo," Used Table to Attack",opponent.get_Name()," With Points", table.get_Item_Points())
        time.sleep(2)

    elif object_choice == 3:
        opponent.take_Damage(chair.get_Item_Points())
        print(naemo," Used Chair to Attack",opponent.get_Name()," With Points", chair.get_Item_Points())
        time.sleep(2)

    elif object_choice == 4:
        opponent.take_Damage(rod.get_Item_Points())
        print(naemo, " Used Rod to Attack",opponent.get_Name(), "With Points", rod.get_Item_Points())
        time.sleep(2)

    elif object_choice == 5:
        opponent.take_Damage(stairs.get_Item_Points())
        print(naemo, "Used Stairs to Attack",opponent.get_Name()," With Points", stairs.get_Item_Points())
        time.sleep(2)

    elif object_choice == 0:
        dmg = you.generate_Damage()
        opponent.take_Damage(dmg)
        print(naemo, " Attacked",opponent.get_Name(), "With Points", dmg)
        time.sleep(2)
#to make players enter the ring by cheating
def Cheating():
    cheating_Choice=random.randrange(0,2)
    if cheating_Choice==0:
        print("Come on fight Harder...!!")
    elif cheating_Choice==1:
        Opponent_Choice1 = generate_Random_Number(1, 3)
        print("Oh my God", name_of_partner.get_Name(), " has entered the ring... This is against the rules")
        if Opponent_Choice1 == 1:
            side_Choice=generate_Random_Number(1,3)
            if side_Choice==1:
                print("Oh my God he is trying to attack",name_of_opponent.get_Name())
                dmg3=name_of_partner.generate_Damage()
                name_of_opponent.take_Damage(dmg3)
                print(name_of_partner.get_Name()," Attacked the",name_of_opponent.get_Name(),"with points",dmg3)
                Object_Attack(name_of_partner, name_of_opponent, name_of_partner.get_Name())
            elif side_Choice==2:
                print("Oh my God he is trying to Attack ",name_of_player.get_Name())
                dmg3=name_of_partner.generate_Damage()
                name_of_player.take_Damage(dmg3)
                print(name_of_partner.get_Name(), " Attacked You with points", dmg3)
                Object_Attack(name_of_partner, name_of_player, name_of_partner.get_Name())

            print_Stats()
            print(name_of_partner.name, " Health: ",name_of_partner.get_HP())
        elif Opponent_Choice1 == 2:
            index11 = int(finisher_Number(name_of_partner.name))
            name_of_player.modify_Health()
            print(finisher[index11]['message'])
            dmg4 = generate_Finisher(index11)
            side_Choice2 = generate_Random_Number(1, 3)
            if side_Choice2==1:
                print("Oh my God he is trying to attack",name_of_opponent.get_Name())
                name_of_opponent.take_Damage(dmg4)
                print(name_of_partner.get_Name()," Attacked the",name_of_opponent.get_Name(),"with points",dmg4)
            elif side_Choice2==2:
                print("Oh my God he is trying to Attack ",name_of_player.get_Name())
                name_of_player.take_Damage(dmg4)
                print(name_of_partner.get_Name(), " Attacked You with points", dmg4)
            print_Stats()
            print(name_of_partner.name," Health: ",name_of_partner.get_HP())
            time.sleep(2)


list_of_Items=['Hammer','Table','Chair','Rod','Stairs']
chance=0
running = True
print_Stats()

while running == True:

    print(" ")
    Cheating()
    Opponent_Choiceo = generate_Random_Number(1, 3)
    if Opponent_Choiceo==1:
        Object_Attack(name_of_opponent,name_of_player,name_of_opponent.get_Name())
        print_Stats()
    elif Opponent_Choiceo==2:
        index = int(finisher_Number(name_of_opponent.name))
        name_of_player.modify_Health()
        print(finisher[index]['message'])
        dmg1 = generate_Finisher(index)
        name_of_player.take_Damage(dmg1)
        print("Enemy Attacked With Points", dmg1)
        print_Stats()
        time.sleep(2)
    #checking health if its less than 20.. if we found then we change it to 20 coz we dont want negatives or zero
    name_of_player.modify_Health()
    time.sleep(1)
    print("")
    #checking if health is low and that if the games needs to be paused
    guess = name_of_player.health_Is_Low()
    if guess == True:
        chance=chance+1
        if chance==1:
            name_of_player.ply_health=name_of_player.ply_health+80
            print("Giving You first time bonus of 80")
        else:
        #displaying low health message
            name_of_player.low_Health_Message()
            running = False
    else:
        type_choice = name_of_player.choose_Action()
        print("")

        if type_choice == 1:

            print("There following objects available to help you with attack")
            o=1
            for item in list_of_Items:
                print(o,item)
                o+=1
            Object_Attack(name_of_player,name_of_opponent,"You")
            name_of_opponent.modify_Health()
            print_Stats()
            print("")
            guess = name_of_opponent.health_Is_Low()
            if guess == True:
                print("You Just Defeated this",name_of_opponent.get_Name()," CONGRATS YOU WON..!!!!",name_of_player.get_Name())
                running = False

        elif type_choice == 2:

            index=int(finisher_Number(name_of_player.name))
            name_of_opponent.modify_Health()
            print(finisher[index]['message'])
            dmg1 = generate_Finisher(index)
            name_of_opponent.take_Damage(dmg1)
            print("You Attacked With Points", dmg1)
            time.sleep(2)
            print_Stats()
            time.sleep(1)
            print("")
            guess = name_of_opponent.health_Is_Low()
            if guess == True:
                print("You Just Defeated this", name_of_opponent.get_Name(), " CONGRATS YOU WON..!!!!",name_of_player.get_Name())
                running = False








