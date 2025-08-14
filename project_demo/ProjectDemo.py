# -*- coding: UTF-8 -*-
from multiprocessing import Process
from project_demo.app_web.AppWeb import AppWeb
from project_demo.app_cron.AppCron import AppCron

class ProjectDemo:
    def __init__(self, venti_queue, venti_dict, venti_event, venti_lock, path, stype):
        self.venti_queue = venti_queue
        self.venti_dict = venti_dict
        self.venti_event = venti_event
        self.venti_lock = venti_lock
        self.path = path
        self.stype = stype

    def app_web(self):
        app_web = AppWeb(self.venti_queue, self.venti_dict, self.venti_event, self.venti_lock, self.path, self.stype)
        app_web.controller()

    def app_cron(self):
        app_cron = AppCron(self.venti_queue, self.venti_dict, self.venti_event, self.venti_lock, self.path, self.stype)
        app_cron.cron()

    def project(self):
        app_web = Process(target = self.app_web)
        app_cron = Process(target = self.app_cron)
        app_web.start()
        app_cron.start()
        self.venti_event.wait()
        app_web.join()
        app_cron.join()