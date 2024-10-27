"""Provide an abstract Plugin base class.

Copyright (c) 2024 Peter Triesberger
For further information see https://github.com/peter88213/mdnovel
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
from abc import ABC, abstractmethod


class PluginBase(ABC):
    """Abstract Plugin base class."""

    @abstractmethod
    def __init__(self, model, view, controller):
        """Install the plugin.
        
        Positional arguments:
            model -- reference to the main model instance of the application.
            view -- reference to the main view instance of the application.
            controller -- reference to the main controller instance of the application.
        """
        self._mdl = model
        self._ui = view
        self._ctrl = controller

    def disable_menu(self):
        """Disable menu entries when no project is open."""
        pass

    def enable_menu(self):
        """Enable menu entries when a project is open."""
        pass

    def on_close(self):
        """Actions to be performed when a project is closed."""
        pass

    def on_quit(self):
        """Actions to be performed when mdnovel is closed."""
        pass

