import sys


class Faction:
    def __init__(self, name="default", unit_num=50, attack_point=30, health_point=150, reg_num=10):
        self.name = name,
        self.unit_num = unit_num
        self.attack_point = attack_point
        self.health_point = health_point
        self.reg_num = reg_num
        self.total_health = unit_num * reg_num
        self.is_alive = True
    
    def AssgnEnemies(self, first_enemy, second_enemy):
        self.first_enemy = first_enemy
        self.second_enemy = second_enemy

    def PerformAttack(self):
        return self.unit_num * self.attack_point * 100

    def ReceiveAttack(self, damage):
        self.unit_num -= damage

    def PurchaseWeapons(self, increase_attack, profit):
        self.increase_attack = increase_attack
        return profit

    def PurchaseArmors(self, increase_health, profit):
        self.increase_health = increase_health
        return profit

    def Print(self):
        if(self.is_alive == True):
            status = True
        elif(self.is_alive == False):
            status = False

        print("Faction Name:/t/t" + self.name,
              "Status:/t/t" + status,
              "Number of Units:/t/t" + self.unit_num,
              "Attack Point:/t/t" + self.attack_point,
              "Health Point:/t/t" + self.health_point,
              "Unit Regen Number:/t/t" + self.reg_num,
              "Total Faction Health:/t/t" + self.total_health)      

    def EndTurn(self):
        if(self.unit_num < 0):
            self.unit_num = 0
        if(self.unit_num == 0):
            self.is_alive = False                             

#----------------------------------------

#----------------------------------------




class Orcs(Faction):
    def __init__(self, name = "Orcs"):
        super().__init__(name) 

    def PerformAttack(self):
        if(self.first_enemy.is_alive == True and self.second_enemy == False):
          self.first_enemy.ReceiveAttack(super().PerformAttack(), "Orcs")    

        elif(self.first_enemy.is_alive == False and self.second_enemy == True):
            self.second_enemy.ReceiveAttack(super().PerformAttack(), "Orcs")
        elif(self.first_enemy.is_alive == True and self.second_enemy == True):
            self.first_enemy.ReceiveAttack(super().PerformAttack()*0.7, "Elves")
            self.first_enemy.ReceiveAttack(super().PerformAttack()*0.3, "Dwarves")

        
    def ReceiveAttack(self, damage, obj):
        if obj == "Elwes":
            super().ReceiveAttack(0.75*(damage/self.health_point))
        elif obj == "Dwarves":
            super().ReceiveAttack(0.8*(damage/self.health_point))


    def PurchaseWeapon(self, weapon_point):
       self.attack_point += 2 * weapon_point
       gold = 20 * weapon_point

       return gold

    def PurchaseArmors(self, armor_points):
        self.armor_points += 3 * armor_points
        gold = armor_points

        return gold            

    def Print(self):
        print("Stop running, you’ll only die tired!")
        super().Print()
    
#-----------------------

#-----------------------


class Dwarves(Faction):
    def __init__(self, name="Dwarves"):
        super().__init__(name)

    def PerformAttack(self):
        if(self.first_enemy.is_alive == True and self.second_enemy.is_alive == False): #First enemy is Elves, Second enemy is Elves
            self.first_enemy.ReceiveAttack(super().PerformAttack(), "Dwarves")
        elif(self.first_enemy.i_alive == False and self.second_enemy.is_alive == True):
            self.second_enemy.ReceiveAttack(super().PerformAttack(), "Dwarves")    
        elif(self.first_enemy.is_alive == True and self.second_enemy.is_alive == True):
            self.first_enemy.ReceiveAttack(super().PerformAttack()/2, "Dwarves")
            self.second_enemy.ReceiveAttack(super().PerformAttack()/2, "Dwarves")    

    def ReceiveAttack(self, damage):
        return super().ReceiveAttack(damage/self.health_point)

    def PurchaseWeapons(self, weapon_points):
        self.attack_point += weapon_points

        gold = 10 * weapon_points

        return gold

    def PurchaseArmors(self, armor_point):
        self.health_point += armor_point

        gold = 3 * armor_point

        return gold

    def Print(self):
        print("Taste the power of our axes!")
        super().Print()

                
#---------------------

#---------------------

class Elves(Faction):
    def __init__(self, name="Elves"):
        super().__init__(name)

    def PerformAttack(self, health_point):  #First enemy is Orcs, Second enemy is Dwarves
        if(self.second_enemy == Dwarves):
            self.second_enemy.ReceiveAttack(super().PerformAttack, "Elves")
        elif(self.first_enemy.is_alive == True and self.second_enemy.is_alive == False):
            self.first_enemy.ReceiveAttack(super().PerformAttack, "Elves")
        elif(self.first_enemy.is_alive == False and self.second_enemy.is_alive == True):
            self.second_enemy.ReceiveAttack(super().PerformAttack, "Elves")
        elif(self.first_enemy.is_alive == True and self.second_enemy.is_alive == True):
            self.first_enemy.ReceiveAttack(super().PerformAttack * 0.6, "Elves")
            self.second_enemy.ReceiveAttack(super().PerformAttack * 0.4, "Elves")

    def ReceiveAttack(self, damage, enemy):
        if enemy == "Orcs":
            super().ReceiveAttack((damage/self.health_point) * 1.25)
        elif enemy == "Dwarves":
            super().ReceiveAttack((damage/self.health_point) * 0.75)


    def PurchaseWeapons(self, weapon_point):
        self.attack_point += 2 * weapon_point
        gold += 15 * weapon_point
        return gold

    def PurchaseArmors(self, armor_point):
        self.health_point += 4 * armor_point
        gold += 5 * armor_point
        return gold 

    def Print(self):
        print("You cannot reach our elegance.")
        super().Print()



#--------------------------

#--------------------------


class Merchant():
    def __init__(self, start_weapon = 10, start_armor = 10):
        self.start_weapon = start_weapon
        self.start_armor = start_armor
        self.revenue = 0

    def Assgnfaction(self, o, d, e):
        self.first_faction = o #Orcs
        self.second_faction = d #Dwarves
        self.third_faction = e #Elves

    def SellWeapons(self, to_whom, weapon_to_sell):
        if to_whom == "Orcs": to_whom = self.first_faction
        elif to_whom == "Dwarves": to_whom = self.second_faction
        elif to_whom == "Elves": to_whom = self.third_faction

        if(to_whom.is_alive == False):
            print("The faction you want to sell weapons is dead!")
        else:
            if(weapon_to_sell > self.weapon_left):
                print("You try to sell more weapons than you have in possession.") 

            else:
                self.revenue += to_whom.PurchaseWeapons(weapon_to_sell)
                print("Weapons sold!")
                self.weapon_left -= weapon_to_sell
                return True

    def SellArmors(self, to_whom, armor_to_sell):
        if to_whom == "Orcs": to_whom = self.first_faction
        elif to_whom == "Dwarves": to_whom = self.second_faction
        elif to_whom == "Elves": to_whom = self.third_faction

        if(to_whom.is_alive == False):
            print("The faction you want to sell armors is dead!")
        else:
            if(armor_to_sell > self.armor_left):
                print("You try to sell more armors than you have in possession.") 

            else:
                self.revenue += to_whom.PurchaseWeapons(armor_to_sell)
                print("Armors sold!")
                self.armor_left -= armor_to_sell
                return True

    def EndTurn(self):
        self.weapon_left = self.start_weapon
        self.armor_left = self.start_armor



