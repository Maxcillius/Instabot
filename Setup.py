import sys
import subprocess


packages = ['selenium', 'colorama']
def check_packages():
    for i in range(len(packages)):
        try:
             return __import__(packages[i])
        except ImportError:
             print('\nInstalling package', str(packages[i]))
             subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{packages[i]}'])

check_packages()