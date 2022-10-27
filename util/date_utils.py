from datetime import datetime


def get_day_name(date):
    day_name = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']
    return day_name[datetime.strptime(date, '%Y-%m-%d').weekday()]
