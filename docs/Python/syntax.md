# Syntax

<div class="grid cards" markdown>

-   #### [Enums](https://docs.python.org/3/library/enum.html)

    ---

    ```py
    from enum import Enum

    class Color(Enum):
        red = 'RED'
        blue = 'BLUE'
        green = 'GREEN'
    ```
    

-   #### Decorators

    ---

    > A **decorator** is any function that accepts a function and returns a function.

    Decorators are one of the main ways that Python implements **functional programming** principles.

    Functions are **first-class objects** and can be passed as parameters.

    ```py
    import logging

    def hello_wrapper(name, func):
      func(f'Hello {name}')

    hello_wrapper("world", func=print) # Hello world
    hello_wrapper("logs", func=logging.warning) # WARNING:root:Hello logs
    ```

    ```py
    with open('hello.txt', 'w') as f:
      hello_wrapper('everyone!', func=f.write)
    ```

    ```py
    import random

    def anagram(t):
      l = [c for c in t]
      random.shuffle(l)
      print("".join(l))

    hello_wrapper('Japushku', anagram) #  eHoulhluaskpJ
    ```


    The function has to be passed as a reference, actually calling it will cause the wrapper function to attempt to execute the value **returned** by the inner function.


    ```py
    hello_wrapper("world", func=print()) # Error
    ```


    ```py
    def outer():
        print('Hi from the outer function')
        def inner():
            print('Hello from the inner function')
        inner()
    ```

    We can use the **`__name__`** attribute to access a passed function's name.
    ```py
    def hello(func):
        print(f'Hello {func.__name__}')

    hello(outer) # Hello outer
    ```
    We can also return functions, which can then be invoked
    ```py
    def hello(func):
      print(f'Hello {func.__name__}')
      return func

    hello(outer)()  
    '''
    Hi from the outer function
    Hello from the inner function
    '''

    new_outer = hello(outer)
    new_outer is outer # True
    ```

    ```py
    def wrapper(func):
      print(f'Before {func.__name__}')
      func()
      print(f'After {func.__name__}')

    wrapper(outer)
    '''
    Before outer
    Hi from the outer function
    Hello from the inner function
    After outer
    '''
    ```

    The true decorator pattern appears here, where `wrapper` is called the **decorator** and `outer` has been **decorated**.

    ```py
    def wrapper(func):
      def _wrapper():
        print(f'Before {func.__name__}')
        func()
        print(f'After {func.__name__}')
      return _wrapper

    outer = wrapper(outer)
    ```

    But the usual syntax since Python 2.4 is to place the decorator on the line above the decorated function, preceded by `@`:

    ```py
    @wrapper
    def outer():
      print('Hi from the outer function')
      def inner():
        print('Hello from the inner function')
      inner()
    ```

    **\_wrapper** here does not accept any positional arguments, so wrapping functions that take arguments will produce a TypeError.

    ```py
    @wrapper
    def say_hello(name):
      print(f'Hello {name}!') # error
    ```

    The solution is to incorporate `*args, **kwargs` into the definition of the inner function, as well as the invocation of the function passed in.


    ```py
    def wrapper(func):
      def _wrapper(*args, **kwargs):
        print(f'Before {func.__name__}')
        func(*args, **kwargs)
        print(f'After {func.__name__}')
      return _wrapper
    ```


    Returned values are not captured yet:


    ```py
    def wrapper(func):
      def _wrapper(*args, **kwargs):
        print(f'Before {func.__name__}')
        value = func(*args, **kwargs)
        print(f'After {func.__name__}')
        return value
      return _wrapper
    ```
    Inspecting the decorated function's `__name__` attribute reveals that it is still named `_wrapper`
    ```py
    say_hello.__name__ # '_wrapper'
    ```

    This is also true for other attributes, including docstring. `functools.wraps` is a decorator factory to reassign attributes to the wrapped function. This is considered superior to the `functools.update_wrapper` function which is also available.

    ```py
    def wrapper(func):
      @functools.wraps(func)
      def _wrapper(*args, **kwargs):
        print(f'Before {func.__name__}')
        value = func(*args, **kwargs)
        print(f'After {func.__name__}')
        return value
      return _wrapper
    ```

    This forms an ideal starting template for the creation of custom decorators.


-   #### Classes

    ##### Properties

    In the [Python documentation](https://docs.python.org/3/library/functions.html#property), attributes accessed with accessor functions are called **managed attributes**, which makes the term equivalent to **properties** in C#.

    Three methods can be defined using the `@property` decorator

    ```python
    # Constructor
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
      return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            raise ValueError

    @price.deleter
    def price(self):
        del self._price
    ```


    The **`@classmethod`** decorator prevents the interpreter from passing in the instantiated object using `self`, rather the class itself is passed in as the `cls` argument. This means that the methods decorated as such must take not `self` as the first argument but `cls`

    ```py
    @classmethod
    def classmethod(cls):
      pass
    ```

    The **`@staticmethod`** decorator prevents the interpreter from passing any additional arguments whatsoever. The resulting method has no access to the object itself nor the class and functions like a procedurally defined function.

</div>
