import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import QTimer, Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.elapsed_ms = 0  # Total elapsed milliseconds
        self.timer = QTimer(self)
        self.timer.setInterval(10)  # 10 ms for centiseconds
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.setStyleSheet("""
            QPushButton, QLabel{
                padding: 20px;
                font-weight: bold;
                font-family: calibri;
            }
            QPushButton{
                font-size: 50px;
            }
            QLabel{
                font-size: 120px;
                background-color: hsl(200, 100%, 85%);
                border-radius: 20px;
            }
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.elapsed_ms = 0
        self.time_label.setText(self.format_time(self.elapsed_ms))

    def format_time(self, ms):
        hours = ms // (3600 * 1000)
        minutes = (ms // (60 * 1000)) % 60
        seconds = (ms // 1000) % 60
        centiseconds = (ms % 1000) // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{centiseconds:02}"

    def update_display(self):
        self.elapsed_ms += 10
        self.time_label.setText(self.format_time(self.elapsed_ms))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())

