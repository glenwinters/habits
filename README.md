# habits

[![Build Status](https://travis-ci.org/glenwinters/habits.svg?branch=master)](https://travis-ci.org/glenwinters/habits)
[![codecov](https://codecov.io/gh/glenwinters/habits/branch/master/graph/badge.svg)](https://codecov.io/gh/glenwinters/habits)
[![Linty](https://www.lintyapp.com/repo/glenwinters/habits/badge.svg)](https://www.lintyapp.com/repo/glenwinters/habits)

Score your habits.

## Example

```python
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
])
p.add_goal(WakeTimeGoal(time(5, 0)))
sleep_score = p.score_sleep()
print(sleep_score)
```

The result would be 3 because one point is given per day that the sleep goal is met in the last 7 days.
