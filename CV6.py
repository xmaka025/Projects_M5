import datetime

now = datetime.datetime.now()
print(now)
print(now.strftime("%A"))
year = now.year
if year % 100 == 0:
    print(f"{year} = Невисокосный")
elif year % 400 == 0:
    print(f"{year} = Високосный")
elif year % 4 == 0:
    print(f"{year} = Високосный")
else:
    print(f"{year} = Невисокосный")

date = input('Введите дату (год-месяц-день): ')
date_user = datetime.datetime.strptime(date, "%Y-%m-%d")
if date_user > now:
    y = date_user - now
    days = y.days
    hours = y.seconds // 3600
    minut = (y.seconds % 3600) // 60
    print(f"Разница между состовляет {date_user} и {now} {days} дней, {hours} часов, {minut} минут.")
else:
    y = now - date_user
    days = y.days
    hours = y.seconds // 3600
    minut = (y.seconds % 3600) // 60
    print(f"Разница между состовляет {now} и {date_user} {days} дней, {hours} часов,{minut} минут.")
