def time_conversion(t):
    if t[-2:]=='AM' and t[:2]=='12':  t='00'+ t[2:-2]
    elif t[-2:] =='AM': t=t[:-2]
    elif t[-2:] =='PM': t = str(12 + int(t[:2])) + t[2:-2]
    print(t)
        

t = '02:00:00PM'
time_conversion(t)