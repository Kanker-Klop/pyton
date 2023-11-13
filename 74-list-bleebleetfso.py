EnergyRing = {
    'Aquario': (4,5,5),
    'Aquila': (2,1,3),
    'Escolpio': (5,0,1),
    'Anubis': (2,1,1),
    'Aquila': (2,1,3),
    'Blaze': (2,2,1),
    'Cancer': (3,4,3)
}
FusionWheel = {
    'Earth': (1,4,4),
    'Flash': (5,1,3),
    'Galaxy': (3,1,1),
    'Hell': (4,3,3),
    'Screw': (4,1,3),
    'Vulcan': (4,1,3),
    'Sol': (1,3,1)
    
}
SpinTrack = {
    '85': (5,1,5),
    'GB145': (3,5,5),
    '230': (3,4,4),
    'R145': (4,5,3),
    'C145': (3,4,4),
    'ED145': (3,3,3)
}
PerformanceTip = {
    'BS': (1,1,3),
    'RS': (2,5,2),
    'RF': (5,2,1),
    'EWD': (1,3,5),
    'F': (3,1,1),
    'DS': (1,5,5)
}

BleebleetVerdediging = EnergyRing["Aquario"][1]+FusionWheel["Earth"][1]+SpinTrack["GB145"][1]+PerformanceTip["RS"][1]
print(BleebleetVerdediging)

