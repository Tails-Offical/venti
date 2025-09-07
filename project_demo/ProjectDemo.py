# -*- coding: UTF-8 -*-
from project_demo.app_concurrent.AppConcurrent import AppConcurrent
from project_demo.app_parallel.AppParallel import AppParallel
from project_demo.app_web.AppWeb import AppWeb

class ProjectDemo:
    def __init__(self, osname, path, processes, venti_plock, venti_pevent, venti_pqueue, venti_pdict):
        self.osname = osname
        self.path = path
        self.processes = processes
        self.venti_plock = venti_plock
        self.venti_pevent = venti_pevent
        self.venti_pqueue = venti_pqueue
        self.venti_pdict = venti_pdict

    def app_concurrent(self):
        AppConcurrent.app(self.osname, self.path, self.processes, self.venti_plock, self.venti_pevent, self.venti_pqueue, self.venti_pdict)

    def app_parallel(self):
        AppParallel.app(self.osname, self.path, self.processes, self.venti_plock, self.venti_pevent, self.venti_pqueue, self.venti_pdict)

    def app_tray(self):
        if self.osname == 'nt':
            from project_demo.app_tray.AppTray import AppTray
            AppTray.app(self.osname, self.path, self.processes, self.venti_plock, self.venti_pevent, self.venti_pqueue, self.venti_pdict)

    def app_web(self):
        AppWeb.app(self.osname, self.path, self.processes, self.venti_plock, self.venti_pevent, self.venti_pqueue, self.venti_pdict)

    def project(self):
        self.app_concurrent()
        self.app_parallel()
        self.app_tray()
        self.app_web()
