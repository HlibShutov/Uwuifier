import platform
import subprocess

print('uwu')

try:
    import pynvim
except Exception:
    print("Pynvim is not installed, installing it now...")
    pip_command = 'pip' if platform.system() == "Windows" else 'pip3'
    subprocess.run([pip_command, 'install', 'pynvim'])

try:
    import uwuipy
except Exception:
    print("Uwuipy is not installed, installing it now...")
    pip_command = 'pip' if platform.system() == "Windows" else 'pip3'
    subprocess.run([pip_command, 'install', 'uwuipy'])
