def speed(level):
    if level == 1: return 175
    if level == 2: return 150
    if level == 3: return 125
    if level == 4: return 100
    if level == 5: return 75
    if level == 6: return 50
    
def Score(level):
    if level == 1: return 10
    if level == 2: return 15
    if level == 3: return 20
    if level == 4: return 25
    if level == 5: return 30
    if level == 6: return '∞'

def level(score):
    if score < 10: return 1
    elif score < 15: return 2
    elif score < 20: return 3
    elif score < 25: return 4
    elif score < 30: return 5
    else: return 6
    