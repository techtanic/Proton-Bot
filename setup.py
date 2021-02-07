import subprocess
import sys
from pack.vers import *

def install(name):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])

def main():

    my_packages = ['selenium', 'colorama', 'numpy', 'scipy']

    installed_pr = [] 
    
    for package in my_packages:
        install(package)
        print('\n')

    print('\nChrome')
    chrome_ver = get_chrome_version()

    if chrome_ver != None:
        is_chrome_there = True
        installed_pr.append('Chrome')
        setup_Chrome(chrome_ver)
    else:
        is_chrome_there = False
        print('Chrome isn\'t installed')
    
    if not is_chrome_there:
        print('Error - Setup installation failed \nReason - Please install either Chrome browser to complete setup process')
        exit()

    print('Setup Completed')
if __name__ == '__main__':
    main()