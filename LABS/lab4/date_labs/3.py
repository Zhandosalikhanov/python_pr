from datetime import datetime

def microsec_now():
    x = datetime.today().replace(microsecond= 0)
    return x