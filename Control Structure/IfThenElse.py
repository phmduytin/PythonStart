for i in range(0, 10):
    if i % 2 == 0:
        print(i, end=', ')
    print()

workday = ['Monday', 'Tuesday', 'Wednesday', 'Thusday', 'Friday']
weekend = ['Saturday', 'Sunday']
holiday = ['30/04', '01/05', '02/09']
day = 'Monday'
date = '30/05'

if day in weekend or date in holiday:
    print('Let\'s fun')
else:
    print('Go to work')









