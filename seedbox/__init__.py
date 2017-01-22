__title__ = 'seedbox'
__version__ = '0.4'
__author__ = 'Anthony Fox'

import platform

if platform.system() == 'Windows':
    raise OSError("This is not compatible with windows.")

from .api import cli

