# -*- coding: UTF-8 -*-
import argparse
import os
import subprocess

class Vmanage:
    def __init__(self):
        self.vpath = os.getcwd()
        self.vsys = os.name

    def _lpath(self):
        if self.vsys == "nt":
            return {"file_path":os.path.join(self.vpath,".venv","Scripts"),
                    "pyinstaller":os.path.join(self.vpath,".venv","Scripts","pyinstaller.exe")}
        else:
            return {"file_path":os.path.join(self.vpath,".venv","bin"),
                    "pyinstaller":os.path.join(self.vpath,".venv","bin","pyinstaller")}

    def lib(self, args):
        if args.ph:
            python_pyth = args.ph
        else:
            python_pyth = 'python'
        file_path = self._lpath()["file_path"]
        subprocess.run([python_pyth,'-m','venv',os.path.join(self.vpath,'.venv')],check=True)
        subprocess.run([os.path.join(file_path,'python'),"-m","pip","install","--upgrade","pip"],check=True)
        subprocess.run([os.path.join(file_path,'pip'),"install","-r","requirements.txt"],check=True)

    def show(self, args):
        total_projects = 0
        total_apps = 0
        project_folders = [f for f in os.listdir(self.vpath) if f.startswith("project_") and os.path.isdir(os.path.join(self.vpath, f))]
        total_projects = len(project_folders)
        for project_folder in project_folders:
            project_path = os.path.join(self.vpath, project_folder)
            app_folders = [f for f in os.listdir(project_path) if f.startswith("app_") and os.path.isdir(os.path.join(project_path, f))]
            total_apps += len(app_folders)
        print("Program: {} ( project {} , app {} )".format(os.path.basename(self.vpath), total_projects, total_apps))
        for project_index, project_folder in enumerate(project_folders, start=1):
            print("  project {}: {}".format(project_index, project_folder.replace("project_", "")))
            project_path = os.path.join(self.vpath, project_folder)
            app_folders = [f for f in os.listdir(project_path) if f.startswith("app_") and os.path.isdir(os.path.join(project_path, f))]
            for app_index, app_folder in enumerate(app_folders, start=1):
                print("    app {}: {}".format(app_index, app_folder))

    def build(self, args):
        for i in args.project:
            target = i.capitalize()
            subprocess.run([self._lpath()["pyinstaller"],"--onefile","--name",f"Venti{target}",f"Venti{target}.py"],check=True)

    def listen(self):
        parser = argparse.ArgumentParser(description="vmanage")    
        subparsers = parser.add_subparsers(dest="command")  

        # lib
        parser_lib = subparsers.add_parser("lib")
        parser_lib.add_argument('-pp', '--pp', help='set python path')
        parser_lib.set_defaults(func=lambda args: self.lib(args))

        # show
        parser_show = subparsers.add_parser("show")
        parser_show.add_argument('-pj', '--pj', help='set project name')
        parser_show.set_defaults(func=lambda args: self.show(args))

        # build
        parser_build = subparsers.add_parser("build")
        parser_build.add_argument('project', nargs=argparse.REMAINDER)
        parser_build.set_defaults(func=lambda args: self.build(args))

        args = parser.parse_args()
        if hasattr(args, "func"):
            args.func(args)
        else:  
            parser.print_help()  

if __name__ == "__main__":
    Vmanage().listen()