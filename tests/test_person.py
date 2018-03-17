import pytest
from habits import Person, SleepEvent
from habits import SleepHoursGoal, WakeTimeGoal
from habits import ScoreError, GoalError
from datetime import datetime, timedelta, time


@pytest.fixture()
def person_with_sleep_history():
    p = Person('Glen')
    p.history.extend([
        SleepEvent(datetime(2018, 2, 19, 22, 0), datetime(2018, 2, 20, 5, 45)),
        SleepEvent(datetime(2018, 2, 20, 22, 0), datetime(2018, 2, 21, 5, 30)),
        SleepEvent(datetime(2018, 2, 21, 23, 0), datetime(2018, 2, 22, 5, 0)),
        SleepEvent(datetime(2018, 2, 22, 20, 30), datetime(2018, 2, 23, 5, 15)),
        SleepEvent(datetime(2018, 2, 23, 23, 0), datetime(2018, 2, 24, 4, 30)),
        SleepEvent(datetime(2018, 2, 24, 23, 0), datetime(2018, 2, 25, 6, 0)),
        SleepEvent(datetime(2018, 2, 25, 22, 0), datetime(2018, 2, 26, 5, 0)),
    ])
    return p


def test_person_repr():
    p = Person('Glen')
    assert str(p) == '<Person(name="Glen")>'


def test_score_sleep(person_with_sleep_history):
    p = person_with_sleep_history
    p.add_goal(SleepHoursGoal(timedelta(hours=8)))
    p.add_goal(WakeTimeGoal(time(5, 30)))
    sleep_score = p.score_sleep()
    assert sleep_score == 6


def test_score_sleep_no_history():
    p = Person('Glen')
    print(p.goals)
    p.add_goal(SleepHoursGoal(timedelta(hours=8)))
    with pytest.raises(ScoreError) as e:
        sleep_score = p.score_sleep()
    assert 'sleep history' in str(e.value)


def test_score_sleep_no_goals(person_with_sleep_history):
    p = person_with_sleep_history
    with pytest.raises(ScoreError) as e:
        sleep_score = p.score_sleep()
    assert 'No sleep goals' in str(e.value)
