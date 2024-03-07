import tkinter as tk

EnergyRing = {
    'Aquario': (4,4,4),
    'Aquila': (2,1,3),
    'Escolpio': (5,0,1),
    'Anubis': (2,1,1),
    'Aquila': (2,1,3),
    'Blaze': (2,2,1),
    'Cancer': (3,4,3),
    'Capricorne': (3,2,1),
    'Gemios': (1,1,1),
    'Giraffe': (2,1,1),
    'Leone': (1,1,2),
    'Horuseus': (2,1,1),
    'Perseus': (4,1,1),
    'Herculeo': (3,3,3),
    'WEELMAGNIE': (5,1,1),
    'Phoenix': (2,1,2),
    'Gil': (3,1,1),
    'Cygnus': (2,5,3),
    'Gemios': (0,0,1),
    'Pisces': (1,1,3),
    'Kerbecs': (4,4,4),
    'Serpent': (2,2,1),
    'Byxis': (3,2,2)
}

FusionWheel = {
    'Earth': (1,4,4),
    'Flash': (5,1,3),
    'Galaxy': (3,1,1),
    'Hell': (4,3,3),
    'Screw': (4,1,3),
    'Vulcan': (4,1,3),
    'Sol': (1,3,1),
    'Virgo': (1,2,4),
    'Poison': (0,0,0),
    'Bakushin':	(1,4,3),
    'Thermal': (1,2,3),
    'Libra': (1,4,3),
    'Pisces': (1,3,3),
    'Escolpio':	(1,2,2),
    'Flame': (1,2,4),
    'Burn':	(1,3,4),
    'Dark':	(1,2,2),
    'Divine': (-100,-100,-100),
    'Duo': (1,5,5),
    'Grand': (1,3,3),
    'Infinity': (1,2,3),
    'Mercury': (1,1,1),
    'Phantom': (1,5,5),
    'Scythe': (1,2,5),
    'Rock': (2,1,1),
    'Storm': (3,1,2),
    'Gravity': (4,1,1),
    'Cyclone': (3,1,2),
    'Screw': (4,1,2),
    'Variares': (5,1,1),
    'Ray': (4,1,2),
    'Evil': (1,1,2),
    'Wing': (3,5,3)
}

SpinTrack = {
    '85': (5,1,5),
    'GB145': (3,5,5),
    '230': (3,5,4),
    'R145': (4,5,3),
    'C145': (3,4,4),
    'ED145': (3,3,3),
    'WD145': (3,1,1),
    'BD145': (3,5,4),
    '105': (4,1,4),
    'CH120': (4,3,4),
    '90': (5,1,5),
    'M145': (1,1,-21),
    'UW145': (2,2,4),
    '145': (3,1,4),
    'DF145': (1,2,1),
    '125': (4,3,4),
    'D125':	(2,3,3),
    'W105':	(3,1,1),
    'AD145': (2,4,5),
    'LW105': (3,2,1),
    '135': (2,1,2),
    'V145': (3,3,3),
    'TR145': (2,4,4),
    'SP230': (3,5,4),
    'S130': (3,4,3),
    '100': (4,1,4),
    'H145': (4,1,1),
    'T125': (4,3,4),
    'WA130': (4,3,2),
    'SW145': (3,3,3),
}

PerformanceTip = {
    'BS': (1,1,3),
    'RS': (2,5,2),
    'RF': (5,2,1),
    'EWD': (1,3,5),
    'F': (3,1,1),
    'DS': (1,5,5),
    'CS': (3,5,1),	
    'HF': (4,1,2),
    'D': (1,3,5),
    'HF/S': (4,1,3),
    'WD': (1,3,5),
    'S': (1,1,3), 	
    'Q': (4,1,1),
    'B': (1,3,3),
    'SF': (3,1,3),
    'WF': (4,1,1),
    'JB': (2,2,2),
    'AS': (1,1,3),
    'LF': (4,1,1),
    'ES': (1,1,4),
    'RS': (2,5,2),
    'FB': (2,3,2),
    'MF': (5,1,2),
    'MB': (1,4,4),
    'FS': (3,1,3),
    'WB': (1,4,3),
    'SD': (1,3,5),
    'R²F': (5,2,1),
    'RSF': (4,5,1),
    'XF': (4,1,1),
    'MS': (1,1,4)                                                                                                                                                                                                            
}

print("KOM, WE GON IS ZIEN OF DIEJE COMBINATSE WEL GOE IS")
print("GEEFT IS EEN RINGESKE")
ringeske = input()
print("GEEFT IS EEN IJZER")
ijzer = input()
print("GEEFT IS NE SPINTRACK")
flieter = input()
print("ALS LOTSTE, GEEFT IS NEN TIP")
tip = input()

BleebleetAanval = EnergyRing[ringeske][0]+FusionWheel[ijzer][0]+SpinTrack[flieter][0]+PerformanceTip[tip][0]
BleebleetVerdediging = EnergyRing[ringeske][1]+FusionWheel[ijzer][1]+SpinTrack[flieter][1]+PerformanceTip[tip][1]
BleebleeUithouding = EnergyRing[ringeske][2]+FusionWheel[ijzer][2]+SpinTrack[flieter][2]+PerformanceTip[tip][2]

print(f"DEN AANVAL IS {BleebleetAanval}, DEN VERDEDIGING IS {BleebleetVerdediging} EN'T UITHOUDINGSVERMOGEN IS {BleebleeUithouding}")
print("EN TRAPT HET NEI AF")

