from typing import Optional

from unit import BaseUnit

class BaseSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Arena(metaclass=BaseSingleton):
    STAMINA_PER_ROUND = 1
    player = None
    enemy = None
    game_is_running = False

    def start_game(self, player: BaseUnit, enemy: BaseUnit) -> None:
        self.player = player
        self.enemy = enemy
        self.game_is_running = True

    def _check_players_hp(self) -> Optional[str]:
        self.battle_result = None
        if self.player.hp <= 0 and self.enemy.hp <= 0:
            self.battle_result = "Ничья"
        elif self.enemy.hp <= 0:
            self.battle_result = f"{self.player.name} победил!"
        elif self.player.hp <= 0:
            self.battle_result = f"{self.enemy.name} победил!"
        if self.battle_result is not None:
            return self._end_game()


    def _stamina_regeneration(self):
        if self.player.stamina + Arena.STAMINA_PER_ROUND < self.player.unit_class.max_stamina:
            self.player.stamina += Arena.STAMINA_PER_ROUND
        if self.enemy.stamina + Arena.STAMINA_PER_ROUND < self.enemy.unit_class.max_stamina:
            self.enemy.stamina += Arena.STAMINA_PER_ROUND


    def next_turn(self):
        result = self._check_players_hp()
        self._stamina_regeneration()
        if result:
            return result
        if self.game_is_running:
            return self.enemy.hit(self.player)

    def _end_game(self) -> str:
        self._instances = {}
        result = f"{self.battle_result}"
        self.game_is_running = False
        return result

    def player_hit(self):
        result = self.player.hit(self.enemy)
        turn_result = self.next_turn()
        return f"{result}\n{turn_result}"

    def player_use_skill(self):
        result = self.player.use_skill(self.enemy)
        turn_result = self.next_turn()
        return f"{result}\n{turn_result}"