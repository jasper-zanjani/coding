import gi, sys
gi.require_version('GdkPixbuf', '2.0')
from gi.repository import GdkPixbuf, GLib
from pathlib import Path

def load_image(path):
    loader = GdkPixbuf.PixbufLoader()
    with open(path, 'rb') as f:
        image = f.read()
    loader.write(image):
    loader.close()
    pixbuf = loader.get_pixbuf()
    return pixbuf

if __name__=='__main__':
    arg = sys.argv[-1]
    image_path = Path(arg).expanduser()
    if image_path.is_file():
        pixbuf = load_image(arg)
        print(f"Width: {pixbuf.get_width()}, Height: {pixbuf.get_height()}")
    else:
        print(f"File {arg} not found")


