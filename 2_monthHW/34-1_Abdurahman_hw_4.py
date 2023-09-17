from enum import Enum
from random import randint, choice
from typing import Any


class SuperAbility(Enum):
    HEAL = 1
    CRITICAL_DAMAGE = 2
    BOOST = 3
    BLOCK_DAMAGE_AND_REVERT = 4


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} HEALTH: {self.__health} DAMAGE: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage ):
        super().__init__(name, health, damage)
        self.__defence = None
        self.__stun = False

    @property
    def stun(self):
        return self.__stun

    @stun.setter
    def stun (self, value):
        self.__stun = value

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self):
        abilities_list = [e for e in SuperAbility]
        self.__defence = choice(abilities_list)

    def attack(self, heroes ):
        for hero in heroes:
            if hero.health > 0:
                if type(hero) == Berserk and self.__defence != SuperAbility.BLOCK_DAMAGE_AND_REVERT:
                    hero.blocked_damage = self.damage // 5
                    hero.health -= self.damage - hero.blocked_damage
                else:
                    hero.health -= self.damage

    def __str__(self):
        return (f'BOSS "{self.name}" HEALTH: {self.health} '
                f'DAMAGE: {self.damage} DEFENCE: {self.__defence} STUNNED: {self.__stun}')


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        if type(ability) == SuperAbility:
            self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        if self.health > 0 and boss.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coeff = randint(1, 4)
        boss.health -= self.damage * coeff
        print(f'Warrior {self.name} hits critically {self.damage * coeff}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and boss.health > 0 and type(hero) != Witcher:
                hero.damage += 10


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero and type(hero) != Ghoust:
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BLOCK_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        boss.health -= self.__blocked_damage

class Thor(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE )

    def apply_super_power(self, boss, heroes):
        super_punch = randint(1, 6)
        if super_punch == 3:
            boss.damage = 0
            boss.stun = True
            print(f'Boss {boss.name} оглушен героем {self.name} на 1 раунд ')
        else:
            boss.stun = False
            boss.damage = 60

class Witcher(Hero):
    def __init__(self, name, health, damage, chance):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__chance = chance

    def apply_super_power(self, boss, heroes):

        revive = randint(1,15)
        choice_hero = [hero for hero in heroes if hero.health <= 0 ]
        if revive <= self.__chance and choice_hero:
            revive_hero = choice(choice_hero)
            revive_hero.health = self.health
            self.health = 0
            print(f'{self.name} оживил товарища {revive_hero.name} пожертвовам собой ')

class Samurai(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        shurikens = randint(1,2) # оказывается рандом считает последнию цифру
        virus = 25
        heal = 15
        if shurikens == 1 :
            boss.health -= virus
            print('Virus actived')
        elif shurikens == 2 :
            boss.health += heal
            print(f'Oops, + {heal} health Boss')


#My hero №1
class Ghoust(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    # Способность неуезвимость к атакам босса и критическая атака на 1 раунд
    def apply_super_power(self, boss, heroes):
        spirit = randint(1,7)
        if spirit == 5 :
            self.health += boss.damage
            boss.health - (self.damage * 1.5)
            print('The Ghoust Among Us')
            print(f'Ghoust {self.name} hits critically {self.damage * 1.5}')
            self.damage / 1.5


#My hero #2
class GigaChad(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BOOST)


    def apply_super_power(self, boss, heroes):
        power = randint(1,100)
        if power <= 3:
            boss.health = 0
            self.health = 100000
            self.damage = 100000
            print(f'{self.name} превратился в GigaChad -а и своей харизмой и увереностью довибвает Босса {boss.name}')
            print('''⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠋⠉⠈⠉⠉⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿
⣿⣿⣿⣿⡏⣀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿
⣿⣿⣿⢏⣴⣿⣷⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿
⣿⣿⣟⣾⣿⡟⠁⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣷⢢⠀⠀⠀⠀⠀⠀⠀⢸⣿
⣿⣿⣿⣿⣟⠀⡴⠄⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⣿
⣿⣿⣿⠟⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⢴⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⣿
⣿⣁⡀⠀⠀⢰⢠⣦⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⡄⠀⣴⣶⣿⡄⣿
⣿⡋⠀⠀⠀⠎⢸⣿⡆⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⠗⢘⣿⣟⠛⠿⣼
⣿⣿⠋⢀⡌⢰⣿⡿⢿⡀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣧⢀⣼
⣿⣿⣷⢻⠄⠘⠛⠋⠛⠃⠀⠀⠀⠀⠀⢿⣧⠈⠉⠙⠛⠋⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣧⠀⠈⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⢀⢃⠀⠀⢸⣿⣿⣿⣿
⣿⣿⡿⠀⠴⢗⣠⣤⣴⡶⠶⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡸⠀⣿⣿⣿⣿
⣿⣿⣿⡀⢠⣾⣿⠏⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠀⣿⣿⣿⣿
⣿⣿⣿⣧⠈⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿
⣿⣿⣿⣿⡄⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣦⣄⣀⣀⣀⣀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠙⣿⣿⡟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠁⠀⠀⠹⣿⠃⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠿⠛⠉⠉⠁⠀⢻⣿⡇⠀⠀⠀⠀⠀⠀⢀⠈⣿⣿⡿⠉⠛⠛⠛⠉⠉
⣿⡿⠋⠁⠀⠀⢀⣀⣠⡴⣸⣿⣇⡄⠀⠀⠀⠀⢀⡿⠄⠙⠛⠀⣀⣠⣤⣤
''')


round_number = 0


def start():
    boss = Boss('Fiofan', 4500, 60)
    warrior_1 = Warrior('Fiokl', 280, 25)
    warrior_2 = Warrior('Batman', 290, 20)
    magic = Magic('Harry', 270, 20)
    doc = Medic('Hipocrat', 230, 10, 20)
    assistant = Medic('Stajer', 250, 15, 10) # тут вообще игра цифр произошло , хотел что был баланс :)
    berserk = Berserk('Viking', 350, 20)
    thor = Thor('Thor', 320, 30)
    witcher = Witcher('Rudeus', 250, 0, 10)
    ronin = Samurai('Maks', 270, 20)
    ghoust = Ghoust('Wolfert', 340, 25)
    human = GigaChad('Халимов', 200, 5)

    heroes_list = [warrior_1, warrior_2, magic, doc, assistant, berserk, thor, witcher, ronin, ghoust, human]

    show_stats(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


def show_stats(boss, heroes):
    print(f'\nROUND {round_number} ----------------')
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence()
    boss.attack(heroes)
    for hero in heroes:
        if (boss.defence != hero.ability and
                hero.health > 0 and boss.health > 0):
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_stats(boss, heroes)


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
        return True
    return False


start()
