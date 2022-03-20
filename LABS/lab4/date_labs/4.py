from datetime import datetime, date

def two_date_dif(date1, date2):
    return((b - a).seconds)

if __name__ == 'main':
    a = datetime(2022, 2, 26, 8, 35, 20)
    b = datetime(2022, 2, 28, 12, 20, 5)
    print((b - a).seconds)