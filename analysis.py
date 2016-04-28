#!/usr/bin/env python
import sys 
import configparser
hqsconfig = configparser.RawConfigParser()
hqsconfig.read(str(sys.argv[1]) + '/.hqsrc')

dboutside = None
dbinside = None
pyenv = None
rq = None

class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def db_check():
    global dbinside
    global dboutside
    dbinsideval = None
    dboutsideval = None
    try:
        dbinside = hqsconfig.items('Extension-DB')
        dbinsideval = True
    except:
        dbinsideval = False
        pass
    try:
        dboutside = hqsconfig.items('Standalone-DB')
        dboutsideval = True
    except:
        pass
    if dbinsideval == dboutsideval:
        print(bcolors.FAIL + '[E] Can not have two DB Value !' + bcolors.ENDC)
        sys.exit()
    elif dbinsideval is False and dboutsideval is None:
        print(bcolors.WARNING + '[W] Dont have DB setting !' + bcolors.ENDC)


def require_check():
    global rq
    try:
        rq = hqsconfig.items('Require-Env')
    except:
        print(bcolors.FAIL + '[E] RequireSection NotFound !' + bcolors.ENDC)
        sys.exit()

def pyenv_check():
    global pyenv
    try:
        pyenv = hqsconfig.items('Python-Env')
    except:
        print(bcolors.FAIL + '[E] PythonSection NotFound !' + bcolors.ENDC)
        sys.exit()


if __name__ == '__main__':
    require_check()
    pyenv_check()
    db_check()
