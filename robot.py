import random 

class Robot : 
    def __init__(self, name, hp, attack) : 
        self.name = name 
        self.hp = hp 
        self.attack = attack 
        self.defense = 0 

    def attack_enemy(self, enemy) : 
        if self.attack > enemy.defense :
            damage = self.attack - enemy.defense 
            enemy.hp -= damage 
            print(f"{enemy.name} menerima {damage} damage ")
        else : 
            print(f"{self.name} gagal menyerang ")
    
    def regen_health(self) : 
        regen = random.randint(10, 30)
        self.hp += regen 
        print(f"{self.name} mendapat {regen} HP")

    def defend(self) :
        self.defense = random.randint(5,15) 
        print(f"{self.name} meningkatkan pertahanan-nya")
    
    def get_status(self) :
        return f"{self.name} [{self.hp} | {self.attack}]"

    
