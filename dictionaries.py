# make a dictionary for nine Tampa Bay Rays (see below).
# You can make up the player names. These are old.
# Use the player names as keys and a list for each value. See page 374.
# Each value list should hold the position played by the player, the batting order, and
# current batting average.

# Next, use loop(s) to print the "lineup" (the dictionary in batting order).
# Duplicate the sample output for full points.
# Pull Rivera and DeJesus. Substitute Wilson as catcher and Beckham as DH (see sample output).
# Reprint the new lineup.

# 9 Tampa Bay Ray's players dictionary
TampaBayRaysTeam = {
    "Chris Archer"  : ["DH", 6, 299],
    "Matt Andriese" : ["1B", 4, 222],
    "Brad Boxberge" : ["C",  9, 194] ,
    "Xavier Cedeno" : ["2B", 5, 304],
    "Alex Cobb"     : ["RF", 2, 229],
    "Alex Colome"   : ["3B", 3, 282],
    "Jacob Fairia"  : ["SS", 7, 214],
    "Eddie Gamboa"  : ["CF", 1, 240],
    "Ryan Garton"   : ["LF", 8, 274]
}

# Ray's starter code
print("Rays Starters: \n")
for key, value in TampaBayRaysTeam.items():
    print(key, value)
print('\n')

# Today's lineup code
print("Today's lineup: \n")
i = 1
numItems = len(TampaBayRaysTeam)
for key, value in TampaBayRaysTeam.items():
    if(value[1] == i):
        print("Batting",i,":",value[0],key)
        i += 1
        
# Lineup change code
