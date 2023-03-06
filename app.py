import gui
import sys
import googletrans
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox


class Main(QtWidgets.QMainWindow, gui.Ui_Form):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.setupUi(self)
        self.textEdit.clear()
        self.add_languages()
        self.pushButton.clicked.connect(self.translate)
        self.pushButton_2.clicked.connect(self.clear)

    def add_languages(self):
        for x in googletrans.LANGUAGES.values():
            self.comboBox.addItem(x.capitalize())
            self.comboBox_2.addItem(x.capitalize())

    def translate(self):
        try:
            text_1 = self.textEdit.toPlainText()
            lang_1 = self.comboBox.currentText()
            lang_2 = self.comboBox_2.currentText()

            translator = googletrans.Translator()
            translate = translator.translate(text_1, src=lang_1, dest=lang_2)
            self.textEdit_2.setText(translate.text)
        except Exception as err:
            self.error_message(err)

    def error_message(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle('Error')
        msg.setText(str(text))
        msg.exec_()

    def clear(self):
        self.textEdit.clear()
        self.textEdit_2.clear()


if __name__ == "__main__":
    a = QtWidgets.QApplication(sys.argv)
    app = Main()
    app.show()
    a.exec_()
