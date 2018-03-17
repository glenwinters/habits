from habits.goal import SleepGoal
from habits.exceptions import ScoreError, GoalError


class Person(object):
    def __init__(self, name):
        self.name = name
        self.history = []
        self.goals = []

    def __repr__(self):
        return '<Person(name="{}")>'.format(self.name)

    def add_goal(self, goal):
        existing_goal = [g for g in self.goals if isinstance(g, goal.__class__)]
        if len(existing_goal) != 0:
            raise GoalError('Goal type already exists')
        self.goals.append(goal)

    def score_sleep(self):
        sleep_goals = [g for g in self.goals if isinstance(g, SleepGoal)]
        if len(sleep_goals) == 0:
            raise ScoreError('No sleep goals to score')
        return sum([g.score(self.history) for g in sleep_goals])

    def score_food(self):
        food_goals = [g for g in self.goals if isinstance(g, FoodGoal)]
        if len(food_goals) == 0:
            raise ScoreError('No food goals to score')
        return sum([g.score(self.history) for g in food_goals])
