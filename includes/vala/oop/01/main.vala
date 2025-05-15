public class Class {
    public int integer;

    public Class() {
        this.integer=20;
    }
}

public static int main(string[] args) {
    var object = new Class ();
    stdout.printf("integer value is %d\n", object.integer);
    return 0;
}
