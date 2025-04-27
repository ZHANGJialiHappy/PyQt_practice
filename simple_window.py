import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox

def create_window():
    app =QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('PyQt Controls')
    window.setGeometry(100, 100, 800, 600)  # x, y, width, height

    layout = QVBoxLayout()

    label = QLabel('Hello, PyQt!')
    button = QPushButton('Click Me!')
    button.clicked.connect(lambda: on_button_click(window))

    layout.addWidget(label)
    layout.addWidget(button)

    window.setLayout(layout)

    window.show()
    sys.exit(app.exec_())

def on_button_click(parent_window):
    msg_box = QMessageBox(parent_window)
    msg_box.setText("Button clicked!")
    msg_box.setWindowTitle("Message")
    msg_box.setGeometry(
        parent_window.x() + (parent_window.width() - 200) // 2,
        parent_window.y() + (parent_window.height() - 100) // 2,
        200,
        100
    )
    msg_box.exec_()
    print("Button clicked in terminal!")

if __name__ == '__main__':
    create_window()