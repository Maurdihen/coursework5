from dataclasses import dataclass

from skills import Skill, Berserker


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(
    name="Воин",
    max_health=60.0,
    max_stamina=30.0,
    attack=0.8,
    stamina=0.9,
    armor=1.2,
    skill=Berserker()
)
#
ThiefClass = UnitClass(
    name="Вор",
    max_health=50.0,
    max_stamina=25.0,
    stamina=1.2,
    attack=1.5,
    armor=1.0,
    skill=Berserker()
)

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}
