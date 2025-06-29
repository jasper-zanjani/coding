Learning Rust has been exceptionally challenging for me, at least partly because the examples given
by teachers and books are very difficult. It seems that most people who take an interest in Rust 
already have familiarity with computer science topics that seem bizarre to me.

This is especially apparent in the Smart Pointers chapter of Klabnik (Chapter 15) where the section
on `Rc<T>` uses a scenario that assumes familiarity with "cons lists" from the Lisp programming lang-
uage. This is another unfortunate case of too many "dependencies" in the teaching material for a
technical topic. Klabnik also doesn't touch on Cells specifically but launches into `RefCell<T>`s and
uses the same cons list scenario he began in the beginning of the chapter. Unfortunately this is of 
very little use to anyone who is not familiar with that topic.

The Starships scenario provides a great case study on interior mutability. An immutable Starship
can be made partially mutable by changing a field to a `Cell<T>` type. This allows the crew complement
to be updated, which is a very intuitive and easy to understand application.


Cursive makes for an interesting use-case in learning closure semantics. This is especially true
when it comes to how some widgets do not implement the Nameable trait. This forces any retrieval
of the selection a user made to take place in a closure. Not only that, the `move` keyword must
be used because it must necessarily capture the environment of the current scope.

- Lifetime parameters and implementing std Traits was key in extending the Cursive Starships application.

