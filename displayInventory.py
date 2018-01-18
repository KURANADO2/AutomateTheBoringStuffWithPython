inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
addItems = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayInventory(inventory):
    count = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        count += inventory.get(k, 0)
    print('Total number of items: ' + str(count))
    print()


def addToInventory(inventory, addedItems):
    for item in addItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1

displayInventory(inventory)
addToInventory(inventory, addItems)
displayInventory(inventory)
