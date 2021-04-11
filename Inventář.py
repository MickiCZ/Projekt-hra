#item list - 0. name, 1. dmg 2. price 3. equipable 4. type
#wooden_sword = ["Wooden sword", 5, 100, True, "weapon"]
#stick = ["Stick", 0, 0, False, "item"]
#shield = ["Shield", 0, 200, True, "weapon"]
#rock = ["Rock", 0, 0, False, "item"]
#inventory_list = [wooden_sword, stick, shield, rock]
#equiped = []
def inventory(inv, eqp):
    inventory_slot = 0
    item_summarize = ""
    for i in inv:
        if i[3] == True:
            print(i)
            want_equip = input("Chceš si to vybavit? (y/n) ")
            if want_equip == "y":
                eqp.append(i)
                inv.pop(inventory_slot)
                
        inventory_slot += 1
    for i in inv:
        if i[4] == "weapon":
            item_summarize = item_summarize + i[0] + " " + "+" + str(i[1]) +"Dmg, "
        else:
            item_summarize = item_summarize + i[0] + ", "
       
    
    print(f"V inventáří máš: {item_summarize}a equipnuto máš: {eqp}")

#inventory(inventory_list,equiped)




