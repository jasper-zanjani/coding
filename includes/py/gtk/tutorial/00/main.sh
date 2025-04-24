# Install build dependencies
dnf install -y gcc gobject-instrospection-devel cairo-gobject-devel

# Build and install Pycairo
pip install pycairo

# Build and install PyGObject
pip install pygobject
