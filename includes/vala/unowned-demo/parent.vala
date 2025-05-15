public class Parent : Object {
    public Child? child; // Parent has a strong reference to Child

    public Parent() {
        stdout.printf("Parent created.\n");
    }

    public void create_child() {
        this.child = new Child(this); // Pass self (Parent) to Child
    }

    ~Parent() {
        stdout.printf("Parent destroyed.\n");
    }

    public void greet_from_child() {
        if (child != null) {
            child.say_hi_to_parent();
        } else {
            stdout.printf("Parent has no child.\n");
        }
    }
}
