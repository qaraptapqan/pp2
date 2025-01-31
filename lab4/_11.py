from datetime import datetime, timedelta
print(f'Yesterday was {datetime.today()-timedelta(days=1):%y-%m-%d}, today is {datetime.today():%Y-%m-%d} and tommorow will be {datetime.today()+timedelta(days=1):%y-%m-%d}')
