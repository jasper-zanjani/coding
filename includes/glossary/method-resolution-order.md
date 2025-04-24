**method resolution order** (MRO): the order of base classes that are searched when using `super()`
It is [accessed](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/) with `__mro__`, which returns a tuple of base classes in order of precedence, ending in `object` which is the root class of all classes.
