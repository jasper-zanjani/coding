import gi
gi.require_version("GObject", "2.0")
from gi.repository import GObject

class Starship(GObject.Object):
    name = GObject.Property(type=str)
    registry = GObject.Property(type=str)
    crew = GObject.Property(type=int)

    def __init__(self, name, registry, crew):
        super().__init__()
        self.name=name
        self.registry=registry
        self.crew=crew
