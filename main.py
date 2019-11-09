from classes.game import player
from classes.items import items
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





player_1 = player("Brock Lesnar",300,50,24,"F5")
player_2 = player("Rock",200,50,30,"Rock Bottom")
player_3 = player("Undertaker",300,50,39,"Tombstone")
player_4 = player("Randy Orton",260,50,22,"RKO")
player_5 = player("Rey Mysterio",297,50,28,"619")
player_6 = player("Kane",206,50,27,"ChokeSlam")
player_7 = player("Big Show",242,50,25,"ShowStopper")
player_8 = player("Rikishi",280,80,40,"Ass to Face")
player_9 = player("Triple H",283,50,32,"Pedigree")
player_10 = player("John Cena",223,50,37,"Attitude Adjustment")
player_11 = player("Batista",299,50,12,"Batista Bomb")
player_12 = player("Roman Reigns",236,50,33,"Spear")
player_13 = player("Kofi Kingston",244,50,16,"S.O.S")
player_14 = player("Great Khali",210,50,35,"Vise Grip")
player_15 = player("Stone Cold",259,50,21,"Stone Cold Stunner")
player_16 = player("Jeff Hardy",220,50,18,"The Swanton Bomb")
player_17 = player("Shawn Michaels",265,50,39,"Sweet Chin Music")
player_18 = player("Shemas",201,50,20,"Brogue Kick")
player_19 = player("Sincara",218,50,23,"Moonsault Side Slam")
player_20 = player("Kurt Angle",274,50,29,"Angle Slam")



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
    elif n == 'Shemus':
        u=17
    elif n == 'Sincare':
        u=18
    elif n == 'Kurt Angle':
        u=19
    return u

#boxes for storing the number of player and enemy that we got from the above functions
box1=choose_Player()
box2=choose_Opponent()

player_name="null"
opponent_name="null"

#for storing the name of the chosen player
def name_Of_Player():
    if box1==1:
        player_name=player_1
    elif box1==2:
        player_name=player_2
    elif box1==3:
        player_name=player_3
    elif box1==4:
        player_name=player_4
    elif box1==5:
        player_name=player_5
    elif box1==6:
        player_name=player_6
    elif box1==7:
        player_name=player_7
    elif box1==8:
        player_name=player_8
    elif box1==9:
        player_name=player_9
    elif box1==10:
        player_name=player_10
    elif box1==11:
        player_name=player_11
    elif box1==12:
        player_name=player_12
    elif box1==13:
        player_name=player_13
    elif box1==14:
        player_name=player_14
    elif box1==15:
        player_name=player_15
    elif box1==16:
        player_name=player_16
    elif box1==17:
        player_name=player_17
    elif box1==18:
        player_name=player_18
    elif box1 == 19:
        player_name = player_19
    elif box1 == 20:
        player_name = player_20
    return player_name

name_Of_Player()

def name_Of_Opponent():
    if box2==1:
        opponent_name=player_1
    elif box2==2:
        opponent_name=player_2
    elif box2==3:
        opponent_name=player_3
    elif box2==4:
        opponent_name=player_4
    elif box2==5:
        opponent_name=player_5
    elif box2==6:
        opponent_name=player_6
    elif box2==7:
        opponent_name=player_7
    elif box2==8:
        opponent_name=player_8
    elif box2==9:
        opponent_name=player_9
    elif box2==10:
        opponent_name=player_10
    elif box2==11:
        opponent_name=player_11
    elif box2==12:
        opponent_name=player_12
    elif box2==13:
        opponent_name=player_13
    elif box2==14:
        opponent_name=player_14
    elif box2==15:
        opponent_name=player_15
    elif box2==16:
        opponent_name=player_16
    elif box2==17:
        opponent_name=player_17
    elif box2==18:
        opponent_name=player_18
    elif box2==19:
        opponent_name= player_19
    elif box2==20:
        opponent_name=player_20
    return opponent_name

name_Of_Opponent()


def generate_Finisher(i):
   return finisher[i]['power']


def hit_Object(self):
    name_Of_Opponent().take_Damage()

list_of_Items=['Hammer','Table','Chair','Rod','Stairs']

running = True
print("YOUR HEALTH : ", name_Of_Player().get_HP(), "\nENEMY HEALTH : ", name_Of_Opponent().get_HP())

while running == True:

    print(" ")
    dmg = name_Of_Opponent().generate_Damage()
    name_Of_Player().take_Damage(dmg)
    #checking health if its less than 20.. if we found then we change it to 20 coz we dont want negatives or zero
    name_Of_Player().modify_Health()
    print("Opponent Attacked With Points: ", dmg)
    time.sleep(2)
    print("YOUR HEALTH : ", name_Of_Player().get_HP(), "\nENEMY HEALTH : ", name_Of_Opponent().get_HP())
    time.sleep(1)
    print("")
    #checking if health is low and that if the games needs to be paused
    guess = name_Of_Player().health_Is_Low()
    if guess == True:
        #displaying low health message
       name_Of_Player().low_Health_Message()
       running = False
    else:
        type_choice = name_Of_Player().choose_Action()
        print("")

        if type_choice == 1:

            print("There following objects available to help you with attack")
            o=1
            for item in list_of_Items:
                print(o,item)
                o+=1
            object_choice = int(input("Which object you wish to choose enter 0 to continue without object? Enter number: "))
            if object_choice==1:
                name_Of_Opponent().take_Damage(hammer.get_Item_Points())
                print("You Attacked With Points", hammer.get_Item_Points())

            elif object_choice==2:
                name_Of_Opponent().take_Damage(table.get_Item_Points())
                print("You Attacked With Points", table.get_Item_Points())
                time.sleep(2)
                print("YOUR HEALTH : ", name_Of_Player().get_HP(), "\nENEMY HEALTH : ", name_Of_Opponent().get_HP())

            elif object_choice==3:
                name_Of_Opponent().take_Damage(chair.get_Item_Points())
                print("You Attacked With Points", chair.get_Item_Points())
                time.sleep(2)
                print("YOUR HEALTH : ", name_Of_Player().get_HP(), "\nENEMY HEALTH : ", name_Of_Opponent().get_HP())

            elif object_choice==4:
                name_Of_Opponent().take_Damage(rod.get_Item_Points())
                print("You Attacked With Points", rod.get_Item_Points())
                time.sleep(2)
                print("YOUR HEALTH : ", name_Of_Player().get_HP(), "\nENEMY HEALTH : ", name_Of_Opponent().get_HP())
            elif object_choice == 5:
                name_Of_Opponent().take_Damage(rod.get_Item_Points())
                print("You Attacked With Points", rod.get_Item_Points())
                time.sleep(2)
                print("YOUR HEALTH : ", name_Of_Player().get_HP(), "\nENEMY HEALTH : ", name_Of_Opponent().get_HP())

            elif object_choice==0:
                continue
            name_Of_Opponent().modify_Health()
            dmg1 = name_Of_Player().generate_Damage()
            name_Of_Opponent().take_Damage(dmg1)
            print("You Attacked With Points", dmg1)
            time.sleep(2)
            print("YOUR HEALTH : ", name_Of_Player().get_HP(), "\nENEMY HEALTH : ", name_Of_Opponent().get_HP())
            time.sleep(1)
            print("")
            guess = name_Of_Opponent().health_Is_Low()
            if guess == True:
                print("You Just Defeated this",name_Of_Opponent().get_Name()," CONGRATS YOU WON..!!!!",name_Of_Player().get_Name())
                running = False

        elif type_choice == 2:

            index=int(finisher_Number(name_Of_Player().name))
            name_Of_Opponent().modify_Health()
            print(finisher[index]['message'])
            dmg1 = generate_Finisher(index)
            name_Of_Opponent().take_Damage(dmg1)
            print("You Attacked With Points", dmg1)
            time.sleep(2)
            print("YOUR HEALTH : ", name_Of_Player().get_HP(), "\nENEMY HEALTH : ", name_Of_Opponent().get_HP())
            time.sleep(1)
            print("")
            guess = name_Of_Opponent().health_Is_Low()
            if guess == True:
                print("You Just Defeated ",name_Of_Opponent().get_Name(),".... CONGRATS YOU WON..!!!!", name_Of_Player().get_Name())
                running = False








