import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chemical Equipment Parameter Visualizer")
        self.setGeometry(100, 100, 400, 300)

        # Main layout container
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Upload Button
        self.upload_btn = QPushButton("Upload CSV")
        self.upload_btn.clicked.connect(self.on_upload_click)
        layout.addWidget(self.upload_btn)

        # Status Label
        self.status_label = QLabel("Waiting for upload...")
        layout.addWidget(self.status_label)

    def on_upload_click(self):
        self.status_label.setText("Upload Button Clicked!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
