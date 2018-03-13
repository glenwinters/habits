import pytest
from habits import Person, Sleep, Food, ScoreError
from datetime import datetime, date, timedelta, time


@pytest.fixture()
def person_with_histories():
    p = Person('Glen')
    p.sleep_history.extend([
        Sleep(datetime(2018, 2, 18, 21, 0), datetime(2018, 2, 20, 5, 0)),
        Sleep(datetime(2018, 2, 19, 22, 0), datetime(2018, 2, 20, 5, 45)),
        Sleep(datetime(2018, 2, 20, 22, 0), datetime(2018, 2, 21, 5, 30)),
        Sleep(datetime(2018, 2, 21, 23, 0), datetime(2018, 2, 22, 5, 0)),
        Sleep(datetime(2018, 2, 22, 20, 30), datetime(2018, 2, 23, 5, 15)),
        Sleep(datetime(2018, 2, 23, 23, 0), datetime(2018, 2, 24, 4, 30)),
        Sleep(datetime(2018, 2, 24, 23, 0), datetime(2018, 2, 25, 6, 0)),
        Sleep(datetime(2018, 2, 25, 22, 0), datetime(2018, 2, 26, 5, 0)),
    ])
    p.food_history.extend([
        Food(date(2018, 2, 18), 2000),
        Food(date(2018, 2, 19), 2146),
        Food(date(2018, 2, 20), 1727),
        Food(date(2018, 2, 21), 2075),
        Food(date(2018, 2, 22), 3127),
        Food(date(2018, 2, 23), 1996),
        Food(date(2018, 2, 24), 1802),
        Food(date(2018, 2, 25), 1799),
    ])
    return p


def test_person_repr():
    p = Person('Glen')
    assert str(p) == '<Person(name="Glen")>'


def test_score_sleep(person_with_histories):
    p = person_with_histories
    p.sleep_hours_goal = timedelta(hours=8)
    p.sleep_wake_goal = time(5, 30)
    sleep_score = p.score_sleep()
    assert sleep_score == 6


def test_score_sleep_no_history():
    p = Person('Glen')
    with pytest.raises(ScoreError) as e:
        sleep_score = p.score_sleep()
    assert 'sleep history' in str(e.value)


def test_score_sleep_no_hours_goal(person_with_histories):
    p = person_with_histories
    p.sleep_wake_goal = time(5, 30)
    with pytest.raises(ScoreError) as e:
        sleep_score = p.score_sleep()
    assert 'hours goal' in str(e.value)


def test_score_sleep_no_wake_goal(person_with_histories):
    p = person_with_histories
    p.sleep_hours_goal = timedelta(hours=8)

    with pytest.raises(ScoreError) as e:
        sleep_score = p.score_sleep()
    assert 'wake goal' in str(e.value)


def test_score_calories(person_with_histories):
    p = person_with_histories
    p.calorie_goal = 2000
    calorie_score = p.score_calories()
    assert calorie_score == 4


def test_score_calories_no_history():
    p = Person('Glen')
    with pytest.raises(ScoreError) as e:
        calories_score = p.score_calories()
    assert 'food history' in str(e.value)


def test_score_calories_no_calorie_goal(person_with_histories):
    p = person_with_histories

    with pytest.raises(ScoreError) as e:
        calories_score = p.score_calories()
    assert 'Calorie goal' in str(e.value)
