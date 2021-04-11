#item list - 0. name, 1. dmg 2. price 3. equipable
wooden_sword = ["Wooden sword", 5, 100, True]
stick = ["Stick", 0, 0, False]
shield = ["Shield", 0, 200, True]
rock = ["Rock", 0, 0, False]
inventory_list = [wooden_sword, stick, shield, rock]
equiped = []
def inventory():
    inventory_slot = 0
    for i in inventory_list:
        if i[3] == True:
            print(i)
            want_equip = input("Chceš si to vybavit? (y/n) ")
            if want_equip == "y":
                equiped.append(i)
                inventory_list.pop(inventory_slot)
        inventory_slot += 1

    print(f"V inventáří máš: {inventory_list} a equipnuto máš: {equiped}")




