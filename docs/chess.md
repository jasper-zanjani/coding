The first step is building the [**board representation**](https://www.chessprogramming.org/Board_Representation), which controls how it keeps track of the board and the rules of the game.

-   [Chess Engine in Python - Part 1 - Drawing the board](https://www.youtube.com/watch?v=EnYui0e73Rs)

The [Minimax algorithm](https://en.wikipedia.org/wiki/Minimax) is commonly used as the basis of chess engines.
The algorithm employs two agents, one the maximizer or current player and the minimizer or opponent, both of which make moves by turn for a determined number of moves, generating a game tree.
The positions in the tree are evaluated using a heuristic evaluation function which produces negative scores for positions favoring the minimizer and positive values for positions favoring the maximizer.

The evaluation function can use various metrics:

-   Piece values
-   Attacking squares

Alpha-beta pruning keeps the game tree size manageable by pruning actions that are not superior to already found moves.
