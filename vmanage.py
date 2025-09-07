# -*- coding: UTF-8 -*-
import argparse
import os

class VmanageExecute:
    def lib(self, args, vpath):
        if vsys == "nt":
            os.system('python -m venv {}'.format(os.path.join(vpath,'.venv')))
            os.system(os.path.join(vpath,".venv","Scripts","python.exe -m pip install --upgrade pip"))
            os.system(os.path.join(vpath,".venv","Scripts","pip3.exe") + " install -r requirements.txt")
        if vsys == "posix":
            os.system('python -m venv {}'.format(os.path.join(vpath,'.venv')))
            os.system(os.path.join(vpath,".venv","bin","python -m pip install --upgrade pip"))
            os.system(os.path.join(vpath,".venv","bin","pip3") + " install -r requirements.txt")

    def show(self, args, vpath):
        total_projects = 0
        total_apps = 0
        project_folders = [f for f in os.listdir(vpath) if f.startswith("project_") and os.path.isdir(os.path.join(vpath, f))]
        total_projects = len(project_folders)
        for project_folder in project_folders:
            project_path = os.path.join(vpath, project_folder)
            app_folders = [f for f in os.listdir(project_path) if f.startswith("app_") and os.path.isdir(os.path.join(project_path, f))]
            total_apps += len(app_folders)
        print("Program: {} ( project {} , app {} )".format(os.path.basename(vpath), total_projects, total_apps))
        for project_index, project_folder in enumerate(project_folders, start=1):
            print("  project {}: {}".format(project_index, project_folder.replace("project_", "")))
            project_path = os.path.join(vpath, project_folder)
            app_folders = [f for f in os.listdir(project_path) if f.startswith("app_") and os.path.isdir(os.path.join(project_path, f))]
            for app_index, app_folder in enumerate(app_folders, start=1):
                print("    app {}: {}".format(app_index, app_folder))

    def build(self, args, vpath, vsys):
        if len(args.project) == 1:
            target = args.project[0].capitalize()
            if vsys == "nt":
                os.system("{} --onefile --noconsole --name Venti{} Venti{}.py".format(os.path.join(vpath, ".venv", "Scripts", "pyinstaller.exe"),
                                                                                                    target,
                                                                                                    target))
            if vsys == "posix":
                os.system("{} --onefile --name Venti{} Venti{}.py".format(os.path.join(vpath, ".venv", "bin", "pyinstaller"),
                                                                                                    target,
                                                                                                    target))
        else:
            print("python vmanage.py build demo")

class Vmanage():
    def __init__(self, vpath, vsys):
        self.ve = VmanageExecute()
        self.vpath = vpath
        self.vsys = vsys

    def listen(self):
        parser = argparse.ArgumentParser(description="vmanage")    
        subparsers = parser.add_subparsers(dest="command")  

        # lib
        parser_lib = subparsers.add_parser("lib")
        parser_lib.set_defaults(func=lambda args: self.ve.lib(args, self.vpath))

        # show
        parser_show = subparsers.add_parser("show")
        parser_show.set_defaults(func=lambda args: self.ve.show(args, self.vpath))

        # build
        parser_build = subparsers.add_parser("build")
        parser_build.add_argument('project', nargs=argparse.REMAINDER)
        parser_build.set_defaults(func=lambda args: self.ve.build(args, self.vpath, self.vsys))

        args = parser.parse_args()
        if hasattr(args, "func"):
            args.func(args)
        else:  
            parser.print_help()  

if __name__ == "__main__":
    vpath = os.path.abspath(os.path.dirname(__file__))
    vsys = os.name
    Vmanage(vpath, vsys).listen()