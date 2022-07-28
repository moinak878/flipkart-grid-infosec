import os
import zipfile
import subprocess
import sys

def download(package):
    subprocess.check_call([sys.executable, "-m", "pip", "download", package])

def unpack():
    for file in os.listdir(os.getcwd()):   # get the list of files
        if zipfile.is_zipfile(file): # if it is a zipfile, extract it
            with zipfile.ZipFile(file) as item: # treat the file as a zip
               item.extractall()
               item.close()
            os.remove(file)

dirname = 'tmp'
n = len(sys.argv)
if n==1:
    print("Please provide Pypi package to scan !")
else:
    try:
        os.mkdir(dirName)

    except FileExistsError:
        shutil.rmtree(dirName)
        os.mkdir(dirName)

    os.chdir(dirName)
    download(sys.argv[1])
    unpack()
    shutil.rmtree(dirName)