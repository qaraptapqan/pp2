from datetime import datetime, timedelta
print(f'Today is {datetime.today(): %Y-%m-%d}, five days ago: {datetime.today()-timedelta(days=5):%Y-%m-%d}')
