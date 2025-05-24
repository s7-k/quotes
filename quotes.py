import gi
import random
import json
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GLib
gi.require_version('Gtk', '3.0')

QUOTES_JSON_PATH = "/home/predator/Desktop/project_files/python/experimental_ground/projectFile.json" 

def load_quotes(quotes_json_path):
    with open(quotes_json_path) as f:
        return json.loads(f.read())

class QuoteDisplay(Gtk.Window):
    def __init__(self):
        super().__init__(title="Raven Labs -FocusAssist", name="toplevel")
        self.quote_label = Gtk.Label(name="main_content")
        self.quote_label.set_justify(Gtk.Justification.CENTER)
        self.quote_label.set_max_width_chars(50)
        self.quote_label.set_line_wrap(True)
        
        self.author_label = Gtk.Label(name="other_content")
        self.author_label.set_justify(Gtk.Justification.CENTER)
        self.author_label.set_max_width_chars(50)
        self.author_label.set_line_wrap(True)

        CSS = b"""
        #toplevel {
            background-color: rgba(2, 34, 93, 0.0);
        }
        #mybox {
            margin: 20px;    
        }
        #main_content {
            color: white;
            font-size: 20px;
            font-weight:bold;
        }
        #other_content {
            color: white;
            font-size: 14px;
            font-style: italic;
        }
        """

        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(CSS)

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        box = Gtk.Box(name="mybox", orientation=Gtk.Orientation.VERTICAL)
        box.set_homogeneous(False)
        box.pack_start(self.quote_label, False, False, 0)
        box.pack_start(self.author_label, False, False, 0)

        self.add(self.quote_label)
        self.add(self.author_label)

        self.add(box)
        
        self.timer_id = None
        self.update_quote()
    
    def update_quote(self):
        random_quote_idx = random.randint(0, len(quotes))

        quote_content = quotes[random_quote_idx]["Quote"]
        quote_author = quotes[random_quote_idx]["Author"]
        self.quote_label.set_text(quote_content + '\n')
        self.author_label.set_text(quote_author)

        self.timer_id = GLib.timeout_add_seconds(300, self.update_quote)

    def destroy(self):
        if self.timer_id:
            GLib.source_remove(self.timer_id)

quotes = load_quotes(QUOTES_JSON_PATH)
window = QuoteDisplay()
screen = window.get_screen()
width = screen.get_width()-100
height = screen.get_height()//20

hints = Gdk.Geometry()
hints.min_width = width 
hints.max_width = width
hints.min_height = 100
hints.max_height = 250

geom_mask = (
    Gdk.WindowHints.MIN_SIZE | Gdk.WindowHints.MAX_SIZE
)

visual = screen.get_rgba_visual()
window.set_visual(visual)
window.set_decorated(False)

# Set the window to always be on top
window.set_keep_above(False)
#window.set_default_size(width, height)
window.set_geometry_hints(window, hints, geom_mask)
window.move(40,40)
window.set_resizable(False)
window.connect("destroy", window.destroy)

window.show_all()
Gtk.main()