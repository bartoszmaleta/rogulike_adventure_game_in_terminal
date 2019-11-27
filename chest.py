x = ['gold coin', 'dagger', 'torch', 'arrow', 'bow', 'ruby']
ksa = [1,2,3,4,5]
pos = 2
import random
z = random.choice(ksa)
chest_inventory = random.choices(x, k=z)
for i in range(len(chest_inventory)):
   x.insert(i + pos, chest_inventory[i])
