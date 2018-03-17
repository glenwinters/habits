class Event(object):
    """Base event"""


class SleepEvent(Event):
    """One event of sleeping"""
    def __init__(self, start, end):
        self.start = start
        self.end = end


class FoodEvent(Event):
    """One day of eating"""
    def __init__(self, date, calories):
        self.date = date
        self.calories = calories
