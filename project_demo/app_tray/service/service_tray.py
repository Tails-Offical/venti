# -*- coding: UTF-8 -*-
from PIL import Image
from pystray import MenuItem, Icon
import os

class ServiceTray:
    def __init__(self, osname, path, venti_plock, venti_pevent, venti_pqueue, venti_pdict):
        self.osname = osname
        self.path = path
        self.venti_plock = venti_plock
        self.venti_pevent = venti_pevent
        self.venti_pqueue = venti_pqueue
        self.venti_pdict = venti_pdict
        self.switch = False

    def tray_switch(self, icon):
        self.switch = not self.switch
        icon.menu = self.tray_menu()
        icon.update_menu()

    def tray_quit(self, icon):
        self.venti_pevent.set()
        icon.stop()

    def tray_menu(self):
        return (
            MenuItem(
                f"{'Switch On' if self.switch else 'Switch Off'}",
                self.tray_switch
            ),
            MenuItem('Quit', self.tray_quit)
        )

    def service(self):
        if self.osname == "nt":
            image = Image.open(os.path.join(self.path, "data", "project_demo", "tray", "ico", "ico.png"))
            menu = self.tray_menu()
            icon = Icon("Venti", image, "Venti", menu)
            icon.run()
