class Monster:

    def __init__(self, name, strength, health):
        self.name = name
        self.strength = strength

        self.health = health


plus_monster = Monster(
    "plus_monster",
    2,
    5
)

print(plus_monster.name)
print(plus_monster.strength)
print(plus_monster.health)