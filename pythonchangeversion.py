import os
import subprocess
import winreg as wrg 

"""
class PythonChangeVersion():
    def __init__(self) -> None:
        pass
    
    def get_versions_installed(self):
        getVersion =  subprocess.Popen("py --list", shell=True, stdout=subprocess.PIPE).stdout
        version =  getVersion.read()
        res = [i for i in range(len(version)) if version.startswith(b":", i)]
        versions = []
        for i in res:
            versions.append(float(version[i+1:i+5]))
        star = version.find(b"*")
        default = version[star-5:star-1]
        
        return versions, default
    def set_defaut(self, v:str):
        file_ini_path = "C:/Users/CODE/AppData/Local/py.ini"
        ini = open(file_ini_path,"r").read()
        python_pl = ini.find("python=")
        ini_rewrite = open(file_ini_path, "w")
        textr = ini[:python_pl]+v+ini[python_pl:]
        print(textr)
        os.system("set PY_PYTHON=" + v)
"""

class PyVersionManager():
    def __init__(self) -> None:
        pass
    
    @classmethod
    def get_versions(cls):
        getVersion =  subprocess.Popen("py --list", shell=True, stdout=subprocess.PIPE).stdout
        version =  getVersion.read()
        res = [i for i in range(len(version)) if version.startswith(b":", i)]
        versions = []
        for i in res:
            versions.append(float(version[i+1:i+5]))
        return versions, cls.get_default_v()
    
    @staticmethod
    def get_default_v():
        getVersion =  subprocess.Popen("where python", shell=True, stdout=subprocess.PIPE).stdout
        rawPath =  getVersion.read()
        path = str(rawPath)
        index1 = path.find("python.exe")
        path = path[:index1+10]
        indexPython = path.rfind("Python")
        path = path[indexPython:]
        index = path.find("\\")
        v = path[:index]
        return v
    @classmethod
    def get_v_and_paths(cls):
        versionsList = []
        pyListPath =  subprocess.Popen("py --list-paths", shell=True, stdout=subprocess.PIPE).stdout
        pyListPath =  pyListPath.read()
        pyListPath = str(pyListPath)
        i = 0
        for line in pyListPath.split("\\n"):
            decomposedPath = line.split("\\")
            versions = cls.get_versions()[0]
            if len(decomposedPath) > 2:
                
                versionsList.append([versions[i], "C:"+line.split("C:")[1][:-2]])
            i += 1
        return versionsList
    
    
    @classmethod
    def set_default_version(cls, version):
        getPath =  subprocess.Popen("echo %path%", shell=True, stdout=subprocess.PIPE).stdout # get whole paths
        rawPath =  getPath.read() # Read command
        path = rawPath.decode() # Convert bytes -> string
        versionsList = cls.get_v_and_paths() # Get versions and paths installed
        for i in versionsList:
            print("-->",i[0]) # print each version installed
        user = input("Version :") # Ask user to choose a version to set default
        for i in versionsList: # Loop that allow us to find which version user want 
            if str(i[0]) == str(user):
                pathChoose = i[1]
        pathSplit = pathChoose.split(r"\\\ "[:2])[:-1] # split the path by \\\
        pathV = ""
        for i in pathSplit: # loop to get formated path to user's choices version
            pathV = pathV+i+"\\" # 
        
        pathWithoutPv = []
        for i in path.split(";"):
            if i.find(pathV) == -1:
                pathWithoutPv.append(i)
        pathWithoutPv = ";".join(pathWithoutPv)
        path = pathV+";"+pathV+"Scripts;"+pathWithoutPv
        location = wrg.HKEY_CURRENT_USER 
        key = wrg.OpenKey(location, r"Environment", 0, wrg.KEY_ALL_ACCESS)
        wrg.SetValueEx(key, "Path", 0, wrg.REG_SZ, path) 

        
PyVersionManager.set_default_version(35)
        
    