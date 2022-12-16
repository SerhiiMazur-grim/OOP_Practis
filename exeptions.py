

class EnemyDown(Exception):
    def __init__(self, enemy_level: int) -> None:
        self.enemy_level = enemy_level

    def __str__(self) -> str:
        return f"\nCongratulations you have defeated a level {self.enemy_level} enemy!" \
               f"\nYou get 2 points"


class GameOver(Exception):
    def __init__(self, player_name: str, player_score: int) -> None:
        self.player_name = player_name
        self.player_score = player_score

    def __str__(self) -> str:
        return f"\nSorry {self.player_name} but you lost =( " \
               f"\nGame Over!" \
               f"\nYou have scored {self.player_score} points!"
