import datetime
class SuperDate():
    def __init__(self, year, month, day, hour):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour

    def get_season(self):

        if self.month in range(3, 6):
            return 'Spring'
        elif self.month in range(6, 9):
            return 'Summer'
        elif self.month in range(9, 12):
            return 'Autumn'
        else:
            return 'Winter'

    def get_time_of_day(self):

        if self.hour in range(6, 12):
            return 'Morning'
        elif self.hour in range(12, 18):
            return 'Day'
        elif self.hour in range(18, 0):
            return 'Evening'
        else:
            return 'Night'


a = SuperDate(2024, 2, 22, 12)
print(a.get_season())
print(a.get_time_of_day())
