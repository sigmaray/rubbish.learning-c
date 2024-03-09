# https://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html

import gi
import json
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

class EntryWindow(Gtk.Window):
    def add_entry(self, parsed_json, vbox):
        for item in parsed_json:
            hbox = Gtk.Box(spacing=6)
            vbox.pack_start(hbox, True, True, 0)
            
            if type(item).__name__ == 'str':
                value = parsed_json[item]
                # print("The key and value are ({}) = ({})".format(key, value))
                entry_key = Gtk.Entry()
                entry_key.set_editable(False)
                entry_key.set_text(item)
                hbox.pack_start(entry_key, True, True, 0)

                if type(value).__name__ == 'list' or type(value).__name__ == 'dict':
                    vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
                    # vbox.add(vbox2)
                    hbox.pack_start(vbox2, True, True, 0)
                    self.add_entry(value, vbox2)            
                else:
                    entry_val = Gtk.Entry()
                    entry_val.set_editable(False)
                    entry_val.set_text(str(value))
                    hbox.pack_start(entry_val, True, True, 0)
                    
            elif type(item).__name__ == 'dict':
                entry_key = Gtk.Entry()
                entry_key.set_editable(False)
                entry_key.set_text('-')
                hbox.pack_start(entry_key, True, True, 0)

                vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
                # vbox.add(vbox2)
                hbox.pack_start(vbox2, True, True, 0)
                self.add_entry(item, vbox2)

    def __init__(self):
        super().__init__(title="Entry Demo")
        self.set_size_request(200, 100)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        
        str = ""
        dir = os.path.dirname(os.path.realpath(__file__))
        with open(dir + '/in-json.json') as f:
        # with open(dir + '/arr.json') as f:
            str = f.read()
        parsed_json = json.loads(str)
        # for item in parsed_json:
        #     # type(v)
        #     # isinstance(key, dict)
        #     # if type(key).__name__ == 'str':
        #     # if isinstance(key, dict):
        #     self.add_entry(parsed_json, item, vbox)
        self.add_entry(parsed_json, vbox)


        # self.entry = Gtk.Entry()
        # self.entry.set_text("Hello World")
        # vbox.pack_start(self.entry, True, True, 0)

        # hbox = Gtk.Box(spacing=6)
        # vbox.pack_start(hbox, True, True, 0)

        # self.check_editable = Gtk.CheckButton(label="Editable")
        # self.check_editable.connect("toggled", self.on_editable_toggled)
        # self.check_editable.set_active(True)
        # hbox.pack_start(self.check_editable, True, True, 0)

        # self.check_visible = Gtk.CheckButton(label="Visible")
        # self.check_visible.connect("toggled", self.on_visible_toggled)
        # self.check_visible.set_active(True)
        # hbox.pack_start(self.check_visible, True, True, 0)

        # self.pulse = Gtk.CheckButton(label="Pulse")
        # self.pulse.connect("toggled", self.on_pulse_toggled)
        # self.pulse.set_active(False)
        # hbox.pack_start(self.pulse, True, True, 0)

        # self.icon = Gtk.CheckButton(label="Icon")
        # self.icon.connect("toggled", self.on_icon_toggled)
        # self.icon.set_active(False)
        # hbox.pack_start(self.icon, True, True, 0)

    # def on_editable_toggled(self, button):
    #     value = button.get_active()
    #     self.entry.set_editable(value)

    # def on_visible_toggled(self, button):
    #     value = button.get_active()
    #     self.entry.set_visibility(value)

    # def on_pulse_toggled(self, button):
    #     if button.get_active():
    #         self.entry.set_progress_pulse_step(0.2)
    #         # Call self.do_pulse every 100 ms
    #         self.timeout_id = GLib.timeout_add(100, self.do_pulse, None)
    #     else:
    #         # Don't call self.do_pulse anymore
    #         GLib.source_remove(self.timeout_id)
    #         self.timeout_id = None
    #         self.entry.set_progress_pulse_step(0)

    # def do_pulse(self, user_data):
    #     self.entry.progress_pulse()
    #     return True

    # def on_icon_toggled(self, button):
    #     if button.get_active():
    #         icon_name = "system-search-symbolic"
    #     else:
    #         icon_name = None
    #     self.entry.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, icon_name)


win = EntryWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
