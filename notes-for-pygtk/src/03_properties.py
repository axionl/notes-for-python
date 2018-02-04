#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

window = Gtk.Window()

label = Gtk.Label()
label.set_label("OMG I think the new boston is awesome!")
label.set_angle(30)
label.set_halign(Gtk.Align.END)

window.add(label)

print(label.get_properties("label"))
print(label.get_properties("angle"))
print(label.get_properties("halign"))
window.connect("delete-event", Gtk.main_quit)
