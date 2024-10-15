import winreg as wrg 
  
# Store location of HKEY_CURRENT_USER 
location = wrg.HKEY_CURRENT_USER 
  
# Store path in soft 
key = wrg.OpenKey(location, r"Environment", 0, wrg.KEY_ALL_ACCESS)
# Creating values in Geeks 
wrg.SetValueEx(key, "Path", 0, wrg.REG_SZ, 
               r"C:\Users\CODE\AppData\Local\Programs\Python\Python37\Scripts\;C:\Users\CODE\AppData\Local\Programs\Python\Python37\;C:\Python312\Scripts\;C:\Python312\;C:\Program Files\Common Files\Oracle\Java\javapath;C:\Program Files (x86)\Common Files\Oracle\Java\javapath;C:\windows\system32;C:\windows;C:\windows\System32\Wbem;C:\windows\System32\WindowsPowerShell\v1.0\;C:\windows\System32\OpenSSH\;C:\Program Files\dotnet\;C:\Program Files\nodejs\;C:\ProgramData\chocolatey\bin;C:\Users\CODE\AppData\Local\Programs\Python\Python39\;C:\Program Files\Calibre2\;C:\Users\CODE\AppData\Local\Programs\Python\Python312\Scripts\;C:\Users\CODE\AppData\Local\Programs\Python\Python312\;C:\Users\CODE\AppData\Local\Programs\Python\Python39\Scripts\;C:\Users\CODE\AppData\Local\Programs\Python\Python39\;C:\Users\CODE\.pyenv\pyenv-win\bin;C:\Users\CODE\.pyenv\pyenv-win\shims;C:\Users\CODE\AppData\Local\Microsoft\WindowsApps;C:\Users\CODE\AppData\Local\GitHubDesktop\bin;C:\Program Files\JetBrains\PyCharm Community Edition 2024.1.4\bin;C:\Users\CODE\AppData\Local\Programs\Microsoft VS Code\bin;") 

  
if key: 
    wrg.CloseKey(key) 