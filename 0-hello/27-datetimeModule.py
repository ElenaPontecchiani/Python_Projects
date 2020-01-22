import datetime
import pty

today= datetime.date.today()
print(today)

birthday= datetime.date(1997, 2, 28)
days_in_this_sad_life = (today - birthday).days
print(days_in_this_sad_life)

tdelta = datetime.timedelta(days=10)
ten_days_after_today = today + tdelta
print(ten_days_after_today)