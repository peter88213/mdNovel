"""Provide a class with mouse operation definitions for the Mac OS.

Copyright (c) 2024 Peter Triesberger
For further information see https://github.com/peter88213/mdnovel
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
from mdnvlib.view.platform.generic_mouse import GenericMouse


class MacMouse(GenericMouse):

    RIGHT_CLICK = '<Button-2>'
    TOGGLE_STATE = '<Command-Button-1>'
