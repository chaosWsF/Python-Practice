"""
Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

    1. Players take turns placing characters into empty squares (" ").
    2. The first player A always places "X" characters, while the second player B always 
      places "O" characters.
    3. "X" and "O" characters are always placed into empty squares, never on filled ones.
    4. The game ends when there are 3 of the same (non-empty) character filling any row, 
      column, or diagonal.
    5. The game also ends if all squares are non-empty.
    6. No more moves can be played if the game is over.

Given an array moves where each element is another array of size 2 corresponding to the row 
and column of the grid where they mark their respective character in the order in which A and 
B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return 
"Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is 
initially empty and A will play first.

Example 1:

    Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
    Output: "A"
    Explanation: "A" wins, he always plays first.
    "X  "    "X  "    "X  "    "X  "    "X  "
    "   " -> "   " -> " X " -> " X " -> " X "
    "   "    "O  "    "O  "    "OO "    "OOX"

Example 2:

    Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
    Output: "B"
    Explanation: "B" wins.
    "X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
    "   " -> " O " -> " O " -> " O " -> "XO " -> "XO " 
    "   "    "   "    "   "    "   "    "   "    "O  "

Example 3:

    Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
    Output: "Draw"
    Explanation: The game ends in a draw since there are no moves to make.
    "XXO"
    "OOX"
    "XOX"

Example 4:

    Input: moves = [[0,0],[1,1]]
    Output: "Pending"
    Explanation: The game has not finished yet.
    "X  "
    " O "
    "   "

Constraints:
    1. 1 <= moves.length <= 9
    2. moves[i].length == 2
    3. 0 <= moves[i][j] <= 2
    4. There are no repeated elements on moves.
    5. moves follow the rules of tic tac toe.
"""


class Solution:
    def tictactoe(self, moves) -> str:    # 36ms
        grids = [None] * 9
        
        def checker(lst) -> bool:
            tmp = set(lst)
            return (None not in tmp) and (len(tmp) == 1)
        
        for i in range(len(moves)):
            x, y = moves[i]
            if i % 2 == 0:
                grids[3 * x + y] = 'X'
                player = 'A'
            else:
                grids[3 * x + y] = 'O'
                player = 'B'
            
            if (
                checker(grids[:3]) or checker(grids[3:6]) or checker(grids[6:]) or checker(grids[::3]) or 
                checker(grids[1::3]) or checker(grids[2::3]) or checker(grids[::4]) or checker(grids[2:7:2])
            ):
                return player
        
        return 'Draw' if i == 8 else 'Pending'
    
    def tictactoe2(self, moves) -> str:    # 28ms
        A = [0] * 8
        B = [0] * 8
        
        for i in range(len(moves)):
            x, y = moves[i]
            player = B if i % 2 else A
            player[x] += 1
            player[y+3] += 1
            if x == y:
                player[6] += 1
            if x == 2-y:
                player[7] += 1
            
        for i in range(8):
            if A[i] == 3:
                return 'A'
            if B[i] == 3:
                return 'B'
        
        return 'Draw' if len(moves) == 9 else 'Pending'
