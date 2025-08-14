# -*- coding: UTF-8 -*-
import os
import subprocess
from multiprocessing import Manager, Process, freeze_support
from PIL import Image
from pystray import MenuItem, Icon
from project_demo.ProjectDemo import ProjectDemo

class VentiMain:
    def __init__(self, venti_queue, venti_dict, venti_event, venti_lock, stype):
        self.path = os.getcwd()
        self.venti_queue = venti_queue
        self.venti_dict = venti_dict
        self.venti_event = venti_event
        self.venti_lock = venti_lock
        self.stype = stype

    def app_cron_log(self):
        subprocess.call(["notepad", os.path.join(self.path, "data", "project_demo", "log", "app_cron.log")])

    def app_web_log(self):
        subprocess.call(["notepad", os.path.join(self.path, "data", "project_demo", "log", "app_web.log")])

    def tray_quit(self, icon):
        self.venti_event.set()
        icon.stop()

    def tray(self):
        if self.stype == "nt":
            self.image = Image.open(os.path.join(self.path, "data", "project_demo", "tray", "ico", "ico.png"))
            self.menu = (MenuItem("app_cron_log", self.app_cron_log), MenuItem("app_web_log", self.app_web_log), MenuItem("Quit", self.tray_quit))
            self.icon = Icon("Venti", self.image, "Venti", self.menu)
            self.icon.run()

    def project_demo(self):
        ProjectDemo(self.venti_queue, self.venti_dict, self.venti_event, self.venti_lock, self.path, self.stype).project()

    def main(self):
        p_tray = Process(target = self.tray)
        p_tray.start()
        self.project_demo()
        self.venti_event.wait()
        p_tray.join()

if __name__ == "__main__":
    stype = os.name
    if stype == "nt":
        freeze_support()
    with Manager() as manager:
        venti_queue = manager.Queue()
        venti_dict = manager.dict()
        venti_event = manager.Event()
        venti_lock = manager.Lock()
        VentiMain(venti_queue, venti_dict, venti_event, venti_lock, stype).main()