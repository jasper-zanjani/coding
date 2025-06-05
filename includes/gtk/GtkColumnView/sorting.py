sorter_model = Gtk.SortListModel.new(model=data_model, sorter=column_view.get_sorter())
selection = Gtk.SingleSelection.new(model=sorter_model)
column_view.set_model(model=selection)

col1_exp = Gtk.PropertyExpression.new(Starship, None, "name1")
col2_exp = Gtk.PropertyExpression.new(Starship, None, "registry")
col3_exp = Gtk.PropertyExpression.new(Starship, None, "franchise")

col1.set_sorter(Gtk.StringSorter.new(col1_exp))
col2.set_sorter(Gtk.StringSorter.new(col2_exp))
col3.set_sorter(Gtk.NumericSorter.new(col3_exp))
