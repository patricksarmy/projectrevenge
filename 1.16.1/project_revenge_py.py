import os
import random
prof = os.getenv("USERPROFILE")
os.system("echo Welcome to Project Revenge!")
os.system("echo Brought to you by Patrick's Army")
os.system("echo Version is 1.16.1")
try:
    username_file = open("{proff}\\Downloads\\ProjRev\\1.16.1\\username.txt".format(proff=prof),"r")
    username = username_file.read()
    if username == "":
        raise SyntaxError("Username is blank")
except:
    try:
        username_file.close()
    except:
        pass
    os.system("echo Username not found")
    username = input("Please enter the username you would like to use: ")
    username_file = open("{proff}\\Downloads\\ProjRev\\1.16.1\\username.txt".format(proff=prof),"w")
    username_file.write(username)
    username_file.close()
    
    
try:
    javapath_file = open("{proff}\\Downloads\\ProjRev\\1.16.1\\javapath.txt".format(proff=prof),"r")
    javapath = javapath_file.read()
    if username == "":
        raise SyntaxError("Java Path is blank")
except:
    try:
        javapath_file.close()
    except:
        pass
    os.system("echo Java path not found")
    javapath = input("Please enter your java path (refer to readme.md in the github): ")
    javapath_file = open("{proff}\\Downloads\\ProjRev\\1.16.1\\javapath.txt".format(proff=prof),"w")
    javapath_file.write(javapath)
    javapath_file.close()
    

os.system("echo Using stored username {}".format(username))
os.system("echo Opening Environment Folder")
os.system("cd %USERPROFILE%\\Downloads\\ProjRev\\1.16.1")
os.system("echo Running Java")


os.system("\"{jarpathf}\\java\" -XX:-UseAdaptiveSizePolicy -XX:-OmitStackTraceInFastThrow -Dfml.ignorePatchDiscrepancies=true -Dfml.ignoreInvalidMinecraftCertificates=true -Djava.library.path=%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\natives\\1.16.1 -Xmx4G -Xms2G -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Dlog4j.configurationFile=%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\log4j2_112-116.xml -cp %USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\com\\mojang\\patchy\\1.3.9\\patchy-1.3.9.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\oshi-project\\oshi-core\\1.1\\oshi-core-1.1.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\net\\java\\dev\\jna\\platform\\3.4.0\\platform-3.4.0.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\net\\java\\dev\\jna\\jna\\4.4.0\\jna-4.4.0.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\com\\mojang\\javabridge\\1.0.22\\javabridge-1.0.22.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\net\\sf\\jopt-simple\\jopt-simple\\5.0.3\\jopt-simple-5.0.3.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\io\\netty\\netty-all\\4.1.25.Final\\netty-all-4.1.25.Final.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\com\\ibm\\icu\\icu4j\\66.1\\icu4j-66.1.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\org\\apache\\commons\\commons-lang3\\3.5\\commons-lang3-3.5.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\com\\google\\guava\\guava\\21.0\\guava-21.0.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\commons-io\\commons-io\\2.5\\commons-io-2.5.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\commons-codec\\commons-codec\\1.10\\commons-codec-1.10.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\net\\java\\jinput\\jinput\\2.0.5\\jinput-2.0.5.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\net\\java\\jutils\\jutils\\1.0.0\\jutils-1.0.0.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\com\\mojang\\brigadier\\1.0.17\\brigadier-1.0.17.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\com\\mojang\\datafixerupper\\3.0.25\\datafixerupper-3.0.25.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\com\\google\\code\\gson\\gson\\2.8.0\\gson-2.8.0.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\com\\mojang\\authlib\\1.6.25\\authlib-1.6.25.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\org\\apache\\commons\\commons-compress\\1.8.1\\commons-compress-1.8.1.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\commons-logging\\commons-logging\\1.1.3\\commons-logging-1.1.3.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\org\\apache\\httpcomponents\\httpclient\\4.3.3\\httpclient-4.3.3.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\org\\apache\\httpcomponents\\httpcore\\4.3.2\\httpcore-4.3.2.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\org\\apache\\logging\\log4j\\log4j-api\\2.8.1\\log4j-api-2.8.1.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\org\\apache\\logging\\log4j\\log4j-core\\2.8.1\\log4j-core-2.8.1.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\org\\lwjgl\\lwjgl\\3.2.2\\lwjgl-3.2.2.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\org\\lwjgl\\lwjgl-jemalloc\\3.2.2\\lwjgl-jemalloc-3.2.2.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\org\\lwjgl\\lwjgl-openal\\3.2.2\\lwjgl-openal-3.2.2.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\it\\unimi\\dsi\\fastutil\\8.2.1\\fastutil-8.2.1.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\org\\lwjgl\\lwjgl-glfw\\3.2.2\\lwjgl-glfw-3.2.2.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\org\\lwjgl\\lwjgl-opengl\\3.2.2\\lwjgl-opengl-3.2.2.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\org\\lwjgl\\lwjgl-stb\\3.2.2\\lwjgl-stb-3.2.2.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\org\\lwjgl\\lwjgl-tinyfd\\3.2.2\\lwjgl-tinyfd-3.2.2.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\libraries\\com\\mojang\\text2speech\\1.11.3\\text2speech-1.11.3.jar;%USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\versions\\1.16.1\\1.16.1.jar net.minecraft.client.main.Main --username {usernamef} --version 1.16.1 --gameDir %USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\files_1.16.5 --assetsDir %USERPROFILE%\\Downloads\\ProjRev\\1.16.1\\minecraft\\assets --assetIndex 1.16 --uuid {uuidf} --accessToken {tokenf} --userType 0 --versionType ProjectRevenge".format(jarpathf=javapath,usernamef=username,uuidf=random.randint(1,1000),tokenf=random.randint(1,1000)))
