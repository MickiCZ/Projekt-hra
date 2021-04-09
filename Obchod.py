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

#Prodej
select_item = int(input ("Co si z toho koupíš? (napiš číslo od 0 do 4) "))
if select_item == 0:
    print(f"Koupil sis {shop_list[select_item][0]} ")
elif select_item == 1:
    print(f"Koupil sis {shop_list[select_item][0]} ")
elif select_item == 2:
    print(f"Koupil sis {shop_list[select_item][0]} ")
elif select_item == 3:
    print(f"Koupil sis {shop_list[select_item][0]} ")
elif select_item == 4:
    print(f"Koupil sis {shop_list[select_item][0]} ")
else:
    print("Zadal jsi špatné číslo, které není v seznamu!")
#while = True:
 #   print("Vešel jsi do obchodu")