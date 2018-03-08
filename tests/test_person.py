import pytest
from habits import Person, Sleep
from datetime import datetime, timedelta, time

@pytest.fixture()
def person_glen():
    p = Person('Glen', sleep_hours_goal=timedelta(hours=8),
        sleep_wake_goal=time(5, 30))
    p.sleep_history.extend([
        Sleep(datetime(2018, 2, 19, 22, 0), datetime(2018, 2, 20, 5, 45)),        
        Sleep(datetime(2018, 2, 20, 22, 0), datetime(2018, 2, 21, 5, 30)),        
        Sleep(datetime(2018, 2, 21, 23, 0), datetime(2018, 2, 22, 5, 0)),        
        Sleep(datetime(2018, 2, 22, 20, 30), datetime(2018, 2, 23, 5, 15)),        
        Sleep(datetime(2018, 2, 23, 23, 0), datetime(2018, 2, 24, 4, 30)),
        Sleep(datetime(2018, 2, 24, 23, 0), datetime(2018, 2, 25, 6, 0)),
        Sleep(datetime(2018, 2, 25, 22, 0), datetime(2018, 2, 26, 5, 0)),
    ])
    return p

def test_score_sleep(person_glen):
    sleep_score = person_glen.score_sleep()
    assert sleep_score == 6