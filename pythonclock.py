from datetime import datetime
import pytz

local = datetime.now()
print("NYC:", local.strftime("%H:%M:%S"))


time_argentina = pytz.timezone('America/Argentina/Buenos_Aires')
datetime_ag = datetime.now(time_argentina)
print("Argentina:", datetime_ag.strftime("%H:%M:%S"))

time_poland = pytz.timezone('Europe/Warsaw')
datetime_Poland = datetime.now(time_poland)
print("Poland:", datetime_Poland.strftime("%H:%M:%S"))

time_la = pytz.timezone('America/Los_Angeles')
datetime_la = datetime.now(time_la)
print("Los Angeles:", datetime_la.strftime("%H:%M:%S"))

time_hi = pytz.timezone('Pacific/Honolulu')
datetime_hi = datetime.now(time_hi)
print("Hawaii:", datetime_hi.strftime("%H:%M:%S"))
