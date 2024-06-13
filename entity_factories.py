from components.ai import HostileEnemy
from components import consumable, equippable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=25, base_defense=1, base_power=3),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=250),
)

wraith = Actor(
    char="W",
    color=(144, 0, 255),
    name="Wraith",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=4, base_power=5),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=125),
)

human = Actor(
    char="@",
    color=(0, 0, 255),
    name="Human",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=3, base_power=5),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=75),
)


orc = Actor(
    char="o",
    color=(63, 127, 63),
    name="Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=15, base_defense=2, base_power=5),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50),
)

troll = Actor(
    char="T",
    color=(149, 163, 152),
    name="Troll",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=25, base_defense=3, base_power=10),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=75),
)

zombie = Actor(
    char="Z",
    color=(63, 127, 63),
    name="Zombie",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=25, base_defense=3, base_power=7),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=75),
)

kobold = Actor(
    char="K",
    color=(171, 39, 39),
    name="Kobold",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=1, base_power=30),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=75),
)

ogre = Actor(
    char="O",
    color=(63, 127, 63),
    name="Ogre",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=4, base_power=10),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50),
)

goblin = Actor(
    char="G",
    color=(63, 127, 63),
    name="Goblin",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=4, base_power=7),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50),
)

ghoul = Actor(
    char="g",
    color=(63, 127, 63),
    name="Ghoul",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=25, base_defense=1, base_power=8),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=75),
)

snake = Actor(
    char="S",
    color=(196, 27, 24),
    name="Snake",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=25),
)

psword = Actor(
    char="/",
    color=(0, 191, 255),
    name="Possessed Sword",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=4, base_defense=4, base_power=7),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=25),
)
""" cool idea
dummy = Actor(
    char="◉",
    color=(155, 103, 60),
    name="Training Dummy",
    ai_cls=IdkIDontHaveAnIdleAi,
    fighter=Fighter(hp=999999999, base_defense=0, base_power=0),
    equipment=Equipment(),
    inventory=Inventory(capacity=0),
)
"""

confusion_scroll = Item(
    char="~",
    color=(207, 63, 255),
    name="Scroll of Confusion",
    consumable=consumable.ConfusionConsumable(number_of_turns=15),
)

fireball_scroll = Item(
    char="~",
    color=(255, 0, 0),
    name="Scroll of Fire",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)

health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Potion of Healing",
    consumable=consumable.HealingConsumable(amount=5),
)

lightning_scroll = Item(
    char="~",
    color=(255, 255, 0),
    name="Scroll of Lightning",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

bomba = Item(
    char="◉",
    color=(255, 255, 0),
    name="Tsar Bomba",
    consumable=consumable.FireballDamageConsumable(damage=999999, radius=30),
)

dagger = Item(
    char="/", color=(209, 209, 209), name="Dagger", equippable=equippable.Dagger()
)

sword = Item(char="/", color=(0, 191, 255), name="Sword", equippable=equippable.Sword())



mithril_sword = Item(char="/", color=(131, 247, 236), name="Mithril Sword", equippable=equippable.MithrilSword())

leather_armor = Item(
    char="▒",
    color=(110, 59, 37),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
)

chain_mail = Item(
    char="░", color=(139, 69, 19), name="Chain Mail", equippable=equippable.ChainMail()
)

mithril_armor = Item(
    char="▒", color=(131, 247, 236), name="Mithril Armor", equippable=equippable.MithrilArmor()
)

murasama = Item(
    char="▒", color=(131, 247, 236), name="Murasama", equippable=equippable.Murasama()
)