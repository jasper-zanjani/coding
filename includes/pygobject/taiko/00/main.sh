# Install build dependencies
dnf install -y gcc gobject-instrospection-devel cairo-gobject-devel python3-devel pkg-config gtk4

# Build and install Pycairo
pip install pycairo

# Build and install PyGObject
pip install pygobject
