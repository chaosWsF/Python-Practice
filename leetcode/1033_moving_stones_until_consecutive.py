"""
Three stones are on a number line at positions a, b, and c.

Each turn, you pick up a stone at an endpoint (ie., either the lowest or highest position stone), and 
move it to an unoccupied position between those endpoints. Formally, let's say the stones are currently 
at positions x, y, z with x < y < z. You pick up the stone at either position x or position z, and move 
that stone to an integer position k, with x < k < z and k != y.

The game ends when you cannot make any more moves, ie. the stones are in consecutive positions.

When the game ends, what is the minimum and maximum number of moves that you could have made? Return the 
answer as an length 2 array: answer = [minimum_moves, maximum_moves]

Example 1:

    Input: a = 1, b = 2, c = 5
    Output: [1,2]
    Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.

Example 2:

    Input: a = 4, b = 3, c = 2
    Output: [0,0]
    Explanation: We cannot make any moves.

Example 3:

    Input: a = 3, b = 5, c = 1
    Output: [1,2]
    Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.

Note:
    1. 1 <= a <= 100
    2. 1 <= b <= 100
    3. 1 <= c <= 100
    4. a != b, b != c, c != a
"""


class Solution:
    def numMovesStones(self, a: int, b: int, c: int):
        lst = sorted([a, b, c])
        d_1, d_2 = lst[1] - lst[0], lst[2] - lst[1]
        max_moves = d_1 + d_2 - 2
        if d_1 == 1 and d_2 == 1:
            return [0, 0]
        elif d_1 <= 2 or d_2 <= 2:
            return [1, max_moves]
        else:
            return [2, max_moves]
