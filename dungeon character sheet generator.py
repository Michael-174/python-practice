def dungeon(name, weapon = "Rusty sword", armor = "Leather Armor", *item, level = 1, hp = 100, mana = 50, **status):
    print("name:", name,
          "\nweapon:", weapon,
          "\narmor:", armor)
    if item == ():
        print("no item")
        print("You venture empty-handed… brave or foolish?")
    else:
        print("item:", item)
    print("level:", level,
          "\nhp:", hp)
    if hp <= 50:
        print('Warning: fragile soul!')
    print("mana:", mana)
    if status != {}:
        print("status:", status)
    for i in status:
        if status[i] == True:
            print("dangerous effect:", i)

dungeon("Michael", "sacred dick", "light armor", level = 10, hp = 1, monster_girl_lover = True, harem_owner = True)