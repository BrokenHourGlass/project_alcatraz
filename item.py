class Item:
    def __init__(self, name, price, description, usable=False, distance = None, item_type = None):
        self.name = name
        self.price = price
        self.description = description
        self.usable = usable
        self.distance = distance
        self.item_type = item_type

    # Function used to display every object
    def display(self):
        print(f"Item: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Description: {self.description}")
        print(f"Useable: {self.usable}")
        if self.distance:
            print(f"Distance: {self.distance}ft.")
        print(f"Item Type: {self.item_type}")
        print("---------------------------------------------------")

# Items Lists
sword = Item("Cutlass", 25, "A short, curved sword favored for its versatility in close combat.", item_type = "Weapon")
pistol = Item("Flintlock Pistol", 50, "A single-shot firearm used for personal defense.", item_type = "Weapon")
axe = Item("Boarding_axe", 1, "A short, curved sword favored for its versatility in close combat.", item_type = "Weapon")
shotgun = Item("Blunderbuss", 50, "A primitive shotgun with a wide muzzle, used for short-ranged engagements.", item_type = "Weapon")
dagger = Item("Dagger", 00, "A small, sharp blade used for personal defense and close combat situations", item_type = "Weapon")
rifle = Item("Musket", 00, "A long-barreled firearm used by pirates for long ranged attacks and ship-to-ship combat", item_type = "Weapon")
grenade = Item("Grenade", 00, "Explosive device used for attacking enemy ships or structures.", item_type = "Weapon")
sabre_sword = Item("Sabre", 00, "A single-edged, curved sword often used by naval officers and pirates alike.", item_type = "Weapon")
#dildo = Item("Dragon Dildo", 1000, "Congrats, your a cheating dick, enjoy your free dragon dick, dick.", item_type = "Flesh Scepter")
grappling_hook = Item("Grappling Hook", 00, "Used for boarding enemy ships by attaching to rigging or hulls.", False, distance = 20, item_type = "Object")
compass = Item("Compass", 00, "Used for Navigation.", item_type = "Object")
Spyglass = Item("Spyglass", 00, "A handheld telescope used for spotting ships and land from a distance.", distance = 100, item_type = "Object")
town_map = Item("Map", 00, "Used for navigation and locating burried treasure.", item_type = "Object")
lantern = Item("Lantern", 00, "Used for light at night or in dark places.", distance = 20, item_type = "Object")
sextant = Item("Sextant", 00, "Used for celestial navigation.", item_type = "Object")
pen_paper = Item("Parchment and Quill", 00, "Used for writing and communication", item_type = "Object")


items = [sword, pistol, axe, shotgun, dagger, rifle, grenade, sabre_sword, grappling_hook, compass, Spyglass, town_map, lantern, sextant, pen_paper]

for item in items:
    item.display()