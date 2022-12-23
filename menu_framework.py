# menu_framework.py
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction)

class BasicMenu(QMainWindow):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 600, 400) # 창 위치 지정
		self.setWindowTitle("안녕하세요") # 창 캡션
		self.createMenu()
		self.show() 

	def createMenu(self):
		exit_act = QAction("Exit", self)
		exit_act.setShortcut("Ctrl+Q")
		exit_act.triggered.connect(self.close)
		
		menu_bar = self.menuBar()
		menu_bar.setNativeMenuBar(False)

		file_menu = menu_bar.addMenu("File")
		file_menu.addAction(exit_act)

if __name__ ==  '__main__' :
	app = QApplication(sys.argv)		
	window = BasicMenu()
	sys.exit(app.exec_())