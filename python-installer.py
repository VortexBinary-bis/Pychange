import os
from bs4 import BeautifulSoup as bs
import requests
import threading

class python_installer_class():
    MODES = ["amd64", "32bits", "arm64"]
    
    def __init__(self):
        pass
            
            
            
    def callback(url):
        os.system('Invoke-WebRequest -Uri “'+ url +'” -OutFile “Setup.exe”')
        os.system('Start-Process “' + 'Setup.exe' +'” -ArgumentList “/silent /install” -Wait ')
        
        
        
    def version_download(self, version):
        url, code = self.get_version_url(version)
        threading.Thread(target=self.msgCallBack, args=(url)).start()
        
        
        
    def get_url(self, version, a, ext="exe", mode="amd64"):
        if mode == "32bit":
            url = "https://www.python.org/ftp/python/" + version + "/python-" + version + a + ext
        
        if mode == "amd64" or "arm64":
            url = "https://www.python.org/ftp/python/" + version + "/python-" + version + a + mode + "." + ext
        return requests.get(url), url
        
        
        
    def get_version_url(self, version, mode="amd64"):
        code, url = self.get_url(version, "-", "exe", mode)
        if str(code).find("404") != -1:
            code, url = self.get_url(version, "-", "msi", mode)
            if str(code).find("404") != -1:
                code, url = self.get_url(version, ".", "msi", mode)
                if str(code).find("404") != -1:
                    code, url = self.get_url(version, ".", "exe", mode)

        return url, code
        
        
        
    def sort_version_list(self, list_versions):
        list_versions_view2 = []
        
        for version in list_versions:
            preset1 = version[:version.find(".")]
            preset2 = version[version.find(".")+1:]
            
            try :
                list_versions_view2.append(float(preset1 + preset2))
            except :
                pass
            
        sorted_list_versions = sorted(list_versions_view2)
        sorted_list_versions_final = []
        
        for v in sorted_list_versions:
            sorted_list_versions_final.append(str(v)[:1] + "." + str(v)[1:])
            
        return sorted_list_versions_final

    
    
    
    def get_list_version(self):
        url="https://www.python.org/downloads/windows/"
        response = requests.get(url)
        
        soup = bs(response.content, "html.parser")
        
        colum = soup.find_all("div", class_="column")
        stables_releases = colum[0]
        stables_releases = bs(str(stables_releases), "html.parser")
        li = stables_releases.find_all("li")
        
        list_version = []
        
        for li_balise in li:
            li_balise = bs(str(li_balise), "html.parser")
            
            try:
                a_balises = li_balise.find_all("a")
                
                for a_balise in a_balises:
                    preset_a_balise = str(a_balise)[str(a_balise).find(">"):]
                    
                    if preset_a_balise.find("Python") != -1:
                        version = preset_a_balise[preset_a_balise.find("Python")+7:preset_a_balise.find("-")-1]
                        list_version.append(version)
                        pass
            except:
                pass
        return list_version[:-16]
        
        
        
