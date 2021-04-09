utok = 0
obrana = 0
penize = 1000

#shop list - 0. name, 1. dmg 2. price
wooden_sword = ["Wooden sword", 5, 100]
rusty_sword = ["Rusty sword", 10, 250]
iron_sword = ["Iron sword", 15, 500]
katana = ["Katana", 20, 1000]
axe = ["Axe", 30, 2000]
shop_list = [wooden_sword, rusty_sword, iron_sword, katana, axe]
print("V našem obchodě máme následující: ")
for i in shop_list:
    print("Zbraň: {} dmg: +{} cena: {}".format(i[0], i[1], i[2]))


#while = True:
 #   print("Vešel jsi do obchodu")