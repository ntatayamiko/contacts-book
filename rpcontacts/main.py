# -*- coding: utf-8 -*-
#rpcontacts/main.py
"""This module provides RO Contacts application."""

import sys
from PyQt5.QtWidgets import QApplication
from .database import createConnection
from .views import Window

def main():
    """RP Contacts main function"""
    app=QApplication(sys.argv)
    #conect to database before creating any window
    if not createConnection("contacts.sqlite"):
        sys.exit(1)
    #Create the main window
    win=Window()
    win.show()

    #Run the event loop
    sys.exit(app.exec())