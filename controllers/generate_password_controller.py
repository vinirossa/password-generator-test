#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Module Name

    Description...

"""

__author__ = "Vinícius Pereira"
__copyright__ = "Copyright 2021, Vinícius Pereira"
__credits__ = ["Vinícius Pereira","etc."]
__date__ = "2021/04/12"
__license__ = "GPL"
__version__ = "1.0.0"
__pythonversion__ = "3.9.1"
__maintainer__ = "Vinícius Pereira"
__contact__ = "viniciuspsb@gmail.com"
__status__ = "Development"

import sys, os; sys.path.insert(0,os.getcwd())
import inspect as ins
import pyperclip
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
import models.passwordgenerator as pwdgen
import models.toolscontext.validator as validator
from models.toolscontext.fileconverter import ui_to_py
ui_to_py(VIEWFILE,os.path.abspath(VIEWPATH),os.path.abspath(VIEWPATH)) #Creates/updates the UI file.
from views.generate_password_view import Ui_FrmGenerator


VIEWFILE = "generate_password_view"
VIEWPATH = "views"


class FrmGenerator(qtw.QWidget):
    """
    classdocs
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor
        """
        super().__init__(*args, **kwargs)

        self.ui = Ui_FrmGenerator()
        self.ui.setupUi(self)

        ## Instanciação de objetos
        self.generator = pwdgen.PasswordGenerator()

        ## Declaração de variáveis
        self.keywords_list = []

        ## Definição de ícones
        self.setWindowIcon(qtg.QIcon(os.path.abspath('assets/lock-48.ico')))
        self.ui.btnAddKeyword.setIcon(qtg.QIcon(os.path.abspath('assets/plus2-48.png')))
        self.ui.btnCopyPassword.setIcon(qtg.QIcon(os.path.abspath('assets/copy-24.png'))) 

        ## Ui Properties Setup
        self.ui.txtKeyword.setFocus()

        ## Event Handling
        self.ui.btnAddKeyword.clicked.connect(self.add_keyword)
        self.ui.btnResetList.clicked.connect(self.reset_list)
        self.ui.btnGeneratePassword.clicked.connect(self.generate_password)
        self.ui.btnCopyPassword.clicked.connect(self.copy_password)

    def add_keyword(self):
        formatted_text = validator.format_string(self.ui.txtKeyword.text(),qt_window=self)
        if formatted_text:
            self.keywords_list.append(formatted_text)
            self.refresh_list()
            self.ui.txtKeyword.clear()
            self.ui.txtKeyword.setFocus()
    
    def refresh_list(self):
        self.ui.lswKeywords.clear()
        self.ui.lswKeywords.addItems(self.keywords_list)

    def reset_list(self):
        self.ui.lswKeywords.clear()
        self.keywords_list.clear()
        self.ui.txtKeyword.setFocus()

    def generate_password(self):
        password = self.generator.generate_password(self.keywords_list)
        self.ui.txtGeneratedPassword.setText(password)
        self.ui.lblLength.setText(str(len(password)).zfill(5))

    def copy_password(self):
        if self.ui.txtGeneratedPassword.text():
            pyperclip.copy(self.ui.txtGeneratedPassword.text())
            qtw.QToolTip.showText(qtg.QCursor.pos(), "Senha copiada!", self)

    def closeEvent(self, event):
        try:       
            self.setWindowState(qtc.Qt.WindowActive)
            questionbox = qtw.QMessageBox.question(self, "Sair", "Deseja sair do programa?",
                        qtw.QMessageBox.Yes  | qtw.QMessageBox.No, qtw.QMessageBox.No)

            if questionbox == qtw.QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
                
        except BaseException as e:
            msgBox = qtw.QMessageBox()
            msgBox.setIcon(msgBox.Critical)
            msgBox.setWindowTitle("Execution Error")
            msgBox.setText("{}: {}\n\nSource: {} (Line {})".format(e.__class__.__name__,
                           e.__doc__,os.path.basename(__file__),ins.currentframe().f_lineno-6))
            msgBox.exec_()           


    def keyPressEvent(self, event):
        try:
            if event.key() == qtc.Qt.Key_Escape:
                self.close()  
            if event.key() == qtc.Qt.Key_Return or event.key() == qtc.Qt.Key_Enter:
                self.add_keyword()

        except BaseException as e:
            msgBox = qtw.QMessageBox()
            msgBox.setIcon(msgBox.Critical)
            msgBox.setWindowTitle("Execution Error")
            msgBox.setText("{}: {}\n\nSource: {} (Line {})".format(e.__class__.__name__,
                           e.__doc__,os.path.basename(__file__),ins.currentframe().f_lineno-6))
            msgBox.exec_()


# if __name__ == "__main__":
app = qtw.QApplication([])

widget = FrmGenerator()
widget.show()

app.exec_()

if __name__ == "__main__":
    pass