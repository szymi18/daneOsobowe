import re
import sys

from PyQt6.QtWidgets import QDialog, QApplication
from PyQt6 import QtWidgets

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.zapisz.clicked.connect(self.daneOsobowe)
        self.show()

    def daneOsobowe(self):
        imie = self.ui.imie.text()
        nazwisko = self.ui.nazwisko.text()
        telefon = self.ui.telefon.text()
        umowa = self.ui.umowa.isChecked()
        pesel = self.ui.pesel.text()


        if len(pesel) == 11:
            plik = "wynik.txt"
            with open(plik, "a") as plik:
                plik.write(f"Imie: {imie}\nNazwisko: {nazwisko}\nTelefon: {telefon}\nPESEL: {pesel}\nUmowa: {umowa}\n\n")
        else:
            QtWidgets.QMessageBox.warning(self, "Niepoprawny pesel", "popraw")
            return







if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())
