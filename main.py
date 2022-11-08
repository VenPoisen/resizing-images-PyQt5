import sys
from resizedesign import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class ResizeImage(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnChooseArchive.clicked.connect(self.open_image)
        self.btnResize.clicked.connect(self.resized)
        self.btnSave.clicked.connect(self.save)

    def open_image(self):
        image, _ = QFileDialog.getOpenFileName(
            self.centralwidget, 'Open Image', r'c:/Images'
        )
        self.inputOpenArchive.setText(image)
        self.original_img = QPixmap(image)
        self.labelImg.setPixmap(self.original_img)
        self.inputWidth.setText(str(self.original_img.width()))
        self.inputHeight.setText(str(self.original_img.height()))

    def resized(self):
        width = int(self.inputWidth.text())
        self.new_image = self.original_img.scaledToWidth(width)
        self.labelImg.setPixmap(self.new_image)
        self.inputWidth.setText(str(self.new_image.width()))
        self.inputHeight.setText(str(self.new_image.height()))

    def save(self):
        image, _ = QFileDialog.getSaveFileName(
            self.centralwidget, 'Save Image', r'C:/Users/Alan/Desktop'
        )
        self.new_image.save(f'{image}.png')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    resizeimage = ResizeImage()
    resizeimage.show()
    qt.exec_()
