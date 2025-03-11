from robot import Robot 

class Game : 
    def __init__(self,robot1, robot2) :
        self.robot1 = robot1 
        self.robot2 = robot2 
        self.round = 1

    def play_round(self) : 
        print(f"Round-{self.round}")
        print(self.robot1.get_status())
        print(self.robot2.get_status())

        game_over = self.take_action (self.robot1)
        if game_over:
            return True

        game_over = self.take_action(self.robot2)
        if game_over:
            return True
        
        return False

    def take_action(self, robot):
        print("\n1. Attack     2. Defense     3. Giveup")
        action = int(input(f"{robot.name}, pilih aksi: "))

        action_is_attack = action == 1
        action_is_defend = action == 2
        action_is_giveup = action == 3
        
        if action_is_attack:
            if robot == self.robot1:
                robot.attack_enemy(self.robot2)
            else:
                robot.attack_enemy(self.robot1)
        action_is_defend and robot.defend()
        action_is_giveup and print(f"{robot.name} menyerah!") and True

        return action_is_giveup

    def start_game(self):
        while True:
            game_over = self.play_round()
            if game_over:
                break
            self.round += 1

if __name__ == "__main__":
    robot1 = Robot("Atreus", 500, 10)
    robot2 = Robot("Daedalus", 750, 8)

    game = Game(robot1, robot2)
    game.start_game()