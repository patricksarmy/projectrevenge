import os
import sys
import requests
import zipfile

def download_file(file_path,url):
    a = open(file_path,"w")
    a.close()
    a = open(file_path,"wb")
    a.write(requests.get(url, allow_redirects=True).content)
    a.close()
    print("Downloaded {}".format(url))


print("Welcome to Project Revenge!")
print("Brought to you by Patrick's Army")
print("The following file will download assets from minecraft.net and mojang.com")
print("While most of these files will download just fine on school computers, some are blocked")
print("This file is best run on a home computer")


os.system("echo Checking for ProjRev folder")
prof = (os.getenv("USERPROFILE"))

if not os.path.exists("{proff}\\Downloads\\ProjRev".format(proff=prof)):
    print("ProjRev directory not found. Creating one")
    os.mkdir("{proff}\\Downloads\\ProjRev".format(proff=prof))


try:
    print("Creating 1.16.1 folder")
    os.mkdir("{proff}\\Downloads\\ProjRev\\1.16.1".format(proff=prof))
except:
    print("ERROR!")
    print("A 1.16.1 installation is already detected.")
    sys.exit()


print("Creating minecraft folder")
os.mkdir("{proff}\\Downloads\\ProjRev\\1.16.1\\minecraft".format(proff=prof))

print("Downloading log4j because getting hacked is kinda cringe ngl")
download_file("{proff}\\Downloads\\ProjRev\\1.16.1\\minecraft\\log4j2_112-116.xml".format(proff=prof),"https://launcher.mojang.com/v1/objects/02937d122c86ce73319ef9975b58896fc1b491d1/log4j2_112-116.xml")

print("Creating client folder")
os.mkdir("{proff}\\Downloads\\ProjRev\\1.16.1\\minecraft\\versions".format(proff=prof))
os.mkdir("{proff}\\Downloads\\ProjRev\\1.16.1\\minecraft\\versions\\1.16.1".format(proff=prof))


client_list = requests.get("https://github.com/patricksarmy/projectrevenge/raw/main/1.16.1/client_1.16.1.txt", allow_redirects=True).content
client_list = str(client_list,"utf-8")
client_list = client_list.split("\n")

print("Downloading client files")
download_file("{proff}\\Downloads\\ProjRev\\1.16.1\\minecraft\\versions\\1.16.1\\1.16.1.jar".format(proff=prof),client_list[0])
download_file("{proff}\\Downloads\\ProjRev\\1.16.1\\minecraft\\versions\\1.16.1\\1.16.1.json".format(proff=prof),client_list[1])

print("Creating Assets Directory")
os.mkdir("{proff}\\Downloads\\ProjRev\\1.16.1\\minecraft\\assets".format(proff=prof))
os.mkdir("{proff}\\Downloads\\ProjRev\\1.16.1\\minecraft\\assets\\indexes".format(proff=prof))
os.mkdir("{proff}\\Downloads\\ProjRev\\1.16.1\\minecraft\\assets\\objects".format(proff=prof))
os.mkdir("{proff}\\Downloads\\ProjRev_temp".format(proff=prof))


print("Downloading Natives")
natives_list = requests.get("https://github.com/patricksarmy/projectrevenge/raw/main/1.16.1/natives_1.16.1.txt", allow_redirects=True).content
natives_list = str(natives_list,"utf-8")
natives_list = natives_list.split("\n")
for i in natives_list:
    if i == "":
        continue
    ogi = i
    ogi = ogi.rstrip("\n")
    i = i.split("/")
    i[len(i) - 1] = i[len(i) - 1].rstrip("\n")
    i = i[len(i) - 1]
    i = i.rstrip(".jar")
    i += ".zip"
    download_file("{proff}\\Downloads\\ProjRev_temp\\{file}".format(proff=prof,file=i),ogi)
    with zipfile.ZipFile("{proff}\\Downloads\\ProjRev_temp\\{file}".format(proff=prof,file=i), 'r') as zip_ref:
        zip_ref.extractall("{proff}\\Downloads\\ProjRev\\1.16.1\\minecraft\\natives\\1.16.1".format(proff=prof))
    os.remove("{proff}\\Downloads\\ProjRev_temp\\{file}".format(proff=prof,file=i))

os.rmdir("{proff}\\Downloads\\ProjRev_temp".format(proff=prof))


print("Downloading Assets")
assets_list = requests.get("https://github.com/patricksarmy/projectrevenge/raw/main/1.16.1/assets_1.16.1.txt", allow_redirects=True).content
assets_list = str(assets_list,"utf-8")
assets_list = assets_list.split("\n")
for i in assets_list:
    if i == "":
        continue
    if assets_list.index(i) == 0:
        download_file("{proff}\\Downloads\\ProjRev\\1.16.1\\minecraft\\assets\\indexes\\1.16.json".format(proff=prof),i)
    else:
        i = i.rstrip("\n")
        tempi = i.split("/")
        if not os.path.exists("{proff}\\Downloads\\ProjRev\\1.16.1\\minecraft\\assets\\objects\\{hexa}".format(proff=prof,hexa=tempi[3])):
            os.mkdir("{proff}\\Downloads\\ProjRev\\1.16.1\\minecraft\\assets\\objects\\{hexa}".format(proff=prof,hexa=tempi[3]))
        download_file("{proff}\\Downloads\\ProjRev\\1.16.1\\minecraft\\assets\\objects\\{hexa}\\{hexa2}".format(proff=prof,hexa=tempi[3],hexa2=tempi[4]),i)
os.mkdir("{proff}\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\".format(proff=prof))


print("Downloading Libraries")
libraries_list = requests.get("https://github.com/patricksarmy/projectrevenge/raw/main/1.16.1/libraries_1.16.1.txt", allow_redirects=True).content
libraries_list = str(libraries_list,"utf-8")
libraries_list = libraries_list.split("\n")
for i in libraries_list:
    if i == "":
        continue
    i = i.rstrip("\n")
    i2 = i.split("/")
    i2.remove("https:")
    i2.remove("")
    i2.remove("libraries.minecraft.net")
    filepath = "{proff}\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\".format(proff=prof)
    for j in i2:
        if j.endswith(".jar"):
            download_file("{filepathf}{jf}".format(filepathf=filepath,jf=j),i)
        else:
            if not os.path.exists("{filepathf}{jf}".format(filepathf=filepath,jf=j)):
                os.mkdir("{filepathf}{jf}".format(filepathf=filepath,jf=j))
            filepath += "{jf}\\".format(jf=j)

print("Creating Logs Directory")
os.mkdir("{proff}\\Downloads\\ProjRev\\1.16.1\\minecraft\\logs".format(proff=prof))

download_file("{proff}\\Downloads\\ProjRev\\1.16.1\\projectrevenge.py".format(proff=prof),"https://github.com/patricksarmy/project-revenge/raw/main/1.16.1/project_revenge_py.py")

print("Download Complete. Files are now ready for transfer.")
print("The easiest way to do this would be over a flash drive [or SD Card], but if you do not have either, Google Drive and Onedrive also work to transfer files.")
