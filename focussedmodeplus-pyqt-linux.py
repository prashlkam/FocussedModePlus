import sys
import pygame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QPainter, QCursor
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
        self.ndone = True
        self.lx, self.ly = 100, 100
        self.rect_x, self.rect_y = 100, 100
        self.rect_width, self.rect_height = 200, 100
        self.hor_speed, self.vert_speed = 10, 10

        # main func code
        # pygamemouseMoveEvent(self)

    def closeEvent(self, event):
        pygame.quit()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.close()
        elif event.key() == Qt.Key_M:
            self.showMinimized()
        elif event.key() == Qt.Key_Left:
            if self.rect_x >= 0:
                self.rect_x -= self.hor_speed
            else:
                self.rect_x = 0
        elif event.key() == Qt.Key_Right:
            if self.rect_x <= self.width():
                self.rect_x += self.hor_speed
            else:
                self.rect_x = self.width()
        elif event.key() == Qt.Key_Up:
            if self.rect_y >= 0:
                self.rect_y -= self.vert_speed
            else:
                self.rect_y = 0
        elif event.key() == Qt.Key_Down:
            if self.rect_y <= self.height():
                self.rect_y += self.vert_speed
            else:
                self.rect_y = self.height()

        elif event.key() == Qt.Key_Minus:
            if self.rect_width > 0 + self.hor_speed:
                self.rect_width -= self.hor_speed
            else:
                self.rect_width = self.hor_speed
        elif event.key() == Qt.Key_Equal:
            if self.rect_width < self.width() - self.hor_speed:
                self.rect_width += self.hor_speed
            else:
                self.rect_width = self.width() - self.hor_speed
        elif event.key() == Qt.Key_Underscore:
            if self.hor_speed > 5:
                self.hor_speed -= 5
            else:
                self.hor_speed = 5 
        elif event.key() == Qt.Key_Plus:
            if self.hor_speed < self.width():
                self.hor_speed += 5
            else:
                self.hor_speed = self.width()

        elif event.key() == Qt.Key_Comma:
            if self.rect_height > 0 + self.vert_speed:
                self.rect_height -= self.vert_speed
            else:
                self.rect_height = self.vert_speed
        elif event.key() == Qt.Key_Period:
            if self.rect_height < self.height() - self.vert_speed:
                self.rect_height += self.vert_speed
            else:
                self.rect_height = self.height() - self.vert_speed
        elif event.key() == Qt.Key_Less:
            if self.vert_speed > 5:
                self.vert_speed -= 5
            else:
                self.vert_speed = 5
        elif event.key() == Qt.Key_Greater:
            if self.vert_speed < self.rect_height:
                self.vert_speed += 5
            else:
                self.vert_speed = self.rect_height
        self.update()        

    def paintEvent(self, event):
        painter = QPainter(self)
        # Draw a black background
        painter.setBrush(Qt.black)
        painter.setPen(Qt.black)
        # painter.drawRect(0, 0, self.width(), self.height()) # full screen rect - not used...
        painter.drawRect(0, 0, self.rect_x, self.rect_y) # top left
        painter.drawRect(self.rect_x, 0, self.rect_width, self.rect_y) # top center
        painter.drawRect(self.rect_x+self.rect_width, 0, self.width()-(self.rect_x+self.rect_width), self.rect_y) # top right
        painter.drawRect(0, self.rect_y, self.rect_x, self.rect_height) # center left
        painter.drawRect(self.rect_x+self.rect_width, self.rect_y, self.width()-(self.rect_x+self.rect_width), self.rect_height) # center right
        painter.drawRect(0, self.rect_y+self.rect_height, self.rect_x, self.height()-(self.rect_y+self.rect_height)) # bottom left
        painter.drawRect(self.rect_x, self.rect_y+self.rect_height, self.rect_width, self.height()-(self.rect_y+self.rect_height)) # bottom center
        painter.drawRect(self.rect_x+self.rect_width, self.rect_y+self.rect_height, self.width()-(self.rect_x+self.rect_width), self.height()-(self.rect_y+self.rect_height)) # bottom right

        # Draw a transparent rectangle
        painter.setPen(Qt.white)
        painter.setBrush(Qt.transparent)
        painter.drawRect(self.rect_x, self.rect_y, self.rect_width, self.rect_height)

    def mouseMoveEvent(self, event):
        #cursor = QCursor() 
        #if self.lx == self.rect_x and self.ly == self.rect_y:
        #    self.rect_x, self.rect_y = cursor.pos()
        self.rect_x, self.rect_y = event.x(), event.y()
        self.update()
        #self.lx, self.ly = cursor.pos()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TransparentWindow()
    window.showFullScreen()
    # window.pygamemouseMoveEvent() # not working
    sys.exit(app.exec_())

