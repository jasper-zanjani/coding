A Chunk (1) is a custom abstract class that represents a property of a contact; Chunk subclasses correspond to vCard properties (i.e. name, email, phone).
It is central to the function of ContactSheet which creates a widget for each Chunk subclass (`create_widget_for_chunk()`).
{: .annotate }

1.  src/core/contacts-chunk.vala

For example, `ContactSheet.create_widget_for_emails()` runs a loop over item in `BinChunk.elements`.

