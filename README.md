# Overtime

Write a function that calculates the days on which overtime is payable, and how much.

## Background

Freelancers work a standard 8 hour working day, 5 days per week, giving a total of 40 hours. Any work done over the 40 hour limit is subject to overtime. On a weekly-basis this is a simple calculation - `total-hours - 40 = overtime`.

The challenge comes when you try and determine on which day they did the overtime - e.g. if a freelancer works 42 hours, and are due 2 hours’ overtime pay, to which day does this refer?

The table below shows a set of example weeks, with the days on which overtime should be paid highlighted with an ‘*’.

| | Week 1 |  Week 2 | Week 3 | Week 4 | Week 5 | Week 6 | Week 7|
| - |  - |  - |   - | -- | -- |  -|  -|
| Monday |  8 |   8 |   6 |   12* |  16 |  6|   8|
| Tuesday | 8 |   8 |   6 |   8 |   16 |  6|   8|
| Wednesday |   8 |   8 |   6 |   4 |   0 |   6|   8|
| Thursday |    8 |   8 |   6 |   8 |   0 |   6|   8|
| Friday |  0 |   8 |   6 |   8 |   0 |   6|   8|
| Saturday |    8 |   8* |   12* |  2 |   0 |   6|   0|
| Sunday |  0 |   0 |   0 |   0 |   0 |   6*|   0|
| Hours worked |    40 |  48 |  42 |  42 |  32|  42|  40 |
| Overtime |    0 |   8 |   2 |   2 |   0 |   2|   0|

## Test

The test is to write a single function that will accept a list of 7 integer arguments representing the hours worked on each day, and return a corresponding list with the number of hours of overtime payable on each day.

This repo contains a single module (`overtime.py`), that contains an empty function, `overtime`, which you should edit, and a single test that you should work to.
