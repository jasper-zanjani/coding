public class Block : Object
{
    /* Location of block */
    public int x;
    public int y;

    /* Color of block */
    public int color;

    public Block copy ()
    {
        var b = new Block ();
        b.x = x;
        b.y = y;
        b.color = color;
        return b;
    }
}
