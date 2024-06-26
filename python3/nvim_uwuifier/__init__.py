import platform
import subprocess

print('uwu')

try:
    import pynvim
except ImportError:
    print("Pynvim is not installed, installing it now...")
    pip_command = 'pip' if platform.system() == "Windows" else 'pip3'
    subprocess.run([pip_command, 'install', 'pynvim'])

try:
    import uwuipy
except ImportError:
    print("Uwuipy is not installed, installing it now...")
    pip_command = 'pip' if platform.system() == "Windows" else 'pip3'
    subprocess.run([pip_command, 'install', 'uwuipy'])
