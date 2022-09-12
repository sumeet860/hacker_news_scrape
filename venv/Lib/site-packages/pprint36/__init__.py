#!/usr/bin/env python3
#
#  __init__.py
"""
Backport of pprint from Python 3.9 to Python 3.6-3.8
"""
#
#  Copyright © 2001-2020 Python Software Foundation. All rights reserved.
#  Copyright © 2000 BeOpen.com . All rights reserved.
#  Copyright © 1995-2000 Corporation for National Research Initiatives. All rights reserved.
#  Copyright © 1991-1995 Stichting Mathematisch Centrum. All rights reserved.
#
#  License: PSF License
#  See the LICENSE file for details.
#

import sys

if sys.version_info[:2] >= (3, 9):
	from pprint import *
else:
	from ._pprint import *

__author__: str = "Python Software Foundation"
__copyright__: str = "2001-2020 Python Software Foundation"
__license__: str = "PSF License"
__version__: str = "3.9.0.2"
__email__: str = "dominic@davis-foster.co.uk"

__all__ = ["pprint", "pformat", "isreadable", "isrecursive", "saferepr", "PrettyPrinter", "pp"]
