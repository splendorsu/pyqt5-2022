# menu_framework2.py

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, 
	QStatusBar, QTextEdit, QToolBar, QDockWidget	)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt

class BasicMenu(QMainWindow):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 400, 500) # 가로 400 세로 500
		self.setWindowTitle("안녕하세요") # 창 캡션
		self.setCentralWidget(QTextEdit())
		
		self.createMenu()		
		self.createToolBar()
		self.createDockWidget()

		self.show() 
	
	def createWidgets(self):			
		self.text_field = QTextEdit()
		self.setCentralWidget(self.text_field)

	def createMenu(self):
		# 파일 메뉴
		self.exit_act = QAction(QIcon("images/exit.png"),"Exit", self)
		self.exit_act.setShortcut("Ctrl+Q")
		self.exit_act.triggered.connect(self.close)
		
		full_screen_act = QAction("Full Screen", self, checkable = True)
		full_screen_act.setStatusTip("전체 화면 전환")
		full_screen_act.triggered.connect(self.switchToFullScreen)

		menu_bar = self.menuBar()
		menu_bar.setNativeMenuBar(False)

		file_menu = menu_bar.addMenu("File")
		file_menu.addAction(self.exit_act)

		view_menu = menu_bar.addMenu("View")
		appearance_submenu = view_menu.addMenu("Appearance")
		appearance_submenu.addAction(full_screen_act)

		self.setStatusBar(QStatusBar(self))

	def switchToFullScreen(self, state):
		if state : 
			self.showFullScreen()
		else :
			self.showNormal()

	def createToolBar(self):
		tool_bar = QToolBar("Main Toolbar")
		tool_bar.setIconSize(QSize(16,16))
		self.addToolBar(tool_bar)

		tool_bar.addAction(self.exit_act)

	def createDockWidget(self):
		dock_widget = QDockWidget()
		dock_widget.setWindowTitle("My Dock")
		dock_widget.setAllowedAreas(Qt.AllDockWidgetAreas)

		dock_widget.setWidget(QTextEdit())

		self.addDockWidget(Qt.LeftDockWidgetArea, dock_widget)


	
if __name__ ==  '__main__' :
	app = QApplication(sys.argv)		
	window = BasicMenu()
	sys.exit(app.exec_())