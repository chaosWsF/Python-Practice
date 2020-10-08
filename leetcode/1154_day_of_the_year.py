"""
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

Example 1:

    Input: date = "2019-01-09"
    Output: 9
    Explanation: Given date is the 9th day of the year in 2019.

Example 2:

    Input: date = "2019-02-10"
    Output: 41

Example 3:

    Input: date = "2003-03-01"
    Output: 60

Example 4:

    Input: date = "2004-03-01"
    Output: 61

Constraints:
    1. date.length == 10
    2. date[4] == date[7] == '-', and all other date[i]'s are digits
    3. date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
"""

import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        t1 = datetime.date.fromisoformat(date)
        t2 = datetime.date(t1.year, 1, 1)
        return (t1 - t2).days + 1
    
    def dayOfYear2(self, date: str) -> int:
        d = list(map(int, date.split('-')))
        nday_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        res = sum(nday_per_month[i] for i in range(d[1] - 1)) + d[2]
        return res + 1 if d[1] >= 3 and d[0] % 4 == 0 and d[0] != 1900 else res
