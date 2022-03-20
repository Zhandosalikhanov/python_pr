from datetime import datetime

def five_days_ago():
    x = datetime.now()
    return int(x.strftime("%d")) - 5