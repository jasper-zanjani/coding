public class Class {
    public int pub_int = 10;
    private int priv_int;

    public Class() {
        this.priv_int = 20;
    }
}


public static int main(string[] args) {
    var object = new Class ();
    stdout.printf("pub_int: %d\n", object.pub_int);
    stdout.printf("priv_int: %d\n", object.priv_int);
    return 0;
}
