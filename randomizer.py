import random as r
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QCheckBox, QComboBox, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import pyqtSlot, Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap
#import PyQt5.Qt as Qt
#import PyQt5
import sys
import os

def resource_path(relative_path):
     if hasattr(sys, '_MEIPASS'):
         return os.path.join(sys._MEIPASS, relative_path)
     return os.path.join(os.path.abspath("."), relative_path)

#CHAMPIONS
champions = ["Aya","Fiora","Hart","HyunWoo","Isol","Jackie","Magnus","Nadine","Zahir"]

#WEAPONS
daggerLegendary = ["Fragarach"]
daggerEpic = ["Mount Slicer","Vibroblade","Carnwennan"]
daggerRare = ["Rose Knife"]
dagger = daggerLegendary + daggerEpic + daggerRare

twohandswordLegendary = ["Dainsleif","Laevateinn"]
twohandswordEpic = ["Monohoshizao","Hovud","Arondight","Excalibur"]
twohandswordRare = ["Plasma Sword","Thuan Thien","Jewel Sword","Bastard Sword","Muramasa","Masamune","Katana"]
twohandsword = twohandswordLegendary + twohandswordEpic + twohandswordRare

axeLegendary =[]
axeEpic = ["Harpe","Parashu","Scythe","Santa Muerte","Beam Axe"]
axeRare = ["Gigantic Axe","Reaper's Scythe","Light Hatchet"]
axe = axeLegendary + axeEpic + axeRare

dualswordLegendary = []
dualswordEpic = ["Starsteel Twin Sword"]
dualswordRare = ["Divine Dual Swords"]
dualsword = dualswordLegendary + dualswordEpic + dualswordRare

pistolLegendary = ["Kelte"]
pistolEpic = ["Magnum-Boa","Electron Blaster","Elegance","Devil's Marksman"]
pistolRare = ["Magnum-Anaconda","Double Revolver SP","FN57"]
pistol = pistolLegendary + pistolEpic + pistolRare

assaultrifleLegendary = []
assaultrifleEpic = ["AK-12","Gatling Gun","Machine Gun","XCR"]
assaultrifleRare = ["M16A1","AK-47"]
assaultrifle = assaultrifleLegendary + assaultrifleEpic + assaultrifleRare

sniperrifleLegendary = ["The Deadly Ray"]
sniperrifleEpic = ["Polaris","NTW-20","Intervention","Tac-50"]
sniperrifleRare = ["Railgun","Golden Rifle","Harpoon Gun"]
sniperrifle = sniperrifleLegendary + sniperrifleEpic + sniperrifleRare

rapierLegendary = ["Mistilteinn"]
rapierEpic = ["Joyeuse","Meteor Claymore","Volticletto","Durendal mk2","Sword of Justice"]
rapierRare = ["Apricot Sword"]
rapier = rapierLegendary + rapierEpic + rapierRare

spearLegendary = ["Spear of Longinus","Blazing Lance"]
spearEpic = ["Dragon Guandao","Fangtian Huaji","Cosmic Bident","Eighteen Foot Spear","Gentian Silver Gun","Lance of Poseidon"]
spearRare = ["Sharpened Spear","Halberd Axe","Pike","Bident"]
spear = spearLegendary + spearEpic + spearRare

hammerLegendary = []
hammerEpic = ["Magic Stick","Evening Star","Hammer of Thor","Hammer of Dagda","Fang Mace"]
hammerRare = ["Black Stag Hammer","Morning Star"]
hammer = hammerLegendary + hammerEpic + hammerRare

batLegendary = ["Monkey King Bar"]
batEpic = ["Spy Umbrella","Mallet","Statue of Soteria"]
batRare = ["Torch","Umbrella","Goblin Bat"]
bat = batLegendary + batEpic + batRare

throwLegendary = ["Ruthenium Marble"]
throwEpic = ["High Explosive Grenade","Spiky Bouncy Ball"]
throwRare = ["David's Sling","Smoke Bomb","Grenade of Antioch","Flubber","Ball Lightning","Incendiary Bomb","Flour Bomb"]
throw = throwLegendary + throwEpic + throwRare

shurikenLegendary = ["Sudarsana","Petal Torrent"]
shurikenEpic = ["Death Rune","Wind and Fire Wheels","Flechette","Azure Dagger"]
shurikenRare = ["Frost Venom Dart","Fuhma Shuriken","Mystic Jade Charm","Plumbata","Dharma Chakram","Venom Dart","Cards of Tyranny","Apricot Flower Tag","Chakram"]
shuriken = shurikenLegendary + shurikenEpic + shurikenRare 

bowLegendary = ["Failnaught"]
bowEpic = ["Elemental Bow","Twinbow","Golden-Ratio Bow","Ancient Bolt"]
bowRare = ["Scorchbow","Pellet Bow","Mighty Bow","Stallion Bow","Strong Bow","Composite Bow"]
bow = bowLegendary + bowEpic + bowRare

crossbowLegendary = ["Sharanga"]
crossbowEpic = ["The Golden Ghost","Sniper Crossbow","Ballista","The Legend of the General"]
crossbowRare = ["Steel Bow","Heavy Crossbow","Laser Crossbow","Power Crossbow"]
crossbow = crossbowLegendary + crossbowRare + crossbowEpic

gloveLegendary = []
gloveEpic = ["Imperial Silk Glove","White Claw Punch","Brasil Gauntlet","Frost Petal Hand","Bloodwing Knuckles","Divine Fist","One Inch Punch","Buddha's Palm"]
gloveRare = ["Nirvana Gauntlet","Glass Knuckles","Shatter Shell Gauntlet","Bone Gauntlet","Wing Knuckles","Gauntlet"]
glove = gloveLegendary + gloveEpic + gloveRare

tonfaLegendary =[]
tonfaEpic = ["Mai Sok","Plasma Tonfa","Tactical Tonfa"]
tonfaRare = ["Ryukyu Tonfa","Police Baton"]
tonfa = tonfaLegendary + tonfaEpic + tonfaRare 

guitarLegendary = []
guitarEpic = ["Teen Spirit","The Wall","Wonderful Tonight","Satisfaction","Purple Haze","Stairway to Heaven","Bohemian"] 
guitarRare = ["Wild Horse","Superstrat","Nocaster","King-V","Humbucker Pickup","Ruby Special"]
guitar = guitarLegendary + guitarEpic + guitarRare

#ARMOR
headLegendary = ["Laurel Wreath"]
headEpic = ["Imperial Burgonet","Imperial Crown","Chinese Opera Mask","Helm of Banneret","Tactical OPS Helmet","Mithril Helm","Crystal Tiara"]
headRare = ["Motorcycle Helmet","Close Helm","Crown","Tiara","Fire Helmet","Ballistic Helmet"]

chestLegendary = ["Kabana","Blazing Dress","Queen of Hearts"]
chestEpic = ["EOD Suit","Battle Suit","Chang Pao","Butler's Suit","Commander's Armor","Dragon Dobok","Amazoness Armor","Crusader Armor","Mithril Armor","Rocker's Jacket","Optical Camouflage Suit"]
chestRare = ["Covert Agent Uniform","Sunset Armor","Bulletproof Vest","Hanbok","Sheet Metal Armor","Qipao","Suit","Chain Armor","Rider Jacket"]

armLegendary = ["Bracelet of Skadi","Auto-Arms","Radar"]
armEpic = ["Draupnir","Sword of Shah Jahan","Creed of the Knight","Vital Sign Sensor","Mithril Shield"]
armRare = ["Cube Watch","Sword Stopper","Steel Shield","Crimson Bracelet","Bazuband","Golden Bracelet","Sheath"]

legLegendary = ["Glacial Shoes","Red Shoes","Boots of Hermes"]
legEpic = ["Mithril Boots","Bucephalus","EOD Boots"]
legRare = ["Combat Boots","Killer Heels","StraitJacket Sneakers","Steel Knee Pads","Feather Boots","Maverick Runner","Boots","Repaired Slippers"]

accessoryLegendary = ["Emerald Tablet"]
accessoryEpic = ["True Samadhi Fire","Glacial Ice"]
accessoryRare = ["Veritas Lux Mea","Schrodinger's Box","Moonlight Pendant","Magazine","Uchiwa","Powder of Life"]

locations = ["Alley","Archery Range","Avenue","Beach","Cemetery","Chapel","Dock","Factory","Forest","Hospital","Hotel","Pond","School","Temple","Uptown"]

#BY RARITY
legendaryAll = accessoryLegendary + legLegendary + armLegendary + chestLegendary + headLegendary + guitarLegendary + tonfaLegendary + gloveLegendary + crossbowLegendary + bowLegendary + shurikenLegendary + throwLegendary + batLegendary + hammerLegendary + spearLegendary + rapierLegendary + sniperrifleLegendary + assaultrifleLegendary + pistolLegendary + dualswordLegendary + daggerLegendary + axeLegendary + twohandswordLegendary
epicAll = accessoryEpic + legEpic + armEpic + chestEpic + headEpic + guitarEpic + tonfaEpic + gloveEpic + crossbowEpic + bowEpic + shurikenEpic + throwEpic + batEpic + hammerEpic + spearEpic + rapierEpic + sniperrifleEpic + assaultrifleEpic + pistolEpic + dualswordEpic + daggerEpic + axeEpic + twohandswordEpic
rareAll = accessoryRare + legRare + armRare + chestRare + headRare + guitarRare + tonfaRare + gloveRare + crossbowRare + bowRare + shurikenRare + throwRare + batRare + hammerRare + spearRare + rapierRare + sniperrifleRare + assaultrifleRare + pistolRare + dualswordRare + daggerRare + axeRare + twohandswordRare


#INPUT
#champion = int(input("Select champion: (0 = all, 1 = Aya, 2 = Fiora, 3 = Hart, 4 = HyunWood, 5 = Isol, 6 = Jackie, 7 = Magnus, 8 = Nadine, 9 = Zahir) "))
#legendary = int(input("Include legendary items? (1 for yes, 0 for no) "))
#epic = int(input("Include epic items? (1 for yes, 0 for no) "))
#rare = int(input("Include rare items? (1 for yes, 0 for no) "))

#if (champion == 0):
#    champion = r.randint(1,9)

def Randomize(champion,legendary,epic,rare,location):
    champion = champion
    if (champion == 0):
        champion = r.randint(1,9)
    
    #EMPTY
    weapon = []
    head = []
    chest = []
    arm = []
    leg = []
    accessory = []
    print("")
    text = ("")
    
    #AYA
    if (champion == 1):
        print("Champion: Aya")
        text = text + "Champion: Aya" + "\n"
        if (legendary == 1):
            weapon = weapon + pistolLegendary + assaultrifleLegendary + sniperrifleLegendary
        if (epic == 1):
            weapon = weapon + pistolEpic + assaultrifleEpic + sniperrifleEpic
        if (rare == 1):
            weapon = weapon + pistolRare + assaultrifleRare + sniperrifleRare
    
    #FIORA
    if (champion == 2):
        print("Champion: Fiora")
        text = text + "Champion: Fiora" + "\n"
        if (legendary == 1):
            weapon = weapon + twohandswordLegendary + rapierLegendary + spearLegendary
        if (epic == 1):
            weapon = weapon + twohandswordEpic + rapierEpic + spearEpic
        if (rare == 1):
            weapon = weapon + twohandswordRare + rapierRare + spearRare  
    
    #HART
    if (champion == 3):
        print("Champion: Hart")
        text = text + "Champion: Hart" + "\n"
        if (legendary == 1):
            weapon = weapon + guitarLegendary
        if (epic == 1):
            weapon = weapon + guitarEpic
        if (rare == 1):
            weapon = weapon + guitarRare
    
    #HYUNWOO
    if (champion == 4):
        print("Champion: HyunWoo")
        text = text + "Champion: HyunWoo" + "\n"
        if (legendary == 1):
            weapon = weapon + gloveLegendary + tonfaLegendary
        if (epic == 1):
            weapon = weapon + gloveEpic + tonfaEpic
        if (rare == 1):
            weapon = weapon + gloveRare + tonfaRare      
    
    #ISOL
    if (champion == 5):
        print("Champion: Isol")
        text = text + "Champion: Isol" + "\n"
        if (legendary == 1):
            weapon = weapon + assaultrifleLegendary
        if (epic == 1):
            weapon = weapon + assaultrifleEpic
        if (rare == 1):
            weapon = weapon + assaultrifleRare
    
    #JACKIE
    if (champion == 6):
        print("Champion: Jackie")
        text = text + "Champion: Jackie" + "\n"
        if (legendary == 1):
            weapon = weapon + daggerLegendary + twohandswordLegendary + axeLegendary + dualswordLegendary
        if (epic == 1):
            weapon = weapon + daggerEpic + twohandswordEpic + axeEpic + dualswordEpic
        if (rare == 1):
            weapon = weapon + daggerRare + twohandswordRare + axeRare + dualswordRare
    
    #MAGNUS
    if (champion == 7):
        print("Champion: Magnus")
        text = text + "Champion: Magnus" + "\n"
        if (legendary == 1):
            weapon = weapon + batLegendary + hammerLegendary
        if (epic == 1):
            weapon = weapon + batEpic + hammerEpic
        if (rare == 1):
            weapon = weapon + batRare + hammerRare
    
    #NADINE
    if (champion == 8):
        print("Champion: Nadine")
        text = text + "Champion: Nadine" + "\n"
        if (legendary == 1):
            weapon = weapon + bowLegendary + crossbowLegendary
        if (epic == 1):
            weapon = weapon + bowEpic + crossbowEpic
        if (rare == 1):
            weapon = weapon + bowRare + crossbowRare
    
    #Zahir
    if (champion == 9):
        print("Champion: Zahir")
        text = text + "Champion: Zahir" + "\n"
        if (legendary == 1):
            weapon = weapon + throwLegendary + shurikenLegendary
        if (epic == 1):
            weapon = weapon + throwEpic + shurikenEpic
        if (rare == 1):
            weapon = weapon + throwRare + shurikenRare
    
    #FILL LISTS
    if (legendary == 1):
        head = head + headLegendary
        chest = chest + chestLegendary
        arm = arm + armLegendary
        leg = leg + legLegendary
        accessory = accessory + accessoryLegendary
        
    if (epic == 1):
        head = head + headEpic
        chest = chest + chestEpic
        arm = arm + armEpic
        leg = leg + legEpic
        accessory = accessory + accessoryEpic
    
    if (rare == 1):
        head = head + headRare
        chest = chest + chestRare
        arm = arm + armRare
        leg = leg + legRare
        accessory = accessory + accessoryRare
    
    #RANDOM NUMBERS
    weaponN = r.randint(0,len(weapon)-1)
    headN = r.randint(0,len(head)-1)
    chestN = r.randint(0,len(chest)-1)
    armN = r.randint(0,len(arm)-1)
    legN = r.randint(0,len(leg)-1)
    accessoryN = r.randint(0,len(accessory)-1)
    locationN = r.randint(0,len(locations)-1)
        
    
    #GENERATE WEAPON
    weaponR = weapon[weaponN]
    if (weaponR in dagger):
        if (weaponR in daggerLegendary):
            print("Weapon: "+weaponR+" (Dagger, Legendary)")
            text = text + "Weapon: "+weaponR+" (Dagger, Legendary)" + "\n"
        if (weaponR in daggerEpic):
            print("Weapon: "+weaponR+" (Dagger, Epic)")
            text = text + "Weapon: "+weaponR+" (Dagger, Epic)" + "\n"
        if (weaponR in daggerRare):
            print("Weapon: "+weaponR+" (Dagger, Rare)")
            text = text + "Weapon: "+weaponR+" (Dagger, Rare)" + "\n"
    if (weaponR in twohandsword):
        if (weaponR in twohandswordLegendary):
            print("Weapon: "+weaponR+" (Two-Handed Sword, Legendary)")
            text = text + "Weapon: "+weaponR+" (Two-Handed Sword, Legendary)" + "\n"
        if (weaponR in twohandswordEpic):
            print("Weapon: "+weaponR+" (Two-Handed Sword, Epic)")
            text = text + "Weapon: "+weaponR+" (Two-Handed Sword, Epic)" + "\n"
        if (weaponR in twohandswordRare):
            print("Weapon: "+weaponR+" (Two-Handed Sword, Rare)")
            text = text + "Weapon: "+weaponR+" (Two-Handed Sword, Rare)" + "\n"
    if (weaponR in axe):
        if (weaponR in axeLegendary):
            print("Weapon: "+weaponR+" (Axe, Legendary)")
            text = text + "Weapon: "+weaponR+" (Axe, Legendary)" + "\n"
        if (weaponR in axeEpic):
            print("Weapon: "+weaponR+" (Axe, Epic)")
            text = text + "Weapon: "+weaponR+" (Axe, Epic)" + "\n"
        if (weaponR in axeRare):
            print("Weapon: "+weaponR+" (Axe, Rare)")
            text = text + "Weapon: "+weaponR+" (Axe, Rare)" + "\n"
    if (weaponR in dualsword):
        if (weaponR in dualswordLegendary):
            print("Weapon: "+weaponR+" (Dual Sword, Legendary)")
            text = text + "Weapon: "+weaponR+" (Dual Sword, Legendary)" + "\n"
        if (weaponR in dualswordEpic):
            print("Weapon: "+weaponR+" (Dual Sword, Epic)")
            text = text + "Weapon: "+weaponR+" (Dual Sword, Epic)" + "\n"
        if (weaponR in dualswordRare):
            print("Weapon: "+weaponR+" (Dual Sword, Rare)")
            text = text + "Weapon: "+weaponR+" (Dual Sword, Rare)" + "\n"
    if (weaponR in pistol):
        if (weaponR in pistolLegendary):
            print("Weapon: "+weaponR+" (Pistol, Legendary)")
            text = text + "Weapon: "+weaponR+" (Pistol, Legendary)" + "\n"
        if (weaponR in pistolEpic):
            print("Weapon: "+weaponR+" (Pistol, Epic)")
            text = text + "Weapon: "+weaponR+" (Pistol, Epic)" + "\n"
        if (weaponR in pistolRare):
            print("Weapon: "+weaponR+" (Pistol, Rare)")
            text = text + "Weapon: "+weaponR+" (Pistol, Rare)" + "\n"
    if (weaponR in assaultrifle):
        if (weaponR in assaultrifleLegendary):
            print("Weapon: "+weaponR+" (Assault Rifle, Legendary)")
            text = text + "Weapon: "+weaponR+" (Assault Rifle, Legendary)" + "\n"
        if (weaponR in assaultrifleEpic):
            print("Weapon: "+weaponR+" (Assault Rifle, Epic)")
            text = text + "Weapon: "+weaponR+" (Assault Rifle, Epic)" + "\n"
        if (weaponR in assaultrifleRare):
            print("Weapon: "+weaponR+" (Assault Rifle, Rare)")
            text = text + "Weapon: "+weaponR+" (Assault Rifle, Rare)" + "\n"
    if (weaponR in sniperrifle):
        if (weaponR in sniperrifleLegendary):
            print("Weapon: "+weaponR+" (Sniper Rifle, Legendary)")
            text = text + "Weapon: "+weaponR+" (Sniper Rifle, Legendary)" + "\n"
        if (weaponR in sniperrifleEpic):
            print("Weapon: "+weaponR+" (Sniper Rifle, Epic)")
            text = text + "Weapon: "+weaponR+" (Sniper Rifle, Epic)" + "\n"
        if (weaponR in sniperrifleRare):
            print("Weapon: "+weaponR+" (Sniper Rifle, Rare)")
            text = text + "Weapon: "+weaponR+" (Sniper Rifle, Rare)" + "\n"
    if (weaponR in rapier):
        if (weaponR in rapierLegendary):
            print("Weapon: "+weaponR+" (Rapier, Legendary)")
            text = text + "Weapon: "+weaponR+" (Rapier, Legendary)" + "\n"
        if (weaponR in rapierEpic):
            print("Weapon: "+weaponR+" (Rapier, Epic)")
            text = text + "Weapon: "+weaponR+" (Rapier, Epic)" + "\n"
        if (weaponR in rapierRare):
            print("Weapon: "+weaponR+" (Rapier, Rare)")
            text = text + "Weapon: "+weaponR+" (Rapier, Rare)" + "\n"
    if (weaponR in spear):
        if (weaponR in spearLegendary):
            print("Weapon: "+weaponR+" (Spear, Legendary)")
            text = text + "Weapon: "+weaponR+" (Spear, Legendary)" + "\n"
        if (weaponR in spearEpic):
            print("Weapon: "+weaponR+" (Spear, Epic)")
            text = text + "Weapon: "+weaponR+" (Spear, Epic)" + "\n"
        if (weaponR in spearRare):
            print("Weapon: "+weaponR+" (Spear, Rare)")  
            text = text + "Weapon: "+weaponR+" (Spear, Rare)" + "\n"
    if (weaponR in hammer):
        if (weaponR in hammerLegendary):
            print("Weapon: "+weaponR+" (Hammer, Legendary)")
            text = text + "Weapon: "+weaponR+" (Hammer, Legendary)" + "\n"
        if (weaponR in hammerEpic):
            print("Weapon: "+weaponR+" (Hammer, Epic)")
            text = text + "Weapon: "+weaponR+" (Hammer, Epic)" + "\n"
        if (weaponR in hammerRare):
            print("Weapon: "+weaponR+" (Hammer, Rare)")  
            text = text + "Weapon: "+weaponR+" (Hammer, Rare)" + "\n"
    if (weaponR in bat):
        if (weaponR in batLegendary):
            print("Weapon: "+weaponR+" (Bat, Legendary)")
            text = text + "Weapon: "+weaponR+" (Bat, Legendary)" + "\n"
        if (weaponR in batEpic):
            print("Weapon: "+weaponR+" (Bat, Epic)")
            text = text + "Weapon: "+weaponR+" (Bat, Epic)" + "\n"
        if (weaponR in batRare):
            print("Weapon: "+weaponR+" (Bat, Rare)") 
            text = text + "Weapon: "+weaponR+" (Bat, Rare)" + "\n"
    if (weaponR in throw):
        if (weaponR in throwLegendary):
            print("Weapon: "+weaponR+" (Throw, Legendary)")
            text = text + "Weapon: "+weaponR+" (Throw, Legendary)" + "\n"
        if (weaponR in throwEpic):
            print("Weapon: "+weaponR+" (Throw, Epic)")
            text = text + "Weapon: "+weaponR+" (Throw, Epic)" + "\n"
        if (weaponR in throwRare):
            print("Weapon: "+weaponR+" (Throw, Rare)")       
            text = text + "Weapon: "+weaponR+" (Throw, Rare)" + "\n"
    if (weaponR in shuriken):
        if (weaponR in shurikenLegendary):
            print("Weapon: "+weaponR+" (Shuriken, Legendary)")
            text = text + "Weapon: "+weaponR+" (Shuriken, Legendary)" + "\n"
        if (weaponR in shurikenEpic):
            print("Weapon: "+weaponR+" (Shuriken, Epic)")
            text = text + "Weapon: "+weaponR+" (Shuriken, Epic)" + "\n"
        if (weaponR in shurikenRare):
            print("Weapon: "+weaponR+" (Shuriken, Rare)")         
            text = text + "Weapon: "+weaponR+" (Shuriken, Rare)" + "\n"
    if (weaponR in bow):
        if (weaponR in bowLegendary):
            print("Weapon: "+weaponR+" (Bow, Legendary)")
            text = text + "Weapon: "+weaponR+" (Bow, Legendary)" + "\n"
        if (weaponR in bowEpic):
            print("Weapon: "+weaponR+" (Bow, Epic)")
            text = text + "Weapon: "+weaponR+" (Bow, Epic)" + "\n"
        if (weaponR in bowRare):
            print("Weapon: "+weaponR+" (Bow, Rare)")         
            text = text + "Weapon: "+weaponR+" (Bow, Rare)" + "\n"
    if (weaponR in crossbow):
        if (weaponR in crossbowLegendary):
            print("Weapon: "+weaponR+" (Crossbow, Legendary)")
            text = text + "Weapon: "+weaponR+" (Crossbow, Legendary)" + "\n"
        if (weaponR in crossbowEpic):
            print("Weapon: "+weaponR+" (Crossbow, Epic)")
            text = text + "Weapon: "+weaponR+" (Crossbow, Epic)" + "\n"
        if (weaponR in crossbowRare):
            print("Weapon: "+weaponR+" (Crossbow, Rare)")    
            text = text + "Weapon: "+weaponR+" (Crossbow, Rare)" + "\n"
    if (weaponR in glove):
        if (weaponR in gloveLegendary):
            print("Weapon: "+weaponR+" (Glove, Legendary)")
            text = text + "Weapon: "+weaponR+" (Glove, Legendary)" + "\n"
        if (weaponR in gloveEpic):
            print("Weapon: "+weaponR+" (Glove, Epic)")
            text = text + "Weapon: "+weaponR+" (Glove, Epic)" + "\n"
        if (weaponR in gloveRare):
            print("Weapon: "+weaponR+" (Glove, Rare)")
            text = text + "Weapon: "+weaponR+" (Glove, Rare)" + "\n"      
    if (weaponR in tonfa):
        if (weaponR in tonfaLegendary):
            print("Weapon: "+weaponR+" (Tonfa, Legendary)")
            text = text + "Weapon: "+weaponR+" (Tonfa, Legendary)" + "\n"
        if (weaponR in tonfaEpic):
            print("Weapon: "+weaponR+" (Tonfa, Epic)")
            text = text + "Weapon: "+weaponR+" (Tonfa, Epic)" + "\n"
        if (weaponR in tonfaRare):
            print("Weapon: "+weaponR+" (Tonfa, Rare)")      
            text = text + "Weapon: "+weaponR+" (Tonfa, Rare)" + "\n"
    if (weaponR in guitar):
        if (weaponR in guitarLegendary):
            print("Weapon: "+weaponR+" (Guitar, Legendary)")
            text = text + "Weapon: "+weaponR+" (Guitar, Legendary)" + "\n"
        if (weaponR in guitarEpic):
            print("Weapon: "+weaponR+" (Guitar, Epic)")
            text = text + "Weapon: "+weaponR+" (Guitar, Epic)" + "\n"
        if (weaponR in guitarRare):
            print("Weapon: "+weaponR+" (Guitar, Rare)")       
            text = text + "Weapon: "+weaponR+" (Guitar, Rare)" + "\n"
    
    #GENERATE ARMOR
    headR = head[headN]
    if (headR in headLegendary):
        print("Head: "+headR+" (Legendary)")
        text = text + "Head: "+headR+" (Legendary)" + "\n"
    if (headR in headEpic):
        print("Head: "+headR+" (Epic)")
        text = text + "Head: "+headR+" (Epic)" + "\n"
    if (headR in headRare):
        print("Head: "+headR+" (Rare)")
        text = text + "Head: "+headR+" (Rare)" + "\n"
    
    chestR = chest[chestN]
    if (chestR in chestLegendary):
        print("Chest: "+chestR+" (Legendary)")
        text = text + "Chest: "+chestR+" (Legendary)" + "\n"
    if (chestR in chestEpic):
        print("Chest: "+chestR+" (Epic)")
        text = text + "Chest: "+chestR+" (Epic)" + "\n"
    if (chestR in chestRare):
        print("Chest: "+chestR+" (Rare)")    
        text = text + "Chest: "+chestR+" (Rare)" + "\n"
        
    armR = arm[armN]
    if (armR in armLegendary):
        print("Arm: "+armR+" (Legendary)")
        text = text + "Arm: "+armR+" (Legendary)" + "\n"
    if (armR in armEpic):
        print("Arm: "+armR+" (Epic)")
        text = text + "Arm: "+armR+" (Epic)" + "\n"
    if (armR in armRare):
        print("Arm: "+armR+" (Rare)")
        text = text + "Arm: "+armR+" (Rare)" + "\n"
        
    legR = leg[legN]
    if (legR in legLegendary):
        print("Leg: "+legR+" (Legendary)")
        text = text + "Leg: "+legR+" (Legendary)" + "\n"
    if (legR in legEpic):
        print("Leg: "+legR+" (Epic)")
        text = text + "Leg: "+legR+" (Epic)" + "\n"
    if (legR in legRare):
        print("Leg: "+legR+" (Rare)")
        text = text + "Leg: "+legR+" (Rare)" + "\n"
    
    accessoryR = accessory[accessoryN]
    if (accessoryR in accessoryLegendary):
        print("Accessory: "+accessoryR+" (Legendary)")
        text = text + "Accessory: "+accessoryR+" (Legendary)" + "\n"
    if (accessoryR in accessoryEpic):
        print("Accessory: "+accessoryR+" (Epic)")
        text = text + "Accessory: "+accessoryR+" (Epic)" + "\n"
    if (accessoryR in accessoryRare):
        print("Accessory: "+accessoryR+" (Rare)")
        text = text + "Accessory: "+accessoryR+" (Rare)" + "\n"
    
    if (location == 1):
        locationR = locations[locationN]
        print("Starting location: "+ locationR)
        text = text + "Starting location: "+ locationR + "\n"
        
        ReturnedList = [text,headR,chestR,armR,legR,accessoryR,weaponR,champion]
    
    return ReturnedList 
    
class App(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = 'BSER Build Randomizer'
        self.left = 100
        self.top = 100
        #self.size = setFixedSize(320,200)
        self.width = 290
        self.height = 500
        self.initUI()
        self.checkBoxLegendaryState = 1
        self.checkBoxEpicState = 1
        self.checkBoxRareState = 1
        self.checkBoxLocationState = 1
        self.champion = 0
        self.LegendaryColor = "background-color: rgb(212,175,55)"
        self.EpicColor = "background-color: rgb(107,13,185)"
        self.RareColor = "background-color: rgb(39,48,146)"
        app_icon = QIcon()
        app_icon.addFile('Im/Icon.png')
        app.setWindowIcon(app_icon)

 
        
    
    def initUI(self):
        self.setWindowTitle(self.title)
        #self.setStyle()
        self.setGeometry(self.left, self.top,self.width,self.height)
        self.setFixedSize(410,410)
        button = QPushButton("Randomize",self)
        button.setToolTip("Randomize button")
        button.move(12,100)
        button.clicked.connect(self.on_click)
        
        buttonClear = QPushButton("Clear",self)
        buttonClear.setToolTip("Clear button")
        buttonClear.move(12,120)
        buttonClear.clicked.connect(self.on_click_clear)
        
        checkBoxLegendary = QCheckBox("Include legendary items",self)
        checkBoxLegendary.move(12,12)
        checkBoxLegendary.setChecked(True)
        checkBoxLegendary.stateChanged.connect(self.LegendaryChangeState)
        
        checkBoxEpic = QCheckBox("Include epic items",self)
        checkBoxEpic.move(12,32)
        checkBoxEpic.setChecked(True)
        checkBoxEpic.stateChanged.connect(self.EpicChangeState)
        
        checkBoxRare = QCheckBox("Include rare items",self)
        checkBoxRare.move(12,52)
        checkBoxRare.setChecked(True)
        checkBoxRare.stateChanged.connect(self.RareChangeState)
        
        checkBoxLocation = QCheckBox("Randomize location",self)
        checkBoxLocation.move(12,72)
        checkBoxLocation.setChecked(True)
        checkBoxLocation.stateChanged.connect(self.LocationChangeState)        
        
        championLabel = QLabel("Champion:",self)
        championLabel.move(12,74)
        self.championComboBox = QComboBox(self)
        self.championComboBox.move(65,72)
        self.championComboBox.addItems(["Any","Aya","Fiora","Hart","HyunWoo","Isol","Jackie","Magnus","Nadine","Zahir"])
        self.championComboBox.currentIndexChanged.connect(self.ChampionChange)
        
        self.textLabels = QLabel(self)
        #self.textLabels.move (150,12)
        
        
        
        self.ImageHead = QLabel(self)
        #pixmapHead = QPixmap('Chinese Opera Mask.png')
        #self.ImageLabel1.setPixmap(pixmap1)
        self.ImageHead.setStyleSheet("")
        
        
        self.ImageChest = QLabel(self)
        #pixmap2 = QPixmap('Chinese Opera Mask.png')
        #ImageLabel2.setPixmap(pixmap2)
        #self.ImageChest.setStyleSheet("background-color: magenta")
        
        
        self.ImageArm = QLabel(self)
        #pixmap3 = QPixmap('Chinese Opera Mask.png')
        #ImageLabel3.setPixmap(pixmap3)
        #self.ImageArm.setStyleSheet("background-color: purple")
        
        
        self.ImageLeg = QLabel(self)
        #pixmap4 = QPixmap('Chinese Opera Mask.png')
        #ImageLabel4.setPixmap(pixmap4)
        #self.ImageLeg.setStyleSheet("background-color: rgb(107,13,185)")
       
        
        self.ImageAccessory = QLabel(self)
        #x = 'Im\Chinese Opera Mask'+'.png'
        #print(type(x))
        #pixmap5 = QPixmap(x)
        #ImageLabel5.setPixmap(pixmap5)
        #self.ImageAccessory.setStyleSheet("background-color: rgb(150,40,240)")
       
        self.ImageChampion = QLabel(self)
        #pixmapChampion = QPixmap("Im/Jackie.png").scaledToHeight(100)
        #self.ImageChampion.setPixmap(pixmapChampion)
        
        self.ImageWeapon = QLabel(self)
        #pixmapWeapon = QPixmap("Im/_Glacial Ice.png")
        #self.ImageWeapon.setPixmap(pixmapWeapon)
        #self.ImageWeapon.setStyleSheet("background-color: red")
        
        hboxChamp = QHBoxLayout()
        hboxChamp.addWidget(championLabel,1)
        hboxChamp.addWidget(self.championComboBox,3) 
    
        
        vboxPic = QVBoxLayout()
        vboxPic.addWidget(self.ImageWeapon)
        vboxPic.addWidget(self.ImageHead)
        vboxPic.addWidget(self.ImageChest)
        vboxPic.addWidget(self.ImageArm)
        vboxPic.addWidget(self.ImageLeg)
        vboxPic.addWidget(self.ImageAccessory)
        vboxPic.setAlignment(Qt.AlignHCenter)
        
        
        vboxCheck = QVBoxLayout()
        vboxCheck.addWidget(checkBoxLegendary)
        vboxCheck.addWidget(checkBoxEpic)
        vboxCheck.addWidget(checkBoxRare)    
        vboxCheck.addWidget(checkBoxLocation)
        
        hboxTop = QHBoxLayout()
        hboxTop.addLayout(vboxCheck)
        hboxTop.addWidget(self.ImageChampion)
        
        #hboxBot = QHBoxLayout()
        #hboxBot.addStretch(1)
        #hboxBot.addWidget(self.ImageWeapon)
        
        vbox = QVBoxLayout()
        #vbox.addLayout(hboxTop)
        vbox.addLayout(hboxChamp)
        vbox.addWidget(button)
        vbox.addWidget(buttonClear)
        vbox.addWidget(self.textLabels)
        vbox.addStretch(1)
        
        vbox1 = QVBoxLayout()
        vbox1.addLayout(hboxTop,3)
        vbox1.addLayout(vbox,8)
        
        #vboxAll = QVBoxLayout()
        #vboxAll.addLayout(vbox,210)
        #vboxAll.addLayout(hboxBot,50)
        
        hboxB = QHBoxLayout()
        hboxB.addLayout(vbox1,5)
        #hboxB.addStretch(1)
        hboxB.addLayout(vboxPic,2)
        
        self.setLayout(hboxB)

        self.show()
     
    def on_click(self):
        self.ReturnedList = Randomize(self.champion,self.checkBoxLegendaryState,self.checkBoxEpicState,self.checkBoxRareState,self.checkBoxLocationState)
        self.textToDisplay = self.ReturnedList[0]
        self.updateText()
            
    def on_click_clear(self):
        self.textToDisplay = ("")
        self.textLabels.setText(str(self.textToDisplay))
        
        self.ImageWeapon.setPixmap(QPixmap(""))
        self.ImageWeapon.setStyleSheet("")
        
        self.ImageHead.setPixmap(QPixmap(""))
        self.ImageHead.setStyleSheet("")
        
        self.ImageChest.setPixmap(QPixmap(""))
        self.ImageChest.setStyleSheet("")
        
        self.ImageArm.setPixmap(QPixmap(""))
        self.ImageArm.setStyleSheet("")
        
        self.ImageLeg.setPixmap(QPixmap(""))
        self.ImageLeg.setStyleSheet("")
        
        self.ImageAccessory.setPixmap(QPixmap(""))
        self.ImageAccessory.setStyleSheet("")
        
        self.ImageChampion.setPixmap(QPixmap(""))
        self.ImageChampion.setStyleSheet("")
        
    def updateText(self):
        self.textLabels.setText(str(self.textToDisplay))
        
        pixmapWeapon = QPixmap("Im/"+str(self.ReturnedList[6])+".png")
        self.ImageWeapon.setPixmap(pixmapWeapon)
        if self.ReturnedList[6] in legendaryAll:
            self.ImageWeapon.setStyleSheet(self.LegendaryColor)
        if self.ReturnedList[6] in epicAll:
            self.ImageWeapon.setStyleSheet(self.EpicColor)
        if self.ReturnedList[6] in rareAll:
            self.ImageWeapon.setStyleSheet(self.RareColor)
        
        pixmapHead = QPixmap("Im/"+str(self.ReturnedList[1])+".png")
        self.ImageHead.setPixmap(pixmapHead)
        if self.ReturnedList[1] in legendaryAll:
            self.ImageHead.setStyleSheet(self.LegendaryColor)
        if self.ReturnedList[1] in epicAll:
            self.ImageHead.setStyleSheet(self.EpicColor)
        if self.ReturnedList[1] in rareAll:
            self.ImageHead.setStyleSheet(self.RareColor)
            
        pixmapChest = QPixmap("Im/"+str(self.ReturnedList[2])+".png")
        self.ImageChest.setPixmap(pixmapChest)
        if self.ReturnedList[2] in legendaryAll:
            self.ImageChest.setStyleSheet(self.LegendaryColor)
        if self.ReturnedList[2] in epicAll:
            self.ImageChest.setStyleSheet(self.EpicColor)
        if self.ReturnedList[2] in rareAll:
            self.ImageChest.setStyleSheet(self.RareColor)
            
        pixmapArm = QPixmap("Im/"+str(self.ReturnedList[3])+".png")
        self.ImageArm.setPixmap(pixmapArm)
        if self.ReturnedList[3] in legendaryAll:
            self.ImageArm.setStyleSheet(self.LegendaryColor)
        if self.ReturnedList[3] in epicAll:
            self.ImageArm.setStyleSheet(self.EpicColor)
        if self.ReturnedList[3] in rareAll:
            self.ImageArm.setStyleSheet(self.RareColor)
            
        pixmapLeg = QPixmap("Im/"+str(self.ReturnedList[4])+".png")
        self.ImageLeg.setPixmap(pixmapLeg)
        if self.ReturnedList[4] in legendaryAll:
            self.ImageLeg.setStyleSheet(self.LegendaryColor)
        if self.ReturnedList[4] in epicAll:
            self.ImageLeg.setStyleSheet(self.EpicColor)
        if self.ReturnedList[4] in rareAll:
            self.ImageLeg.setStyleSheet(self.RareColor)
            
        pixmapAccessory = QPixmap("Im/"+str(self.ReturnedList[5])+".png")
        self.ImageAccessory.setPixmap(pixmapAccessory)
        if self.ReturnedList[5] in legendaryAll:
            self.ImageAccessory.setStyleSheet(self.LegendaryColor)
        if self.ReturnedList[5] in epicAll:
            self.ImageAccessory.setStyleSheet(self.EpicColor)
        if self.ReturnedList[5] in rareAll:
            self.ImageAccessory.setStyleSheet(self.RareColor)
        
        index = self.ReturnedList[7]
        print(index)
        pixmapChampion = QPixmap("Im/"+str(champions[index-1])+".png").scaledToHeight(100)
        self.ImageChampion.setPixmap(pixmapChampion)
        
    def LegendaryChangeState(self,state):
        if state == Qt.Checked:
            self.checkBoxLegendaryState = 1
        else:
            self.checkBoxLegendaryState = 0
    
    def EpicChangeState(self,state):
        if state == Qt.Checked:
            self.checkBoxEpicState = 1
        else:
            self.checkBoxEpicState = 0
            
    def RareChangeState(self,state):
        if state == Qt.Checked:
            self.checkBoxRareState = 1
        else:
            self.checkBoxRareState = 0
    
    def LocationChangeState(self,state):
        if state == Qt.Checked:
            self.checkBoxLocationState = 1
        else:
            self.checkBoxLocationState = 0
    
    def ChampionChange(self,state):
        self.champion = self.championComboBox.currentIndex()
        

if __name__=='__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = App()
    sys.exit(app.exec_())    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

            
