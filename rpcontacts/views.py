# -*- coding: utf-8 -*-
"""This module provides views to manage the contacts table."""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QAbstractItemView,QDialog,QDialogButtonBox,QFormLayout,QHBoxLayout,QLineEdit, QMainWindow,QMessageBox, QPushButton, QTableView, QVBoxLayout, QWidget,)
from .model import ContactsModel

class Window(QMainWindow):
    """Main Window"""
    def __init__(self,parent=None):
        """Initializer"""
        super(). __init__(parent)
        self.setWindowTitle("RP Contacts")
        self.resize(550, 250)
        self.centralWidget=QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.contactsModel = ContactsModel()
        self.setupUI()

    def setupUI(self):
        """ Set up the main window's GUI."""
        # Create a table view widget
        self.table = QTableView()
        self.table.setModel(self.contactsModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        #Create buttons
        self.addButton = QPushButton("Add...")
        self.deleteButton = QPushButton("Delete")
        self.clearAllButton = QPushButton("Clear All")
        #Lay out the GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

class AddDialog(QDialog):
    """ Add contact dialog."""
    def __init__(self, parent=None):
        """Initializer"""
        super(). __init__(parent=parent)
        self.setWindowTitle("Add Contact")
        self.layout=QVBoxLayout()
        self.setLayout(self.layout)
        self.data=None

        self.setupUI()

    def setupUI(self):
        