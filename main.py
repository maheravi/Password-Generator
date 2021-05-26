# This Python file uses the following encoding: utf-8
import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader
import random


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()

        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.ui.generate.clicked.connect(self.Password)
        self.setWindowTitle("Remove Redundant Paragraph")

    def Password(self):
        passwords = []
        chars = 'abcdefghigklmnopqrstuvwxyz'
        sign = '#$@!%*+-'
        numbers = '0123456789'
        new = ""
        Choices = []
        if self.ui.pass1.isChecked():
            n = 9

        elif self.ui.pass2.isChecked():
            n = 12

        elif self.ui.pass3.isChecked():
            n = 20

        for i in range(0, n):
            choice = random.choice(['numbers', 'upperstrings', 'lowerstring', 'sign'])
            Choices.append(choice)
            if choice == 'numbers':
                passwords.append(str(random.choice(numbers)))
            elif choice == 'upperstrings':
                passwords.append(random.choice(chars).upper())
            elif choice == 'lowerstring':
                passwords.append(random.choice(chars))
            elif choice == 'sign':
                passwords.append(random.choice(sign))

        if not any(item == 'upperstrings' for item in Choices):
            passwords[random.randint(1, n)].remove()
            passwords.append(random.choice(chars).upper())
        if not any(item == 'numbers' for item in Choices):
            passwords[random.randint(n)].remove()
            passwords.append(random.choice(str(random.choice(numbers))))
        if not any(item == 'sign' for item in Choices):
            passwords[random.randint(n)].remove()
            passwords.append(random.choice(sign))

        for char in passwords:
            new += char
        self.ui.password.setText(str(new))


if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    # window.show()
    sys.exit(app.exec_())
