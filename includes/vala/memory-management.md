Vala's memory management system does not rely on garbage collection but on reference counting.
This also includes most objects of GObject-based libraries.

However, Vala allows you to use classes that have no support for reference counting.
Non reference-counted objects may have only one strong reference ("owning").
All other references must be **unowned** references.

!!! info "Destructor"
    
