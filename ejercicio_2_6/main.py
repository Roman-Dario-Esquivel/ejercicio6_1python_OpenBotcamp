from datetime import datetime as dt
import time 
import datetime
hh =  dt.now()
print(hh)
if hh.hour>=19:
    print("hora de irse a casa")
elif hh.hour==18:
    min = 60-hh.minute
    print("Faltan tantos minutos para salir del trabajo: ",min)
else :
    time_1 = datetime.timedelta(hours= 19, minutes=0, seconds=0)
    time_2 = datetime.timedelta(hours= hh.hour, minutes=hh.minute, seconds=hh.second)
    print("Faltan para las 19 hs: ",time_1 - time_2)


