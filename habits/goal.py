from habits.event import SleepEvent
from habits.exceptions import ScoreError


class Goal(object):
    """Base goal"""


class SleepGoal(Goal):
    """Base sleep goal"""
    def filter_history(self, history):
        return [h for h in history if isinstance(h, SleepEvent)]


class WakeTimeGoal(SleepGoal):
    """"Goal for waking up on time"""
    def __init__(self, wake_time):
        self.wake_time = wake_time

    def score(self, history):
        """1 point per day where the wake time is earlier or equal to the goal"""
        points = 0
        sleep_history = self.filter_history(history)
        if len(sleep_history) < 7:
            raise ScoreError('Need at least 7 days of sleep history')
        for sleep in sleep_history:
            if sleep.end.time() <= self.wake_time:
                points += 1
        return points


class SleepHoursGoal(SleepGoal):
    """"Goal for sleeping enough"""
    def __init__(self, hours):
        self.hours = hours

    def score(self, history):
        """1 point per day where sleep duration is equal to or longer than the goal"""
        points = 0
        sleep_history = self.filter_history(history)
        if len(sleep_history) < 7:
            raise ScoreError('Need at least 7 days of sleep history')
        for sleep in sleep_history:
            if sleep.end - sleep.start >= self.hours:
                points += 1
        return points
