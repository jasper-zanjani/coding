public Game (int lines = 20, int columns = 10, int starting_level = 1, int filled_lines = 0, int fill_prob = 5, bool pick_difficult_blocks = false)
{
    this.starting_level = starting_level;
    this.pick_difficult_blocks = pick_difficult_blocks;

    blocks = new Block[columns, lines];
    /* Start with some shape_landed-filled spaces */
    for (var y = 0; y < height; y++)
    {
        /* Pick at least one column to be empty */
        var blank = Random.int_range (0, width);

        for (var x = 0; x < width; x++)
        {
            if (y >= (height - filled_lines) && x != blank && Random.int_range (0, 10) < fill_prob)
            {
                blocks[x, y] = new Block ();
                blocks[x, y].x = x;
                blocks[x, y].y = y;
                blocks[x, y].color = Random.int_range (0, NCOLORS);
            }
            else
                blocks[x, y] = null;
        }
    }

    if (!pick_difficult_blocks)
        next_shape = pick_random_shape ();
}

