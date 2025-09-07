# -*- coding: UTF-8 -*-
from multiprocessing import Process
from project_demo.app_tray.service.service_tray import ServiceTray

class AppTray:
    @staticmethod
    def app(osname, path, processes, venti_plock, venti_pevent, venti_pqueue, venti_pdict):
        st = ServiceTray(osname, path, venti_plock, venti_pevent, venti_pqueue, venti_pdict)
        processes.append(Process(target=st.service))
