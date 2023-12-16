from abc import ABC, abstractmethod


class Elf(ABC):

    def __init__(self, name, mus_instrument, favorite_song, hp):
        self.hp = hp
        self.name = name
        self.mus_instrument = mus_instrument
        self.favorite_song = favorite_song

    def play_song(self):
        print(f"Elf {self.name} playing {self.favorite_song} "
              f"on {self.mus_instrument}")

    @abstractmethod
    def fight(self, opponent):
        pass

    @abstractmethod
    def lvl_up(self):
        pass


class ElfRanger(Elf):

    def __init__(self, name, mus_instrument, favorite_song, hp, bow: dict):
        super().__init__(name, mus_instrument, favorite_song, hp)
        self.hp = hp
        self.damage = bow["damage"]
        self.bow = bow["name"]

    def fight(self, opponent):
        print(f"Elf {self.name} kills his opponent with {self.bow}")
        opp_damage = opponent.hp - self.damage
        print(opp_damage)

    def lvl_up(self):
        self.damage+=300
        self.hp+=1000
        print(f"Після посілення урон - {self.damage}, здоров'я - {self.hp}")

class Dverger(Elf):

    def __init__(self, name, mus_instrument, favorite_song, hp, bow: dict):
        super().__init__(name, mus_instrument, favorite_song, hp)
        self.hp = hp
        self.damage = bow["damage"]
        self.bow = bow["name"]

    def fight(self, opponent):
        print(f"Elf {self.name} kills his opponent with {self.bow}")
        opp_damage = opponent.hp - self.damage
        print(opp_damage)

    def lvl_up(self):
        self.damage+=3000
        self.hp+=1000
        print(f"Після посілення урон - {self.damage}, здоров'я - {self.hp}")


class Ogr(Elf):
    def __init__(self, name, mus_instrument, favorite_song, hp, sword: dict):
        super().__init__(name, mus_instrument, favorite_song, hp)
        self.damage = sword["damage"]
        self.sword = sword["name"]

    def fight(self, opponent):
        print(f"Elf {self.name} kills his opponent with {self.sword}")
        opp_damage = opponent.hp - self.damage
        print(opp_damage)

    def lvl_up(self):
        self.damage+=300
        self.hp+=1000
        print(f"Після посілення урон - {self.damage}, здоров'я - {self.hp}")


bob = ElfRanger("Bob",
                "lute",
                "Bad Romance",
                1500,
                {"name": "M249", "damage": 999})

nif_nif = Dverger("Nif Nif",
                  "No",
                  "No",
                  3000,
                  {"name": "A4", "damage": 1000})

wolf = Ogr("Oleg",
           "No",
           "No",
           300,
           {"name": "sword", "damage": 1})


bob.play_song()
bob.fight(nif_nif)
bob.lvl_up()
bob.fight(nif_nif)