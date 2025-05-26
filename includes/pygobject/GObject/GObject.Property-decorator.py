import gi
gi.require_version("GObject", "2.0")
from gi.repository import GObject

class Starship(GObject.Object):
    def __init__(self, name, registry, franchise):
        super().__init__()

        self._name = name
        self._registry = registry
        self._franchise = franchise

    @GObject.Property(type=str)
    def name(self) -> str:
        return self._name

    @GObject.Property(type=str)
    def registry(self) -> str:
        return self._registry

    @GObject.Property(type=int)
    def crew(self) -> int:
        return self._crew
