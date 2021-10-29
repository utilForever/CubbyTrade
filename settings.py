import locale
import os
import platform

# Set path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Set locale
if 'Linux' in platform.system() or 'Darwin' in platform.system():
    locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')
elif 'Windows' in platform.system():
    locale.setlocale(locale.LC_ALL, '')
