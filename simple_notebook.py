import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog

class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()

        self.testEdit = QTextEdit()
        self.testEdit.setPlaceholderText("please text...")
        self.testEdit.setPlainText("This is default text")
        self.testEdit.setStyleSheet("background-color: lightyellow; font-size: 16px;")
        self.setCentralWidget(self.testEdit)

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple Notepad')
        self.setGeometry(100, 100, 800, 600)

        menubar =self.menuBar()

        fileMenu = menubar.addMenu('File')

        newAction = QAction('New', self)
        newAction.triggered.connect(self.newFile)
        fileMenu.addAction(newAction)

        openAction = QAction('Open', self)
        openAction.triggered.connect(self.openFile)
        fileMenu.addAction(openAction)

        saveAction = QAction('Save', self)
        saveAction.triggered.connect(self.saveFile)
        fileMenu.addAction(saveAction)

    def newFile(self):
        self.testEdit.clear()
        self.testEdit.setPlainText("This is default text")
        print("New file clicked in terminal!")

    def openFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'r', encoding='utf-8') as file:
                self.testEdit.setText(file.read())

    def saveFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'w', encoding='utf-8') as file:
                file.write(self.testEdit.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    notepad = Notepad()
    notepad.show()
    sys.exit(app.exec_())
