# -*- coding: UTF-8 -*-
import os
from sys import version_info
from multiprocessing import Manager, freeze_support
from project_demo.ProjectDemo import ProjectDemo

class VentiDemo:
    def __init__(self, osname, path, processes, venti_plock, venti_pevent, venti_pqueue, venti_pdict):
        self.osname = osname
        self.path = path
        self.processes = processes
        self.venti_plock = venti_plock
        self.venti_pevent = venti_pevent
        self.venti_pqueue = venti_pqueue
        self.venti_pdict = venti_pdict

    def project_demo(self):
        ProjectDemo(self.osname, self.path, self.processes, self.venti_plock, self.venti_pevent, self.venti_pqueue, self.venti_pdict).project()

    def main(self):
        self.project_demo()
        for ps in self.processes:
            ps.start()
        self.venti_pevent.wait()
        for pf in self.processes:
            pf.join()

if __name__ == "__main__":
    if version_info[:2] != (3, 12):
        print("not running on Python 3.12 version, this scenario has not been validated for feasibility")
    else:
        osname = os.name
        path = os.getcwd()
        processes = []
        if osname == "nt":
            freeze_support()
        with Manager() as manager:
            venti_plock = manager.Lock()
            venti_pevent = manager.Event()
            venti_pqueue = manager.Queue()
            venti_pdict = manager.dict()
            VentiDemo(osname, path, processes, venti_plock, venti_pevent, venti_pqueue, venti_pdict).main()
