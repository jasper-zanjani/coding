# Tutorial

## 0. Hello, World!

--8<-- "includes/vala/tutorial/00/info.md"

```vala
--8<-- "includes/vala/tutorial/00/main.vala"
```

## 1. Class constructor

--8<-- "includes/vala/tutorial/01/info.md"

```vala
--8<-- "includes/vala/tutorial/01/main.vala"
```

## 2. Class definition

--8<-- "includes/vala/oop/00/info.md"

```vala
--8<-- "includes/vala/oop/00/main.vala"
```

## 3. Instantiation and properties

--8<-- "includes/vala/oop/01/info.md"

```vala hl_lines="10"
--8<-- "includes/vala/oop/01/main.vala"
```

## 4. Private properties

--8<-- "includes/vala/oop/02/info.md"


```vala hl_lines="3 6 14"
--8<-- "includes/vala/oop/02/main.vala"
```

## 5. Getters and setters

Vala support C#-style [properties](https://docs.vala.dev/tutorials/programming-language/main/03-00-object-oriented-programming/03-05-properties.html) to hide implementation details while exposing public getters and setters.

```vala
--8<-- "includes/vala/oop/03/main.vala"
```

## 6. CCode

All properties of GObjets publish a signal called `notify`.
This can be disabled by **annotating** them with the `CCode` attribute:

```vala hl_lines="2"
public class MyObject : Object {
    [CCode(notify = false)]
    // notify signal is NOT emitted upon changes in the property
    public int without_notification { get; set; }
    // notify signal is emitted upon changes in the property
    public int with_notification { get; set; }
}
```

## 7. Unowned keyword

--8<-- "includes/vala/unowned-demo/info.md"

```vala title="main.vala"
--8<-- "includes/vala/unowned-demo/main.vala"
```


```vala hl_lines="2" title="parent.vala"
--8<-- "includes/vala/unowned-demo/parent.vala"
```


```vala hl_lines="2" title="child.vala"
--8<-- "includes/vala/unowned-demo/child.vala"
```

## 8. GTK boilerplate

```vala title="Basic GTK App"
--8<-- "includes/vala/tutorial/02/main.vala"
```
