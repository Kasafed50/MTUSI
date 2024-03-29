import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.vbox = QVBoxLayout(self)
        self.hbox_one = QHBoxLayout()
        self.hbox_two = QHBoxLayout()
        self.hbox_three = QHBoxLayout()
        self.hbox_for = QHBoxLayout()
        self.hbox_five = QHBoxLayout()
        self.hbox_six = QHBoxLayout()

        self.vbox.addLayout(self.hbox_one)
        self.vbox.addLayout(self.hbox_two)
        self.vbox.addLayout(self.hbox_three)
        self.vbox.addLayout(self.hbox_for)
        self.vbox.addLayout(self.hbox_five)
        self.vbox.addLayout(self.hbox_six)


        self.input = QLineEdit(self)
        self.hbox_one.addWidget(self.input)

        self.b_reset = QPushButton("Clear", self)
        self.hbox_one.addWidget(self.b_reset)

        class Match():
            self.b_plus = QPushButton("+", self)
            self.hbox_two.addWidget(self.b_plus)

            self.b_minus = QPushButton("-", self)
            self.hbox_two.addWidget(self.b_minus)

            self.b_multiplication = QPushButton("*", self)
            self.hbox_two.addWidget(self.b_multiplication)

            self.b_division = QPushButton("/", self)
            self.hbox_two.addWidget(self.b_division)

            self.b_point = QPushButton(",", self)
            self.hbox_two.addWidget(self.b_point)

            self.b_result = QPushButton("=", self)
            self.hbox_two.addWidget(self.b_result)

        class keyboard():
            self.b_1 = QPushButton("1", self)
            self.hbox_three.addWidget(self.b_1)

            self.b_2 = QPushButton("2", self)
            self.hbox_three.addWidget(self.b_2)

            self.b_3 = QPushButton("3", self)
            self.hbox_three.addWidget(self.b_3)

            self.b_4 = QPushButton("4", self)
            self.hbox_for.addWidget(self.b_4)

            self.b_5 = QPushButton("5", self)
            self.hbox_for.addWidget(self.b_5)

            self.b_6 = QPushButton("6", self)
            self.hbox_for.addWidget(self.b_6)

            self.b_7 = QPushButton("7", self)
            self.hbox_five.addWidget(self.b_7)

            self.b_8 = QPushButton("8", self)
            self.hbox_five.addWidget(self.b_8)

            self.b_9 = QPushButton("9", self)
            self.hbox_five.addWidget(self.b_9)

            self.b_zero = QPushButton("0", self)
            self.hbox_six.addWidget(self.b_zero)


        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_multiplication.clicked.connect(lambda: self._operation("*"))
        self.b_division.clicked.connect(lambda: self._operation("/"))
        self.b_point.clicked.connect(lambda: self._button(","))
        self.b_result.clicked.connect(self._result)
        self.b_reset.clicked.connect(self._reset)

        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_9.clicked.connect(lambda: self._button("0"))

    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)

    def _operation(self, op):
        if self.input.text():
            try:
                self.num_1 = int(self.input.text())
            except Exception:
                self.input.setText("Error")
                self.num_1 = 1
            self.op = op
            self.input.setText("")



    def _reset(self):
        self.input.setText("")
        self.num_1 = 1

    def _result(self):
        if self.input.text():
            try:
                self.num_2 = int(self.input.text())
            except Exception:
                self.input.setText("")
                self.num_2 = 1
            if self.op == "+":
                self.input.setText(str(self.num_1 + self.num_2))
            elif self.op == "-":
                self.input.setText(str(self.num_1 - self.num_2))
            elif self.op == "*":
                self.input.setText(str(self.num_1 * self.num_2))
            elif self.op == "/":
                if self.num_2 != 0:
                    self.input.setText(str(self.num_1 / self.num_2))
                else:
                    self.input.setText("Error")


app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())
