from datetime import datetime

def yest_tod_tom():
    x = datetime.now()
    ans = int(x.strftime("%d"))
    return(ans - 1, ans, ans + 1)