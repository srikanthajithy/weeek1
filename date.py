import datetime


def time():
    today = datetime.date.today()
    t1 = today.strftime("%d/%m/%y")
    print("t1=", time)


def now():
    now = datetime.datetime.now()
    print("now =", now)
