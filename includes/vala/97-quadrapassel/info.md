Quadrapassel relies on three classes mainly:

-   Block (1) a square that makes up a tetromino
    {: .annotate }

    1.  

        ```vala
        --8<-- "includes/vala/97-quadrapassel/Block.vala"
        ```

-   Shape (1), represents a tetromino
    {: .annotate }

    1.  

        ```vala
        --8<-- "includes/vala/97-quadrapassel/Shape.vala"
        ```

-   [Game](#game) manages the game board, the falling Shape, scoring, etc.

---

## Game

--8<-- "includes/vala/97-quadrapassel/Game.md"
