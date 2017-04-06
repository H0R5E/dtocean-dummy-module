# -*- coding: utf-8 -*-
"""A demonstration vehicle for the dtocean project.

.. moduleauthor:: Mathew Topper <mathew.topper@tecnalia.com>
"""

from pkg_resources import get_distribution

from .main import Spreadsheet

# credentials
__version__ = get_distribution('dtocean-dummy-module').version
        
        