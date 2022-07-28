#!/usr/bin/env python3

import os


test = """
Welcome to REpo SCanner
Please select an option

1. Git Repository
2. Pypi Package
3. npm Package
"""

while(True):
	print(test)
	option = input(">")
	if option=="1":
		print("Github")
	elif option=="2":
		print("Pypi")
	elif option=="3":
		print("npm")
	else:
		print("Are you crazy")

