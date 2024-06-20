import random
import time
import sys

#---------------- iterators (for/while 'simulation in cycle')
i = 0;

#---------------- Game Variables
Move_Roll = random.random();

#---------------- Resources Variables
res=[];
lock_rsc = True;

#---------------- Player Related
player_hitpoints = 10;
player_bag = [];
player_gear = [];
player_coordinates = [2,1];
player_skills = [];

# --------------- Monster Related
monster_hitpoints = 20;
#attack = random.randint(-50, 0);

# -------- Drop Variables
kill = [];
ResList = [];
SuperRareDropTable = ["whip", "wand", "pet"];
SRDOdds = 0.05;
RareDropTable = ["rune chain", "dragonstone", "rune med"];
RDOdds = 0.45;
CommonDropTable = ["air runes", "rune arrow", "cosmic rune"];
CDOdds = 0.75;
AlwaysDropTable = ["demon ashes"];

# -------- Resource Variables
ResFound = [];
remaining = 100;
SuperRareDropTableWood = ["Magic Tree", "Redwood Tree"];
RareDropTableWood = ["Yew Tree", "Maple Tree"];
CommonDropTableWood = ["Willow Tree", "Oak Tree"];
AlwaysDropTableWood = ["Tree"];
#----
SuperRareDropTableOre = ["Runite Ore"];
RareDropTableOre = ["Adamantite Ore", "Mithril Ore", "Gold Ore"];
CommonDropTableOre = ["Silver Ore", "Coal Ore", "Iron Ore"];
AlwaysDropTableOre = ["Tin Ore", "Copper Ore"];
#----
SuperRareDropTableFish = ["Manta Ray","Anglerfish"];
RareDropTableFish = ["Shark", "Monkfish", "Swordfish"];
CommonDropTableFish = ["Lobster", "Tuna", "Bass"];
AlwaysDropTableFish = ["Salmon", "Trout"];

#------------------ Roll Loot Table Definitions
def roll_me():
    roll = random.random();
    return roll

def roll_me_bool():
    roll_bool = random.randint(0, 1);
    if(roll_bool == 1):
        return True
    else:
        return False
def roll_common(r,k,o,dt):
    if(r <= o):
        k += random.sample(dt, k=1);
        return k

def roll_rare(r,k,o,dt):
    if(r <= o):
        k += random.sample(dt, k=1);
        return k

def roll_superrare(r,k,o,dt):
    if(r <= o):
        k += random.sample(dt, k=1);
        return k

def roll_always(k,dt):
    k += random.sample(dt, k=1);
    return k

def kill_loot(r,k):
    roll_superrare(r,k,SRDOdds,SuperRareDropTable);
    roll_rare(r,k,RDOdds,RareDropTable);
    roll_common(r,k,CDOdds,CommonDropTable);
    roll_always(k,AlwaysDropTable);
    return k
def resource_loot(r,l,t):
    if(t == "Wood"):
        roll_superrare(r,l,SRDOdds,SuperRareDropTableWood);
        roll_rare(r,l,RDOdds,RareDropTableWood);
        roll_common(r,l,CDOdds,CommonDropTableWood);
        roll_always(l,AlwaysDropTableWood);
    elif(t == "Ore"):
        roll_superrare(r,l,SRDOdds,SuperRareDropTableOre);
        roll_rare(r,l,RDOdds,RareDropTableOre);
        roll_common(r,l,CDOdds,CommonDropTableOre);
        roll_always(l,AlwaysDropTableOre);
    else:
        roll_superrare(r,l,SRDOdds,SuperRareDropTableFish);
        roll_rare(r,l,RDOdds,RareDropTableFish);
        roll_common(r,l,CDOdds,CommonDropTableFish);
        roll_always(l,AlwaysDropTableFish);        
    return l

#---------------- Menu Options
MainMenu = {
    "1" : "Start",
    "2" : "Reset",
    "3" : "Exit"
}
#---------------- InGame Options
InGame = {
    "1" : "Walk",
    "2" : "Bag",
    "3" : "Gear",
    "4" : "Skills",
    "5" : "Exit",
    "6" : "Zone Menu"
}

Directions = {
    "N" : "North",
    "S" : "South",
    "W" : "West",
    "E" : "East"
}

City_Places = {
    "S" : "Stores",
    "P" : "Processing",
    "B" : "Bank",
    "Q" : "Quests",
    "W" : "Walk",
    "O" : "Options"
}

Trees = {
"1" : "Tree",
"2" : "Oak Tree",
"3" : "Willow Tree",
"4" : "Maple Tree",
"5" : "Yew Tree",
"6" : "Magic Tree",
"7" : "Redwood Tree"
}

SuperRareDropTableWood = ["Magic Tree", "Redwood Tree"];
RareDropTableWood = ["Yew Tree", "Maple Tree"];
CommonDropTableWood = ["Willow Tree", "Oak Tree"];
AlwaysDropTableWood = ["Tree"];

Map_Coordinates = [("C","C","W","W","R","R"),
                   ("C","C","W","W","W","R"),
                   ("W","W","R","R","W","W"),
                   ("W","W","R","R","W","W"),
                   ("W","W","W","W","C","C"),
                   ("D","W","W","W","C","C")];

Region_Mapper = {
    "C" : "City",
    "W" : "Wild",
    "R" : "Resources",
    "D" : "Dungeon"
}

Resource_Available = {
    "1" : "Wood",
    "2" : "Ore",
    "3" : "Fish",
    "O" : "Options"
}
#------------------ Map_Regions

def Map_Region(h,v):
    try:
        if (Region_Mapper[Map_Coordinates[h][v]] == "City"):
            City_Tasks();
        elif (Region_Mapper[Map_Coordinates[h][v]] == "Wild"):
            Wild_Tasks();     
        elif (Region_Mapper[Map_Coordinates[h][v]] == "Resources"):
            Resources_Tasks();
        elif (Region_Mapper[Map_Coordinates[h][v]] == "Dungeon"):
            Dungeon_Tasks();
        else:
            print("We found a Map_Region Error");
    except:
        print("We found a Map_Region Invalid Input");
#------------------ Wild Encounter Mechanics

def encounter_wild():
    encounter_odds = random.random();
    if (encounter_odds >= 0.2):
        print(encounter_odds);
        combat_system(player_hitpoints,20,roll_me(),kill);
    else:
        print(encounter_odds);
        print("Nothing was found");
        In_Game();
#------------------ Resource Type Generator



#------------------ Loot To Bag
def loot(kill,pb):
    try:
        pickup = input('Pick up Loot: Yes (Y) | No (N) \n Player >>> '); 
        if (pickup == 'Y'):
            pb += kill;
        elif (pickup == 'N'):
            print('You left the loot on the floor');
        else:
            print("Invalid input, try again. *loot(else)*");
            loot(kill,pb);
    except:
        print("Invalid input, try again. *loot(except)*");
        loot(kill,pb);
        

#------------------ City Encounter Mechanics

def city_encounter():
    Select = input("City: Stores (S) | Processing (P) | Bank (B) | Quests (Q) | Walk (W) | (Player)Options (O) \n Player >>> ");
    try:
        if (City_Places[Select] == "Stores"):
            print("Stores");
        elif (City_Places[Select] == "Processing"):
            print("Processing");
        elif (City_Places[Select] == "Bank"):
            print("Bank");
        elif (City_Places[Select] == "Quests"):
            print("Quest");
        elif (City_Places[Select] == "Walk"):
            print("Walk");
            walk_to();
        elif (City_Places[Select] == "Options"):
            print("Player Options");
            In_Game();
        else:
            print("That option is not available. *city_encounter(else)*");
            city_encounter();
    except:
        print("That option is not available. *city_encounter(except)*"); 
        city_encounter();

#------------------ Resource Encounter Mechanics

def resource_encounter_p1():
    resource_odds = random.randint(0,1);
    i = 0;
    wood = False; ore = False; fish = False;
    resource_list=[];
    for i in range(3):
        if(i == 0):
            if(roll_me_bool()):
                wood = True;
                resource_list.append("Wood");
        if(i == 1):
            if(roll_me_bool()):
                ore = True;
                resource_list.append("Ore");
        if(i == 2):
            if(roll_me_bool()):
                fish = True;
                resource_list.append("Fish");
    print(resource_list);
    return resource_list

def resource_encounter_p2(rsl):
    global ResList;
    global ResFound;
    global lock_rsc;
    phrase = "";
    print(len(rsl));
    if (len(rsl) == 0):
        phrase = "This Region is dry | ";
    else:  
        for rs in rsl:
            if (rs == "Wood"):
                phrase +=  "1."+ rs + " | ";
            elif (rs == "Ore"):
                phrase +=  "2."+ rs + " | ";
            else:
                phrase +=  "3."+ rs + " | ";              
    Select = input("Resources: " + phrase + "(Player) Options (O) \n Player >>> ");
    try:
        if (Resource_Available[Select] == "Options"):
            ResList = rsl;
            In_Game();     
        elif (Resource_Available[Select] in rsl):
            print("Collecting: " + Resource_Available[Select]);
            rsl = [Resource_Available[Select]];
            if (lock_rsc):
                ResFound = resource_loot(roll_me(),ResList,Resource_Available[Select]);
                lock_rsc = False;
            phrase_restype = "";
            for restype in ResFound:
                if (restype == "Tree"):
                    phrase_restype += "1." + restype + " | ";
                elif (restype == "Oak Tree"):
                    phrase_restype += "2." + restype + " | ";
                elif (restype == "Willow Tree"):
                    phrase_restype += "3." + restype + " | ";
                elif (restype == "Maple Tree"):
                    phrase_restype += "4." + restype + " | ";
                elif (restype == "Yew Tree"):
                    phrase_restype += "5." + restype + " | ";
                elif (restype == "Magic Tree"):
                    phrase_restype += "6." + restype + " | ";
                elif (restype == "Redwood Tree"):
                    phrase_restype += "7." + restype + " | ";
            SelectT = input("Choose one to Collect " + phrase_restype + "(all others will be discarded) | (Player) Options (O) \n Player >>> ");
            try:
                if (Resource_Available[SelectT] == "Options"):
                    In_Game();
                elif(Trees[SelectT] == "Tree"):
                    ResFound = ["Tree"];
                    collect_deplete();
                elif(Trees[SelectT] == "Oak Tree"):
                    ResFound = ["Oak Tree"];          
                elif(Trees[SelectT] == "Willow Tree"):
                    ResFound = ["Willow Tree"];  
                elif(Trees[SelectT] == "Maple Tree"):
                    ResFound = ["Maple Tree"];
                elif(Trees[SelectT] == "Yew Tree"):
                    ResFound = ["Yew Tree"];  
                elif(Trees[SelectT] == "Magic Tree"):
                    ResFound = ["Magic Tree"];  
                elif(Trees[SelectT] == "Redwood Tree"):
                    ResFound = ["Redwood Tree"];
                else:
                    print("That option is not available. *SelectT(else)*");
                    resource_encounter_p2(rsl);
            except:
                print("That option is not available. *SelectT(except)*");
                resource_encounter_p2(rsl);
                print(SelectT);
        else:
            print("That option is not available. *resource_encounter_p2(else)*");
            print(ResFound);
            resource_encounter_p2(rsl);
    except:
        print("That option is not available. *resource_encounter_p2(except)*");
        print(rsl);
        resource_encounter_p2(rsl);
        
def collect_deplete():
    global remaining;
    print(remaining);
    print("\r[===== 0% =====]",end= "");
    time.sleep(1);
    print("\r[|||== 30% =====]",end= "");
    time.sleep(1);
    print("\r[||||| 50% =====]",end= "");
    time.sleep(1);
    print("\r[||||| 70% ||===]",end= "");
    time.sleep(1);
    print("\r[||||| 100% |||||]\n",end= "");
    time.sleep(1);
    if(remaining <= 0):
        ResFound = [];
        ResList = [];
    remaining += -100;
    print(resList);
    print(resFound);    
    resource_encounter_p2(resList);
    
    
    
    
def refresh_zone_variables():
    global res;
    global ResList;
    global ResFound;
    global remaining;
    global lock_rsc;
    
    res = [];
    RestList = [];
    ResFound = [];
    remaining = 100;
    lock_rsc = True;
    
#------------------ Walk Mechanics

def walk_to():
    global player_coordinates;
    Select = input("Walk: North (N) | South (S) | West (W) | East (E) \n Player >>> ");
    try:
        if (Directions[Select] == "North"):
            if (player_coordinates[1] >= 0 and player_coordinates[1] < 5):
                player_coordinates[1] += 1;
                refresh_zone_variables();
                print(player_coordinates);
                print(Map_Coordinates[player_coordinates[0]][player_coordinates[1]]);
                Map_Region(player_coordinates[0],player_coordinates[1]);
            else:
                print("You have reached the limit of that direction.");
                print(player_coordinates);
                walk_to();
        elif (Directions[Select] == "South"):
            if (player_coordinates[1] > 0 and player_coordinates[1] <= 5):
                player_coordinates[1] += -1;
                refresh_zone_variables();
                print(player_coordinates);
                print(Map_Coordinates[player_coordinates[0]][player_coordinates[1]]);
                Map_Region(player_coordinates[0],player_coordinates[1]);
            else:
                print("You have reached the limit of that direction.");
                print(player_coordinates);
                walk_to();            
        elif (Directions[Select] == "West"):
            if (player_coordinates[0] > 0 and player_coordinates[0] <=5):
                player_coordinates[0] += -1;
                refresh_zone_variables();
                print(player_coordinates);
                print(Map_Coordinates[player_coordinates[0]][player_coordinates[1]]);
                Map_Region(player_coordinates[0],player_coordinates[1]);
            else:
                print("You have reached the limit of that direction.");
                print(player_coordinates);
                walk_to();            
        elif (Directions[Select] == "East"):
            if (player_coordinates[0] >= 0 and player_coordinates[0] < 5):
                player_coordinates[0] += 1;
                refresh_zone_variables();
                print(player_coordinates);
                print(Map_Coordinates[player_coordinates[0]][player_coordinates[1]]);
                Map_Region(player_coordinates[0],player_coordinates[1]);
            else:
                print("You have reached the limit of that direction.");
                print(player_coordinates);
                walk_to();            
    except:
        print("That option is not available. *walk_to(except)*");   
        walk_to();
#------------------ Full Combat Situation

def combat_system(php,hp,r,k):
    global player_hitpoints;
    global monster_hitpoints;
    global player_bag;
    while (hp > 0):
        k = [];
        next_move = input('Next Move: ');
        if (next_move == 'A'):
            hp += random.randint(-10, 0);
            print('You chose to: ' + next_move);
            if (hp >= 0):
                print('Monster has currently: '+ str(hp) + ' HP');
                if (php > 0):
                    php += random.randint(-1, 0);
                    if (php > 0):
                        print('Player has currently: '+ str(php) + ' HP');
                    else:
                        print('Player has currently: 0 HP');
                if (php <= 0):
                    print ("Game Over");
                    player_hitpoints = 0;
                    monster_hitpoints = hp;
                    break;
            else:
                print('Monster has currently: 0 HP');
        else:
            print('That option is not available *combat_system(else)*');
        if (php > 0 and hp <= 0):
            player_hitpoints = php;
            monster_hitpoints = 0;
            kill_loot(r,k);
            #print(r);
            print(k);
            loot(k,player_bag);
            In_Game();
            
# ---------------- Monster_combat Function Separated           
""" def monster_combat(php,r):
    if (php > 0):
            php += random.randint(-25, 0);
            if (php > 0):
                print('Player has currently: '+ str(php) + ' HP');
            else:
                print('Player has currently: 0 HP'); """
                
# ---------------- In-Game UI   

def In_Game():
    global res;
    global ResFound;
    global ResList;
    Select = input("1.Walk | 2.Bag | 3.Gear | 4.Skills | 5.Exit | 6.Zone Menu \n Player >>> ");
    try:
        if (int(Select) <= 6):
            if (InGame[Select] == "Walk"):
                walk_to();
            elif (InGame[Select] == "Bag"):
                print("Opening your Bag:");
                print(player_bag);
                In_Game();
            elif (InGame[Select] == "Gear"):
                print("Opening your Gear");
            elif (InGame[Select] == "Skills"):
                print("Opening your Skills!")
                Main_Menu();                    
            elif (InGame[Select] == "Exit"):
                print("EXIT TO MAIN MENU!")
                Main_Menu();
            elif (InGame[Select] == "Zone Menu"): #----------------- Return to Zone Menus
                if (Region_Mapper[Map_Coordinates[player_coordinates[0]][player_coordinates[1]]] == "City"):
                    City_Tasks();
                elif (Region_Mapper[Map_Coordinates[player_coordinates[0]][player_coordinates[1]]] == "Resources"):
                    resource_encounter_p2(ResList);
                else:
                    print("Your current Zone has no further Option available");
                    In_Game();   
        else:
            print("That option is not available. *In_Game(else)*");
            In_Game(); 
    except:
        print("That option is not available. *In_Game(except)*");    
        In_Game();

#---------------- Tasks for City Zones
def City_Tasks():
    print("You can do all these tasks in the City Zone");
    city_encounter();
#---------------- Tasks for Wild Zones
def Wild_Tasks():
    encounter_wild();

#---------------- Tasks for Resources Zones
def Resources_Tasks():
    print("You can do all these tasks in the Resources Zone");
    resList = resource_encounter_p1();
    resource_encounter_p2(resList);
    
    
#---------------- Tasks for Dungeon Zones
def Dungeon_Tasks():
    print("You can do all these tasks in the Dungeon Zone");
    In_Game();
# ----------------  Main Menu Interface        
def Main_Menu():
    Select = input("1.Start | 2.Reset | 3.Exit \n Player >>> ");
    try:
        if(int(Select) <= 3):
                if(MainMenu[Select] == "Start"):
                    In_Game();
                elif(MainMenu[Select] == "Reset"):
                    print("Reset Game Data!");
                elif(MainMenu[Select] == "Exit"):
                    print("EXIT GAME!");
        else:
            print("That option is not available. *Main_Menu(else)*");
            Main_Menu();  
    except:
        print("That option is not available. *Main_Menu(except)*");   
        Main_Menu();
        
Main_Menu();
#collect_deplete();