import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chemical Equipment Parameter Visualizer")
        self.setGeometry(100, 100, 500, 400)

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
        self.status_label.setWordWrap(True)
        layout.addWidget(self.status_label)

    def on_upload_click(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv)")
        
        if not file_path:
            return

        self.status_label.setText(f"Uploading {file_path}...")
        
        try:
            with open(file_path, 'rb') as f:
                response = requests.post(
                    'http://127.0.0.1:8000/api/upload-csv/',
                    files={'file': f}
                )
            
            if response.status_code == 200:
                data = response.json()
                
                # Format equipment counts
                counts_str = ""
                for equip, count in data['equipment_type_counts'].items():
                    counts_str += f"- {equip}: {count}\n"

                summary_text = (
                    f"Upload Successful!\n\n"
                    f"Total Rows: {data['total_rows']}\n\n"
                    f"Averages:\n"
                    f"- Flowrate: {data['average_metrics']['flowrate']}\n"
                    f"- Pressure: {data['average_metrics']['pressure']}\n"
                    f"- Temperature: {data['average_metrics']['temperature']}\n\n"
                    f"Equipment Distribution:\n"
                    f"{counts_str}"
                )
                self.status_label.setText(summary_text)
            else:
                self.status_label.setText(f"Error: {response.text}")
                
        except Exception as e:
            self.status_label.setText(f"Connection Error: {str(e)}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
