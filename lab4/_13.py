from datetime import datetime

Y, m, d, H, M, S = map(int, input("Enter first year, month, day, hour, minute, second: ").split())
date1 = datetime(Y, m, d, H, M, S)
Y, m, d, H, M, S = map(int, input("Enter second: ").split())
date2 = datetime(Y, m, d, H, M, S)
print(f'Difference is {(date2-date1).total_seconds()}')
