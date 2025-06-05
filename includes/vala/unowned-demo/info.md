Appending a question mark to a type allows it to be [null.](https://docs.vala.dev/developer-guides/bindings/writing-a-vapi-manually/05-00-fundamentals-of-binding-a-c-function/05-03-nullability.html)

The `unowned` keyword creates a weak reference that does not increase the reference count of the target object.
This allows referenced objects to be destroyed.
