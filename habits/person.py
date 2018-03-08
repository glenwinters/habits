from collections import namedtuple

Sleep = namedtuple('Sleep', ['start', 'end'])

class ScoreError(Exception):
    """Error calculating score"""


class Person(object):
    def __init__(self, name, sleep_hours_goal=None, sleep_wake_goal=None):
        self.name = name
        self.sleep_history = []
        self.sleep_hours_goal = sleep_hours_goal
        self.sleep_wake_goal = sleep_wake_goal
    
    def __repr__(self):
        return '<Person(name="{}")>'.format(self.name)

    def score_sleep(self):
        """Scores last 7 days of sleep history out of 14 points

        1 point per day where the hours goal was met
        1 point per day where the wake time goal was met
        """
        if len(self.sleep_history) < 7:
            raise ScoreError('Need at least 7 days of sleep history')
        elif self.sleep_hours_goal is None:
            raise ScoreError('Sleep hours goal not set')
        elif self.sleep_wake_goal is None:
            raise ScoreError('Sleep wake goal not set')

        hours_score = 0
        wake_score = 0
        for sleep in self.sleep_history:
            if sleep.end - sleep.start >= self.sleep_hours_goal:
                hours_score += 1
            if sleep.end.time() <= self.sleep_wake_goal:
                wake_score += 1
        return hours_score + wake_score
