# python gitClone.py url
import imp
import os
import sys
import validators
import shutil
from IP_Carve import ip_carve
from git import Repo




dirName='tempDir'

def listFiles():
	res = []
	for path in os.listdir(dirName):
		address = os.path.join(dirName, path)
		if os.path.isfile(address):
			res+=ip_carve(address)
	print(res)

def cloneRepo(git_url):
	Repo.clone_from(git_url, 'tempDir')
	listFiles()

def isValidUrl(_url):
	valid=validators.url(_url)
	if valid==True:
		cloneRepo(_url)
	else:
		print("Invalid url !")


n = len(sys.argv)
if n==1:
	print("Please provide url to clone !")
else:
	try:
		os.mkdir(dirName)
		print("Directory " , dirName ,  " Created ") 
		isValidUrl(sys.argv[1])
		shutil.rmtree(dirName)
	except FileExistsError:
		print("Directory " , dirName ,  " already exists")
		shutil.rmtree(dirName)
		os.mkdir(dirName)
		print("Directory " , dirName ,  " Created ") 
		isValidUrl(sys.argv[1])
		shutil.rmtree(dirName)


	
	
