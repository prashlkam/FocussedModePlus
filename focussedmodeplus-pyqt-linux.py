import sys
import pygame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow
from pygame.locals import *

class TransparentWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window to be transparent
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Set the window to be top-level and always on top
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        # Set the window to cover the entire screen
        self.setGeometry(0, 0, QApplication.desktop().screenGeometry().width(),
                         QApplication.desktop().screenGeometry().height())

        # Set a transparent background color
        palette = QPalette()
        palette.setColor(QPalette.Background, Qt.transparent)
        self.setPalette(palette)

        # Initialize Pygame
        pygame.init()
        # self.screen = pygame.display.set_mode((1, 1), SWSURFACE)
        # pygame.display.set_caption('Transparent Pygame Window')

        # Initialize rectangle
        self.rect_x, self.rect_y = 100, 100
        self.rect_width, self.rect_height = 200, 100
        self.hor_speed, self.vert_speed = 10, 10
    def closeEvent(self, event):
        pygame.quit()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.close()
        elif event.key() == Qt.Key_M:
            self.showMinimized()

    def paintEvent(self, event):
        painter = QPainter(self)
        # Draw a black background
        painter.setBrush(Qt.black)
        # painter.drawRect(0, 0, self.width(), self.height())
        painter.drawRect(0, 0, self.rect_x, self.rect_y) # top left
        painter.drawRect(self.rect_x, 0, self.rect_width, self.rect_y) # top center
        painter.drawRect(self.rect_x+self.rect_width, 0, self.width()-(self.rect_x+self.rect_width), self.rect_y) # top right
        painter.drawRect(0, self.rect_y, self.rect_x, self.rect_height) # center left
        painter.drawRect(self.rect_x+self.rect_width, self.rect_y, self.width()-(self.rect_x+self.rect_width), self.rect_height) # center right
        painter.drawRect(0, self.rect_y+self.rect_height, self.rect_x, self.height()-(self.rect_y+self.rect_height)) # bottom left
        painter.drawRect(self.rect_x, self.rect_y+self.rect_height, self.rect_width, self.height()-(self.rect_y+self.rect_height)) # bottom center
        painter.drawRect(self.rect_x+self.rect_width, self.rect_y+self.rect_height, self.width()-(self.rect_x+self.rect_width), self.height()-(self.rect_y+self.rect_height)) # bottom right

        # Draw a transparent rectangle
        painter.setBrush(Qt.transparent)
        painter.drawRect(self.rect_x, self.rect_y, self.rect_width, self.rect_height)

    def mouseMoveEvent(self, event):
        self.rect_x, self.rect_y = event.x(), event.y()
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TransparentWindow()
    window.showFullScreen()
    sys.exit(app.exec_())

