**Enumeration**
:   
    In C# the term **enumeration** refers to the process of successively returning individual values. 
    In Python, the term **iteration** is used to refer to the same thing, and **iterable** refers to an object that can be iterated, or parsed out into sub-elements.

    - In Python, any object that exposes the `__iter__()` and `__next__()` **dunder** methods are iterable.
    - In C#, the `IEnumerable` interface implements enumeration.

    Both languages feature a keyword that allows a subclass to access its direct parent.
    Whereas in Python the terms **superclass** and **subclass** are used, in C# the terms **base class** and **derived class** are preferred.

**Garbage collector**
:   
    A garbage collector is a feature of some programming language runtimes that periodically pauses execution to remove data that is no longer used.
    Such languages are considered unsuitable for use in database applications because of the unpredictable latency this garbage collection creates, despite the added memory safety.

**Loop unswitching**
:   
    One of the core optimizations that a C compiler performs; transforms a loop containing a conditional into a conditional with a loop in both parts, which changes flow control


**Register rename engine**
:   
    Component of modern high-end cores which is one of the largest consumers of die area and power


**Scalar Replacement Of Aggregates (SROA)**{: #sroa }
:   
    One of the core optimizations that a [C](#c) compiler performs; attempts to replace `struct`s and arrays with fixed lengths with individual variables, which allows the compiler to treat accesses as independent and elide operations entirely if it can prove the results are never visible, which also deletes padding sometimes.

**Segmented architecture**
:   
    Pointers might be segment IDs and an offset
