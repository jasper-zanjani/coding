public class Child : Object {
    public unowned Parent parent_ref; // Child has an unowned reference to Parent

    public Child(Parent parent) {
        this.parent_ref = parent;
        stdout.printf("Child created, referencing its parent.\n");
    }

    ~Child() {
        stdout.printf("Child destroyed.\n");
    }

    public void say_hi_to_parent() {
        // We need to be careful here. If parent_ref could be null or invalid,
        // we should check. For this barebones example, we assume it's valid
        // for the lifetime of this method call.
        stdout.printf("Child says: Hello to my parent!\n");
        // You could access parent_ref.some_public_member if needed
    }
}

