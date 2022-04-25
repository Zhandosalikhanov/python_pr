# Snake characteristics

# Return speed according to level
def speed(level):
    if level == 1: return 175
    if level == 2: return 150
    if level == 3: return 125
    if level == 4: return 100
    if level == 5: return 75
    if level == 6: return 50
    if level == 7: return 35
    if level == 8: return 20
    if level == 9: return 10
    
# Return max score according to level    
def Score(level):
    if level == 1: return 10
    if level == 2: return 30
    if level == 3: return 50
    if level == 4: return 70
    if level == 5: return 90
    if level == 6: return 110
    if level == 7: return 130
    if level == 8: return 150
    if level == 9: return '∞'

# Return level according to score
def level(score):
    if score < 10: return 1
    elif score < 20: return 2
    elif score < 30: return 3
    elif score < 50: return 4
    elif score < 70: return 5
    elif score < 90: return 6
    elif score < 110: return 7
    elif score < 130: return 8
    elif score < 150: return 9
    else: return 10
    