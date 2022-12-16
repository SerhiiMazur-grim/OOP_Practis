from random import choice
from settings import INITIAL_PLAYER_HEALTH, HEROES, EXIT, ENEMY_LEVEL
from exeptions import EnemyDown, GameOver
import sys


class Enemy:
    def __init__(self) -> None:
        self.level = ENEMY_LEVEL
        self.health = self.level

    def first_level_enemy(self) -> None:
        self.level = ENEMY_LEVEL
        self.health = self.level

    def decrease_health(self) -> None:
        self.health = self.health - 1
        if self.health == 0:
            self.level += 1
            self.health = self.level
            raise EnemyDown(self.level - 1)

    def select_attack(self) -> str:
        return choice(HEROES)

    def select_defence(self) -> str:
        return choice(HEROES)


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.health = INITIAL_PLAYER_HEALTH
        self.score = 0

    @staticmethod
    def stop_game() -> None:
        sys.exit()

    def play_again(self) -> None:
        while True:
            yes_no = str(input("\nDo you want to try again? (Yes/No): ")).strip().lower()
            if yes_no == "no" or yes_no == "n":
                self.stop_game()
            elif yes_no == "yes" or yes_no == "y":
                self.health = INITIAL_PLAYER_HEALTH
                self.score = 0
                break
            else:
                print("\nWrong input!")

    def write_score(self) -> None:
        player_points = f"{self.name} --->>> {self.score}"
        with open("scores.txt", "a+", encoding="utf=8") as f:
            f.write(player_points)
            f.write("\n")

    def decrease_health(self) -> None:
        self.health = self.health - 1
        if self.health == 0:
            raise GameOver(self.name, self.score)

    def select_attack(self) -> str:
        while True:
            player_select = str(input(f"\nInput 'Exit' for stop game!"
                                      f"\n{self.name} choose your hero for attack "
                                      f"(Warrior, Robber, Wizard): ")).strip().lower()
            if player_select == EXIT:
                self.stop_game()
            if player_select in HEROES:
                return player_select
            print("\nWrong input!")

    def select_defence(self) -> str:
        while True:
            player_select = str(input(f"\nInput 'Exit' for stop game!"
                                      f"\n{self.name} choose your hero for defence "
                                      f"(Warrior, Robber, Wizard): ")).strip().lower()
            if player_select == EXIT:
                self.stop_game()
            if player_select in HEROES:
                return player_select
            print("\nWrong input!")

    @staticmethod
    def fight(player, enemy: Enemy) -> str:
        if player == enemy:
            return "draw"
        elif player == "warrior" and enemy == "robber":
            return "win"
        elif player == "robber" and enemy == "wizard":
            return "win"
        elif player == "wizard" and enemy == "warrior":
            return "win"
        else:
            return "lose"

    def attack(self, enemy: Enemy) -> None:
        attack = self.select_attack()
        defence = enemy.select_defence()
        battle = self.fight(attack, defence)

        if battle == "win":
            try:
                enemy.decrease_health()
                self.score += 1
                print("\nYOUR ATTACK IS SUCCESSFUL!\nYou get 1 points")
            except EnemyDown:
                self.score += 2
                raise
        elif battle == "draw":
            print("\nIT'S A DRAW!")
        else:
            print("\nYOUR ATTACK IS FAILED!")

    def defence(self, enemy: Enemy) -> None:
        defence = self.select_defence()
        attack = enemy.select_attack()
        battle = self.fight(defence, attack)

        if battle == "win":
            print("\nYOUR DEFENCE IS SUCCESSFUL!")
        elif battle == "draw":
            print("\nIT'S A DRAW!")
        else:
            self.decrease_health()
            print(f"\nYOUR DEFENCE IS FAILED!\nYou have {self.health} hit points left!")








