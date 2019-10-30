"""
The following is the question scope from https://interviewcake.com:
Your company built an in-house calendar tool called HiCal. You want to add a
feature to see the times in a day when everyone is available. To do this,
you’ll need to know when any team is having a meeting. In HiCal, a meeting is
stored as a tuple of integers (start_time, end_time). These integers
represent the number of 30-minute blocks past 9:00am.

Do not assume the meetings are in order. The meeting times are coming
from multiple teams. Write a solution that's efficient even when we can't put
a nice upper bound on the numbers representing our time ranges. Here we've
simplified our times down to the number of 30-minute slots past 9:00 am. But
we want the function to work even for very large numbers, like Unix timestamps.
In any case, the spirit of the challenge is to merge meetings where start_time
and end_time don't have an upper bound.
"""

# List of tuples for hours in a workday. 0 is 9 AM.
uncondensed_data = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

def merge_ranges(meetings):
