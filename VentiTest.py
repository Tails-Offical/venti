# -*- coding: UTF-8 -*-
# from PIL import Image
# import subprocess
# from pystray import MenuItem, Icon
import os
import multiprocessing
from project_test.ProjectTest import ProjectTest

class VentiMain(object):
    def __init__(self):
        # self.icon_path = os.path.join(os.getcwd(), "data", "test", "app", "app_tray", "ico", "ico.png")
        # self.log_path = os.path.join(os.getcwd(), "data", "test", "log", "test.log")
        self.stop_event = multiprocessing.Event()
        self.path = os.getcwd()

    # def tray_log(self, icon, item):
    #     subprocess.call(["notepad", self.log_path])

    # def tray_quit(self, icon, item):
    #     self.stop_event.set()
    #     icon.stop()

    # def app_tray(self):
    #     self.image = Image.open(self.icon_path)
    #     self.menu = (MenuItem("Log", self.tray_log), MenuItem("Quit", self.tray_quit))
    #     self.icon = Icon("Venti", self.image, "Venti", self.menu)
    #     self.icon.run()

    def app_web(self):
        ProjectTest().app_web(self.stop_event, self.path)

    def app_cron(self):
        ProjectTest().app_cron(self.stop_event, self.path)

    def main(self, stype):
        # p1 = multiprocessing.Process(target = self.app_tray)
        p2 = multiprocessing.Process(target = self.app_web)
        p3 = multiprocessing.Process(target = self.app_cron)
        # p1.start()
        p2.start()
        p3.start()
        self.stop_event.wait()
        # p1.join()
        p2.join()
        p3.join()

if __name__ == "__main__":
    stype = os.name
    if stype == "nt":
        multiprocessing.freeze_support()
    VentiMain().main(stype)