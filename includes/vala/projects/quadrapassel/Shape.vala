public class Shape : Object
{
    /* Location of shape */
    public int x;
    public int y;

    /* Rotation angle */
    public int rotation;

    /* Piece type */
    public int type;

    /* Blocks that make up this shape */
    public List<Block> blocks = null;

    public Shape copy ()
    {
        var s = new Shape ();
        s.x = x;
        s.y = y;
        s.rotation = rotation;
        s.type = type;
        foreach (var b in blocks)
            s.blocks.append (b.copy ());
        return s;
    }
}
