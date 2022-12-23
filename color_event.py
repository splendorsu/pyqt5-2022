# color_event.py
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel)
from PyQt5.QtCore import  Qt, pyqtSignal, QObject

class SendSignal(QObject):
	change_style = pyqtSignal(int)

class EmptyWindow(QMainWindow):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 400, 300)
		self.setWindowTitle("안녕하세요") # 창 캡션
		self.setupLabel()
		self.show()

	def setupLabel(self):
		self.index = 0
		self.direction = ""
		self.color_list = ["red", "orange", "yellow","green","blue","indigo","purple"]
		self.label= QLabel()
		self.label.setStyleSheet(f"background-color:{self.color_list[self.index]}")
		self.setCentralWidget(self.label)

		self.sig = SendSignal()
		self.sig.change_style.connect(self.changeBackground)
		# self.sig.change_style.emit() 

	def keyPressEvent(self, event): # 아무것도 안하는 함수
		if (event.key() == Qt.Key_Up ):
			self.direction = "up"
			self.sig.change_style.emit(10)
		elif (event.key() == Qt.Key_Down ):
			self.direction = "down"
			self.sig.change_style.emit(20)

	def changeBackground(self, num):
		print(num)
		if self.direction == "up" and self.index < len(self.color_list) - 1:
			self.index += 1
			self.label.setStyleSheet(f"background-color:{self.color_list[self.index]}")
		elif self.direction == "down" and self.index > 0 :
			self.index -= 1
			self.label.setStyleSheet(f"backgroung-color:{self.color_list[self.index]}")

# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv
	# print(sys.argv)
	window = EmptyWindow()
	sys.exit(app.exec_())