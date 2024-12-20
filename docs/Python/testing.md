# Testing

[Pytest](https://docs.pytest.org/en/stable/) is a popular **testing framework** preferred to [unittest](#unittest) by many Python developers because it follows Pythonic conventions more closely.
In contrast to unittest's custom methods, pytest relies on the builtin [`assert`](https://docs.python.org/3/reference/simple_stmts.html?highlight=assert#the-assert-statement) statement.

=== "pytest"

    ```py
    from phonebook import PhoneBook
    import pytest

    @pytest.fixture
    def phonebook():
        phonebook = PhoneBook()
        yield phonebook
        phonebook.clear()

    def test_lookup_by_name(phonebook):
        phonebook.add("Bob","1234")
        assert "1234" == phonebook.lookup("Bob")

    def test_phonebook_contains_all_names(phonebook):
        phonebook.add("Bob", "1234")
        assert "Bob" in phonebook.names()

    def test_missing_name_raises_error(phonebook):
        with pytest.raises(KeyError):
            phonebook.lookup("Bob")
    ```
    ```sh
    python -m pytest
    ```

=== "unittest"

    ```py
    import unittest

    from phonebook import PhoneBook


    class PhoneBookTest(unittest.TestCase):

        def test_lookup_by_name(self):
            self.phonebook.add("Bob", "12345")
            number = self.phonebook.lookup("Bob")
            self.assertEqual("12345", number)

        def test_missing_name(self):
            with self.assertRaises(KeyError):
                self.phonebook.lookup("missing")

        def test_empty_phonebook_is_consistent(self):
            self.assertTrue(self.phonebook.is_consistent())

        def setUp(self) -> None:
            self.phonebook = PhoneBook()

        def tearDown(self) -> None:
            self.phonebook.clear()
    ```
    ```sh
    python -m unittest
    ```

=== "Class under test"

    ```py
    import os

    class PhoneBook:
        def __init__(self, cache_directory = os.getcwd()):
            self.numbers = {}
            self.filename = os.path.join(cache_directory, "phonebook.txt")
            self.cache = open(self.filename, "w")

        def add(self, name, number):
            self.numbers[name] = number

        def lookup(self, name):
            return self.numbers[name]

        def is_consistent(self):
            return True

        def names(self):
            return set(self.numbers.keys())

        def clear(self):
            self.cache.close()
            os.remove(self.filename )
    ```

### Doctest

A **doctest** is a docstring containing what looks like interactive Python sessions. <sup>[Python Docs](https://docs.python.org/3/library/doctest.html "doctest - Test interactive Python examples")</sup>

```py
"""
Return the factorial of n, an exact integer >= 0.

>>> [factorial(n) for n in range(6)]
[1, 1, 2, 6, 24, 120]
>>> factorial(30)
265252859812191058636308480000000
>>> factorial(-1)
Traceback (most recent call last):
    ...
ValueError: n must be >= 0

Factorials of floats are OK, but the float must be an exact integer:
>>> factorial(30.1)
Traceback (most recent call last):
    ...
ValueError: n must be exact integer
>>> factorial(30.0)
265252859812191058636308480000000

It must also not be ridiculously large:
>>> factorial(1e100)
Traceback (most recent call last):
    ...
OverflowError: n too large
"""
```

This can then be run 

```py
if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

### pytest

**PyTest** relies on the built-in `assert` statement.

#### Fixtures

The **`@pytest.fixture`** decorator facilitiates the creation of test fixtures.
The fixture function's name is used as argument to the test case, and the value returned can be used by the logic within. 
([src](https://app.pluralsight.com/course-player?clipId=6d87a3a0-2869-419b-ac1d-abbd9b076c98))

Any clean-up logic can be invoked in this fixture as well by replacing `return` with `yield`.
Pytest also provides its own **`tmpdir`** test fixture for temporary directories. ([src](https://app.pluralsight.com/course-player?clipId=8a53dec3-dabb-4b5a-9a6f-0bfb696db0da))

<div class="grid cards" markdown>

```py title="without fixture"
from phonebook import PhoneBook
import pytest

def test_lookup_by_name(phonebook):
    phonebook=PhoneBook()
    phonebook.add("Bob","1234")
    assert "1234" == phonebook.lookup("Bob")

def test_phonebook_contains_all_names(phonebook):
    phonebook = PhoneBook()
    phonebook.add("Bob", "1234")
    assert "Bob" in phonebook.names()

def test_missing_name_raises_error(phonebook):
    phonebook = PhoneBook()
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")
```

```py title="fixture"
from phonebook import PhoneBook
import pytest

@pytest.fixture
def phonebook():
    phonebook = PhoneBook()
    yield phonebook
    phonebook.clear()

def test_lookup_by_name(phonebook):
    phonebook.add("Bob","1234")
    assert "1234" == phonebook.lookup("Bob")

def test_phonebook_contains_all_names(phonebook):
    phonebook.add("Bob", "1234")
    assert "Bob" in phonebook.names()

def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")
```

</div>

=== "tmpdir"

    ```py
    from phonebook import PhoneBook
    import pytest

    @pytest.fixture
    def phonebook(tmpdir):
        phonebook = PhoneBook(tmpdir)
        return phonebook


    def test_lookup_by_name(phonebook):
        # phonebook = PhoneBook()
        phonebook.add("Bob","1234")
        assert "1234" == phonebook.lookup("Bob")

    def test_phonebook_contains_all_names(phonebook):
        # phonebook = PhoneBook()
        phonebook.add("Bob", "1234")
        assert "Bob" in phonebook.names()

    def test_missing_name_raises_error(phonebook):
        # phonebook = PhoneBook()
        with pytest.raises(KeyError):
            phonebook.lookup("Bob")
    ```

#### unittest

[**unittest**](https://docs.python.org/3.8/library/unittest.html) is a testing framework built into Python's Standard Library that was based on JUnit. 
unittest came out in 2001, when JUnit was being ported and adapted to many languages.
Collectively, these frameworks were referred to as the **xUnit family**.
unittest's method names do not follow Python conventions because it predates the PEP-8 naming standard.

unittest allows you to create test classes that inherit from **TestCase**.

**Assertions** are implemented in individual methods of the TestCase subclass through unittest methods like `assertEqual` and `assertRaises`, etc.
Notably, TestCase subclasses must **not** have an `__init__()` constructor method defined.

```py
def test_lookup_by_name(self):
    phonebook = PhoneBook()
    phonebook.add("Bob", "12345")
    number = phonebook.lookup("Bob")
    self.assertEqual("12345", number)
```

**assertRaises** must be placed in a context manager.
Here, the test case will run the code within the `with` block and check to make sure it raises the specified exception: `KeyError`: ([src](https://app.pluralsight.com/course-player?clipId=fa55af11-913d-4171-a2b0-db9f75f249e1))

```py
def test_missing_name(self):
    fleet = Fleet()
    with self.assertRaises(KeyError):
        fleet.lookup("bla")
```

Fixtures:

-   **setUp** is run before every test method, allowing a **test fixture** to be created to avoid repetitive code.

-   **tearDown** is called after every method, which allows these resources to be released, even if the test case raises an exception. However, if it is `setUp` that raises the exception, then neither the test case nor `tearDown` will run. ([src](https://app.pluralsight.com/course-player?clipId=efd71803-d18f-4860-baca-d94bf935765a), [src](https://app.pluralsight.com/course-player?clipId=efd71803-d18f-4860-baca-d94bf935765a))

=== "Before"

    ```py
    import unittest

    from phonebook import PhoneBook


    class PhoneBookTest(unittest.TestCase):






        def test_lookup_by_name(self):
            phonebook = PhoneBook()
            phonebook.add("Bob", "12345")
            number = phonebook.lookup("Bob")
            self.assertEqual("12345", number)

        def test_missing_name(self):
            phonebook = PhoneBook()
            with self.assertRaises(KeyError):
                phonebook.lookup("missing")

        @unittest.skip("WIP")
        def test_empty_phonebook_is_consistent(self):
            phonebook = PhoneBook()
            self.assertTrue(phonebook.is_consistent())
    ```

=== "After"

    ```py
    import unittest

    from phonebook import PhoneBook


    class PhoneBookTest(unittest.TestCase):
        def setUp(self) -> None:
            self.phonebook = PhoneBook()

        def tearDown(self) -> None:
            self.phonebook.clear()

        def test_lookup_by_name(self):
            # phonebook = PhoneBook()
            self.phonebook.add("Bob", "12345")
            number = self.phonebook.lookup("Bob")
            self.assertEqual("12345", number)

        def test_missing_name(self):
            # phonebook = PhoneBook()
            with self.assertRaises(KeyError):
                self.phonebook.lookup("missing")

        @unittest.skip("WIP")
        def test_empty_phonebook_is_consistent(self):
            # phonebook = PhoneBook()
            self.assertTrue(self.phonebook.is_consistent())


    ```

The **`@unittest.skip`** decorator will tell the test runner to skip the decorated test case ([src](https://app.pluralsight.com/course-player?clipId=efd71803-d18f-4860-baca-d94bf935765a))

```py
@unittest.skip("WIP")
def test_empty_phonebook_is_consistent(self):
    phonebook = PhoneBook()
    self.assertTrue(phonebook.is_consistent())
```

The **command line entry point** is made with a call to `unittest.main()`, which executes the tests.
([src](https://realpython.com/python-testing/#how-to-use-unittest-and-flask "Getting Started With Testing in Python"))

```py
import unittest

from my_sum import sum

class TestSum(unittest.TestCase):
  def test_list_int(self):
    """
    Test that it can sum a list of integers
    """
    data = [1, 2, 3]
    result = sum(data)
    self.assertEqual(result, 6)

if __name__ == '__main__':
  unittest.main()
```

#### Integration tests

By convention, tests are put in their own directory as sibling to the main module ( in order to be able to import it ).
Integration and unit tests should be organized separately.

```
.
├── project
│   └── __init__.py
└── tests
    ├── integration
    └── unit
```

Run all integration tests within specified directory.
```sh
python -m unittest discover -s tests/integration
```
