import chest as chest

# inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}  


def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1


# print(inv)

# add_to_inventory(inv, chest.chest_inventory)

# print(inv)