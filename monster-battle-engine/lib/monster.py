class MonsterType:
    NORMAL = 0
    FIRE = 1
    GRASS = 2
    WATER = 3


class MoveType:
    PHYSICAL = 0
    SPECIAL = 1
    STATUS = 2


class Move:
    def __init__(self, name: str, monster_type: MonsterType, power_points: int, accuracy: int,
                 attack: int, move_type: MoveType):
        self.name = name
        self.monster_type = monster_type
        self.power_points = power_points

        self.accuracy = accuracy
        self.attack = attack
        self.move_type = move_type


class Monster:
    def __init__(self, name: str, level: int, monster_types: list[MonsterType], nature: str, ability: str,
                 speed: int, hp: int, attack: int, defense: int, sp_attack: int, sp_defense: int,
                 shiny = False, form = "default", moves: list[Move] = None):
        self.name = name
        self.level = level
        self.current_hp = hp
        self.monster_types = monster_types
        self.nature = nature
        self.friendship = 0
        self.ability = ability

        # EVs
        self.speed = speed
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense

        self.evasiveness = 0

        self.moves = [] if moves is None else moves

        self.shiny = shiny
        self.form = "default"
        self.virus = False

        self.status = None
        self.item = None
