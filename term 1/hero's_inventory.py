# Hero's Inventory
# Demonstrates tuple creation

# create an empty tuple
inventory = ()

# treat the tuple as a condition
if not inventory:
    print("You are empty-handed.")

input("\nPress the enter key to continue.")

# create a tuple with some items
inventory = ("short sword",
             "armor",
             "helm",
             "boots",
             "pants",
             "shield",
             "healing potion",
             "mana potion",
             "dagger",
             "Ashbringer")

# print the tuple
print("\nThe tuple inventory is:")
print(inventory)

# print each element in the tuple
print("\nYour items:")
for item in inventory:
    print(item)

input("\n\nPress the enter key to exit.")
