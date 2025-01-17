from PyQt5 import QtCore, QtGui, QtWidgets
from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter
import functions
from Ui_Roots import Ui_RootsWindow

equal = False


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(529, 577)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(10, 10, 501, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outputLabel.setFont(font)
        self.outputLabel.setStyleSheet("background-color: #FFF700")
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setLineWidth(1)
        self.outputLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clear_it('<<'))
        self.arrowButton.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clear_it('c'))
        self.clearButton.setGeometry(QtCore.QRect(100, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        self.indicesButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("^"))
        self.indicesButton.setGeometry(QtCore.QRect(190, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.indicesButton.setFont(font)
        self.indicesButton.setObjectName("indicesButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("/"))
        self.divideButton.setGeometry(QtCore.QRect(275, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("2"))
        self.eightButton.setGeometry(QtCore.QRect(100, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(275, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(190, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(100, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(275, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(190, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.twiButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("2"))
        self.twiButton.setGeometry(QtCore.QRect(100, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.twiButton.setFont(font)
        self.twiButton.setObjectName("twiButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.addButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("+"))
        self.addButton.setGeometry(QtCore.QRect(275, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(190, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(100, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        self.plusminusButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.plus_minus_it())
        self.plusminusButton.setGeometry(QtCore.QRect(10, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setObjectName("plusminusButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.equal_it())
        self.equalButton.setGeometry(QtCore.QRect(275, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("."))
        self.decimalButton.setGeometry(QtCore.QRect(190, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.decimalButton.setFont(font)
        self.decimalButton.setObjectName("decimalButton")
        self.sinButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.trig_it('sin'))
        self.sinButton.setGeometry(QtCore.QRect(360, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sinButton.setFont(font)
        self.sinButton.setObjectName("sinButton")
        self.cosButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.trig_it('cos'))
        self.cosButton.setGeometry(QtCore.QRect(440, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cosButton.setFont(font)
        self.cosButton.setObjectName("cosButton")
        self.tanButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.trig_it('tan'))
        self.tanButton.setGeometry(QtCore.QRect(360, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tanButton.setFont(font)
        self.tanButton.setObjectName("tanButton")
        self.asinButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.atrig_it('asin'))
        self.asinButton.setGeometry(QtCore.QRect(440, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.asinButton.setFont(font)
        self.asinButton.setObjectName("asinButton")
        self.acosButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.atrig_it('acos'))
        self.acosButton.setGeometry(QtCore.QRect(360, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.acosButton.setFont(font)
        self.acosButton.setObjectName("acosButton")
        self.atanButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.atrig_it('atan'))
        self.atanButton.setGeometry(QtCore.QRect(440, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.atanButton.setFont(font)
        self.atanButton.setObjectName("atanButton")
        self.eButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("2.718281"))
        self.eButton.setGeometry(QtCore.QRect(360, 380, 40, 75))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.eButton.setFont(font)
        self.eButton.setObjectName("eButton")
        self.piButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("3.1415926"))
        self.piButton.setGeometry(QtCore.QRect(395, 380, 40, 75))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.piButton.setFont(font)
        self.piButton.setObjectName("piButton")
        self.natlogButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.log_it('natlog'))
        self.natlogButton.setGeometry(QtCore.QRect(440, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.natlogButton.setFont(font)
        self.natlogButton.setObjectName("natlogButton")
        self.log10Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.log_it('log10'))
        self.log10Button.setGeometry(QtCore.QRect(360, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.log10Button.setFont(font)
        self.log10Button.setObjectName("log10Button")
        self.eqsolverButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.openRoots())
        self.eqsolverButton.setGeometry(QtCore.QRect(440, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.eqsolverButton.setFont(font)
        self.eqsolverButton.setObjectName("eqsolverButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def openRoots(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RootsWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)

        # Setting up buttons - Set up signal (how to pc knows it is clicked) and then slot (what it does)
        self.ui.line_btn.clicked.connect(self.showlinear)
        self.ui.quad_btn.clicked.connect(self.showquadratic)
        self.ui.cube_btn.clicked.connect(self.showcubic)

    def showlinear(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Linear)
        self.ui.lineSolve_btn.clicked.connect(self.rootsoutput)

    def showquadratic(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Quadratic)
        self.ui.quadsolve_btn.clicked.connect(self.rootsoutput)

    def showcubic(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Cubic)
        self.ui.cubesolve_btn.clicked.connect(self.rootsoutput)

    def rootsoutput(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Output)

    def trig_it(self, pressed):
        value = float(self.outputLabel.text())
        if pressed == 'sin':
            value = functions.sin(value)
            if value == -0.0:
                value = 0.0
            self.outputLabel.setText(f'{value}')
        elif pressed == 'cos':
            value = functions.cos(value)
            if value == -0.0:
                value = 0.0
            self.outputLabel.setText(f'{value}')
        elif pressed == 'tan':
            try:
                value = functions.tan(value)
                if value == -0.0:
                    value = 0.0
                self.outputLabel.setText(f'{value}')
            except ValueError:
                self.outputLabel.setText('Math Error')

    def atrig_it(self, pressed):
        value = float(self.outputLabel.text())
        try:
            if pressed == 'asin':
                value = functions.asin(value)
                self.outputLabel.setText(f'{value}')
            elif pressed == 'acos':
                value = functions.acos(value)
                self.outputLabel.setText(f'{value}')
            elif pressed == 'atan':
                value = functions.tan(value)
                self.outputLabel.setText(f'{value}')
        except ValueError:
            self.outputLabel.setText('Math Error')


    def log_it(self, pressed):
        value = float(self.outputLabel.text())
        try:
            if pressed == 'natlog':
                value = functions.natlog(value)
                self.outputLabel.setText(f'{value}')
            elif pressed == 'log10':
                value = functions.base10log(value)
                self.outputLabel.setText(f'{value}')
        except ValueError:
            self.outputLabel.setText('Math Error')

    def press_it(self, pressed):
        global equal
        while not equal:
            if self.outputLabel.text() == '0':
                self.outputLabel.setText('')
            # Concatenate whatever was pressed
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')
            break
        if equal:
            self.outputLabel.setText('0')
            equal = False

    def clear_it(self, pressed):
        if pressed == 'c':
            self.outputLabel.setText('0')
        elif pressed == '<<':
            text = self.outputLabel.text()
            self.outputLabel.setText(text[:-1])

    def plus_minus_it(self):
        screen = self.outputLabel.text()
        if '-' in screen:
            self.outputLabel.setText(screen.replace('-', ''))
        else:
            self.outputLabel.setText(f'-{screen}')

    def equal_it(self):
        global equal
        userinput = self.outputLabel.text()
        # Let user input stuff
        lexer = Lexer(userinput)
        tokens = lexer.generate_tokens()
        # print(list(tokens))
        parser = Parser(tokens)
        tree = parser.parse()
        # print(tree)
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        self.outputLabel.setText(f'{value}')
        equal = True

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scientific"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.clearButton.setText(_translate("MainWindow", "C"))
        self.indicesButton.setText(_translate("MainWindow", "^"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.multiplyButton.setText(_translate("MainWindow", "x"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.twiButton.setText(_translate("MainWindow", "2"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.addButton.setText(_translate("MainWindow", "+"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.plusminusButton.setText(_translate("MainWindow", "+/-"))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.decimalButton.setText(_translate("MainWindow", "."))
        self.sinButton.setText(_translate("MainWindow", "sin"))
        self.cosButton.setText(_translate("MainWindow", "cos"))
        self.tanButton.setText(_translate("MainWindow", "tan"))
        self.asinButton.setText(_translate("MainWindow", "asin"))
        self.acosButton.setText(_translate("MainWindow", "acos"))
        self.atanButton.setText(_translate("MainWindow", "atan"))
        self.eButton.setText(_translate("MainWindow", "e"))
        self.piButton.setText(_translate("MainWindow", "𝝅"))
        self.natlogButton.setText(_translate("MainWindow", "ln"))
        self.log10Button.setText(_translate("MainWindow", "Log10"))
        self.eqsolverButton.setText(_translate("MainWindow", "eq solver"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
