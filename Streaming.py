import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtMultimedia import QCamera, QCameraInfo
from PyQt5.QtCore import Qt
from PyQt5.QtMultimediaWidgets import QCameraViewfinder


class Streaming(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.viewfinder = QCameraViewfinder(self)
        layout.addWidget(self.viewfinder)

        self.camera = QCamera(QCameraInfo.defaultCamera())
        self.camera.setViewfinder(self.viewfinder)
        self.camera.start()

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    LogIn_window = Streaming()
    # Set the dimensions (width, height)
    LogIn_window.setFixedSize(900, 700)  #
    LogIn_window.show()
    sys.exit(app.exec_())
