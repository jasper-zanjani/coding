import gi
gi.require_version("GObject", "2.0")
from gi.repository import GObject, Gio

class Starship(GObject.Object):
    def __init__(self, name, registry, crew):
        super().__init__()

        self._name = name
        self._registry = registry
        self._crew = crew

    @GObject.Property(type=str)
    def name(self) -> str:
        return self._name

    @GObject.Property(type=str)
    def registry(self) -> str:
        return self._registry

    @GObject.Property(type=int)
    def crew(self) -> int:
        return self._crew

starships = {   "USS Enterprise": ("NCC-1701", 203),
                "USS Defiant": ("NX-74205", 50),
                "SSV Normandy": ("SR-1", 12),
                "USS Cerritos": ("NCC-75567", 200), }

list_store = Gio.ListStore(Starship)

for name, starship_info in starships.items():
    list_store.append(
        Starship(name=name, registry=starship_info[0], crew=starship_info[1])
    )

for i in list_store:
    print(i)
