from models import Enemy, Player
from exeptions import EnemyDown, GameOver


def get_player_name() -> str:
    player_name = str()
    while len(player_name) == 0:
        player_name = str(input("Please enter your name: ")).strip()
    return player_name


def play() -> None:
    player_name = get_player_name()
    player = Player(player_name)
    enemy = Enemy()

    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except EnemyDown as exc:
            print(exc)
        except GameOver as exc:
            print(exc)
            player.write_score()
            player.play_again()
            enemy.first_level_enemy()


if __name__ == "__main__":
    play()
