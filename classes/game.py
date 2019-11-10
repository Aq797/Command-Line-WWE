import random
class player:
    def __init__(self,name,health,defence,atk,finisher):
        self.name=name
        self.ply_health=health
        self.ply_defence=defence
        self.atk_l=atk-5
        self.atk_h=atk+5
        self.finisher=finisher
        self.action=['Attack','Finisher']

    def choose_Action(self):
        v=1
        for i in self.action:
            print(v,i)
            v+=1
        choice=int(input("Enter your choice number"))
        return choice


    def generate_Damage(self):
        return random.randrange(self.atk_l,self.atk_h)

    def take_Damage(self,dmg1):
        running1 = True
        while running1 == True:
            if self.ply_health <= 20:
                self.ply_health = 20
                running1 = False
            else:
                self.ply_health = self.ply_health - dmg1
                break


    def do_Finisher(self,i):
        move=self.finisher[i]["power"]
        self.ply_health=self.ply_health-move


    def return_Health(self):
        return self.ply_health

    def get_HP(self):
        return self.ply_health

    def get_Name(self):
        return self.name

    def health_Is_Low(self):
        if self.ply_health<=20:
            return True
        else:
            return False

    def low_Health_Message(self):
        if self.health_Is_Low()==True:
            print("Critical Health: ", self.ply_health)
            print(self.name, "Its over dude u just lost")
            print("You are being transferred to the nearest Hospital to get your shit okay")

    def modify_Health(self):
        if self.health_Is_Low()==True:
            self.ply_health=20

