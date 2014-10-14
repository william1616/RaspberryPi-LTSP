#!/usr/bin/python
from sys import argv, exit
from csv import reader
from os.path import exists, isfile
import subprocess

if len(argv) < 2:
  exit(1)

csvPath = argv[1]

if exists(csvPath) and isfile(csvPath):
  with open(csvPath) as csvFile:
    csvObj = reader(csvFile)
    for userList in csvObj:
      #userList[0] = username, userList[1] = passwd, userList[2] = secondaryGroup
      try:
        subprocess.Popen(["sudo", "useradd", "-m", "-s", "/bin/bash", "-p" , str(userList[1]), str(userList[0])])
        if userList[2]:
          subprocess.Popen(["sudo", "usermod", "-a", "-G", str(userList[2]), str(userList[1])])
      except Exception, e:
        print e
