dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}  


def add_to_inventory(inventory, added_items):
    for item in dragon_loot:
        if item in inv:
            inv[item] += 1
        else:
            inv[item] = 1


print(inv)

add_to_inventory(inv, dragon_loot)

print(inv)