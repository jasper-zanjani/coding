??? info "books.xml"

    ```xml
    --8<-- "includes/books.xml"
    ```

The **etree** submodule contains the **ElementTree** object which can open a string filename to deserialize XML data using **`parse()`**, which returns an **ElementTree** object, representing an XML document.
A Python string can also be parsed with `fromstring()`, which actually returns an **Element** object.

=== "File"

    ```py
    tree = xml.etree.ElementTree.parse('books.xml')
    ```

=== "String"

    ```py
    tree = xml.etree.ElementTree.fromstring(books)
    ```



The `getroot()` method returns an Element object of the XML document's root node.
```py
root = tree.getroot()
```

The parsed data can be displayed using the `tostring()` static method, providing an Element as argument.
```py
ElementTree.tostring(root)
```


Children of an element can be filtered using `findall()`. This returns a list of Elements.
```py
books = root.findall('book')
```

Any Element object exposes an `attrib` property which returns a dictionary of attributes.
```
[b.attrib for b in books]
```

Attributes can be written to an Element using the `set()` method.
```py
root.set('foo','bar')
```

Attributes can also be manipulated on the attrib property with normal Python dictionary operations.

=== "Setting"

    ```py
    root.attrib['foo'] = 'bar'
    ```

=== "Deleting"

    ```py
    del(root.attrib['hello'])
    ```


Commit changes to disk. The argument can be a string representing the filename or a file object (in which case the file must be opened as a binary). Encoding can be specified (default is *UTF-8*) and a XML declaration can also be automatically generated.

=== "String"

    ```py
    tree.write('books.xml', encoding='UTF-16', xml_declaration=True)
    ```

=== "File object"

    ```py
    with open('books.xml', 'wb') as f:
        tree.write(f)
    ```

Find elements by element namescripts
```py
tree.findall('book')
```
