public static int main(string[] args) {
    Parent? p = new Parent();
    p.create_child();
    p.greet_from_child();

    stdout.printf("Setting parent to null...\n");
    // When 'p' goes out of scope or is set to null,
    // the Parent object (and consequently the Child it owns)
    // will be garbage collected because there are no more strong references to Parent.
    // The Child's unowned reference to Parent does not keep the Parent alive.
    p = null;

    return 0;
}
