import os, random

load_list = [0]
run = True
menu = True
play = False
rules = False
key = False
fight = False
spawn_protection = True

HP = 10
MAXHP = 10
ATK = 3
bandages = 1
potions = 0
gold = 0
x = 0
y = 0

map =[
["plains", "plains", "plains", "plains", "forest", "mountain",     "cave"],
["forest", "forest", "forest", "forest", "forest",    "hills", "mountain"],
["forest", "fields", "bridge", "plains",  "hills",   "forest",    "hills"],
["plains",   "shop",   "town",  "major", "plains",    "hills", "mountain"],
["plains", "fields", "fields", "plains",  "hills", "mountain", "mountain"]
]

x_len = len(map)-1
y_len = len(map[0])-1

biome = {
    "plains": {
        "t": "PLAINS",
        "e": True},
    "forest": {
        "t": "FOREST",
        "e": True},
    "fields": {
        "t": "FIELDS",
        "e": False},
    "bridge": {
        "t": "BRIDGE",
        "e": True},
    "town": {
        "t": "TOWN CENTRE",
        "e": False},
    "shop": {
        "t": "SHOP",
        "e": False},
    "major": {
        "t": "MAJOR",
        "e": False},
    "cave": {
        "t": "CAVE",
        "e": False},
    "mountain": {
        "t": "MOUNTAIN",
        "e": True},
    "hills": {
        "t": "HILLS",
        "e": True,}
        }

enemy_list = ["Goblin", "Orc", "Slime"]

enemy_stats = {
    "Goblin": {
        "hp": 15,
        "atk": 2,
        "gold": 10
    },
    "Orc": {
        "hp": 25,
        "atk": 3,
        "gold": 30
    },
    "Slime": {
        "hp": 10,
        "atk": 2,
        "gold": 5
    },
    "Dragon": {
        "hp": 100,
        "atk": 8,
        "gold": 1000,

    }
}

#current_tile = map[x][y]
#print(current_tile)
#tile_name = biome[current_tile]["t"]
#print(tile_name)
#tile_enemy = biome[current_tile]["e"]
#print(tile_enemy)


def clear():
    os.system("cls")

def draw_line():
    print("------------------------")

def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(bandages),
        str(potions),
        str(gold),
        str(x),
        str(y),
        str(key),
        str(MAXHP)

    ]

    f = open("load.txt", "w")

    for item in list:
        f.write(item + "\n")
    f.close()

def battle():
    global fight, play, run, HP, potions, bandages, gold


    enemy = random.choice[enemy_list]
    enemy_hp = enemy_stats[enemy]["hp"]
    enemy_max_hp = enemy_hp
    enemy_atk = enemy_stats[enemy]["atk"]
    enemy_gold = enemy_stats[enemy]["gold"]


while run:
    while menu:
        clear()

        if rules:
            draw_line()
            print("1. go crazy (a)\n2. go stupid (aa)\n3. go absolutelly mental\n4. have fun")
            draw_line()
            print("\n\npress anything to continue")
            rules = False
            choice = ""
            input("> ")
            clear()

        else:
            draw_line()
            print("1. NEW GAME")
            print("2. LOAD GAME")
            print("3. RULES")
            print("4. QUIT GAME")
            draw_line()
            print("")
            choice = input("# ")
            clear()
        
        if choice == "1":
            print("What is your name, hero?")
            name = input("> ")
            clear()

            play = True
            menu = False

        elif choice == "2":
            try:
                if len(load_list) == 9:
                    f = open("load.txt", "r")
                    load_list = f.readlines()
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    bandages = int(load_list[3][:-1])
                    potions = int(load_list[4][:-1])
                    gold = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    MAXHP = int(load_list[9][:-1])
                    print("Welcome back, " + name)
                    input(">")
                    clear()
                else:
                    print("unsupported save file :(")

                play = True
                menu = False
            except OSError:
                print("no loadable save file!")
                input("> ")
                clear()

        elif choice == "3":
            rules = True

        elif choice == "4":
            quit()

    while play:

        if biome[map[x][y]]["e"]:
            if random.randint(0,100) <= 30:
                pass


        clear()
        draw_line()
        print("LOCATION: ", biome[map[x][y]]["t"])
        draw_line()

        print("CHARACTER: ", name)
        print("HP: " + str(HP) + " / " + str(MAXHP))
        print("DAMAGE: " + str(ATK))
        print("DANDAGES: " + str(bandages))
        print("POTIONS: "+ str(potions))
        print("GOLD: " + str(gold))
        print("COORDINATES: " + str(x) + " , " + str(y))
        
        
        draw_line()
        print("OPTIONS:")
        print("")
        print("0. SAVE AND QUIT")

        if y > 0:
            print("1. GO NORTH")
        if x < x_len:
            print("2. GO EAST")
        if y < y_len:
            print("3. GO SOUTH")
        if x > 0:
            print("4. GO WEST")

        draw_line()
        dest = input("# ")

        if dest == "0":
            play = False
            menu = True
            save()
        elif dest == "1":
            if y > 0:
                y -= 1
                spawn_protection = False
        elif dest == "2":
            if x < x_len:
                x += 1
                spawn_protection = False
        elif dest == "3":
            if y < y_len:
                y += 1
                spawn_protection = False
        elif dest == "4":
            if x > 0:
                x -= 1
                spawn_protection = False
