import pytest
from datetime import datetime, date, timedelta, time

from habits import Person
from habits import SleepEvent, FoodEvent
from habits import SleepHoursGoal, WakeTimeGoal, CaloriesGoal
from habits import ScoreError, GoalError


@pytest.fixture()
def person_with_history():
    p = Person('Glen')
    p.history.extend([
        SleepEvent(start=datetime(2018, 2, 19, 22, 0),
                   end=datetime(2018, 2, 20, 5, 45)),
        SleepEvent(start=datetime(2018, 2, 20, 22, 0),
                   end=datetime(2018, 2, 21, 5, 30)),
        SleepEvent(start=datetime(2018, 2, 21, 23, 0),
                   end=datetime(2018, 2, 22, 5, 0)),
        SleepEvent(start=datetime(2018, 2, 22, 20, 30),
                   end=datetime(2018, 2, 23, 5, 15)),
        SleepEvent(start=datetime(2018, 2, 23, 23, 0),
                   end=datetime(2018, 2, 24, 4, 30)),
        SleepEvent(start=datetime(2018, 2, 24, 23, 0),
                   end=datetime(2018, 2, 25, 6, 0)),
        SleepEvent(start=datetime(2018, 2, 25, 22, 0),
                   end=datetime(2018, 2, 26, 5, 0)),
        FoodEvent(date(2018, 2, 18), 2000),
        FoodEvent(date(2018, 2, 19), 2146),
        FoodEvent(date(2018, 2, 20), 1727),
        FoodEvent(date(2018, 2, 21), 2075),
        FoodEvent(date(2018, 2, 22), 3127),
        FoodEvent(date(2018, 2, 23), 1996),
        FoodEvent(date(2018, 2, 24), 1802),
        FoodEvent(date(2018, 2, 25), 1799),
    ])
    return p


def test_person_repr():
    p = Person('Glen')
    assert str(p) == '<Person(name="Glen")>'


def test_person_goal_already_exists():
    p = Person('Glen')
    p.add_goal(SleepHoursGoal(timedelta(hours=8)))
    with pytest.raises(GoalError) as e:
        p.add_goal(SleepHoursGoal(timedelta(hours=8)))
    assert 'Goal type already exists' in str(e.value)


def test_score_sleep(person_with_history):
    p = person_with_history
    p.add_goal(SleepHoursGoal(timedelta(hours=8)))
    p.add_goal(WakeTimeGoal(time(5, 30)))
    sleep_score = p.score_sleep()
    assert sleep_score == 6


def test_score_sleep_wake_no_history():
    p = Person('Glen')
    p.add_goal(WakeTimeGoal(time(5, 30)))
    with pytest.raises(ScoreError) as e:
        sleep_score = p.score_sleep()
    assert 'sleep history' in str(e.value)


def test_score_sleep_hours_no_history():
    p = Person('Glen')
    p.add_goal(SleepHoursGoal(timedelta(hours=8)))
    with pytest.raises(ScoreError) as e:
        sleep_score = p.score_sleep()
    assert 'sleep history' in str(e.value)


def test_score_sleep_no_goals(person_with_history):
    p = person_with_history
    with pytest.raises(ScoreError) as e:
        sleep_score = p.score_sleep()
    assert 'No sleep goals' in str(e.value)


def test_score_food(person_with_history):
    p = person_with_history
    p.add_goal(CaloriesGoal(2000))
    food_score = p.score_food()
    assert food_score == 4


def test_score_food_no_history():
    p = Person('Glen')
    p.add_goal(CaloriesGoal(2000))
    with pytest.raises(ScoreError) as e:
        food_score = p.score_food()
    assert 'food history' in str(e.value)


def test_score_food_no_goals(person_with_history):
    p = person_with_history
    with pytest.raises(ScoreError) as e:
        food_score = p.score_food()
    assert 'No food goals' in str(e.value)
