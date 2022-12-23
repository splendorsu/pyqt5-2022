# photo_editor.py

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, 
	QStatusBar, QTextEdit, QToolBar, QDockWidget	,
	QWidget, QLabel, QFileDialog, QMessageBox, QPushButton,
	QDesktopWidget, QSizePolicy, QVBoxLayout)
from PyQt5.QtGui import QIcon, QPixmap, QTransform, QPainter
from PyQt5.QtCore import QSize, Qt, QRect
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog


class PhotoEditor(QMainWindow):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		# self.setFixedSize(650, 650) 
		self.setGeometry(10,10, 650, 650) 
		self.setWindowTitle("Photo Editor") # 창 캡션
		
		self.centerMainWindow() # Main 이 되는 화면
		self.createToolsDockWidget() # edit할 툴을 담을 화면
		self.createMenu()		
		self.createToolBar()
		self.photoEditorWidget() # Central Widget

		self.show() 
	
	def centerMainWindow(self):
		desktop = QDesktopWidget().screenGeometry()
		screen_width = desktop.width()
		screen_height = desktop.height()
		# print(f"{screen_width}, {screen_height}")
		self.move(int(((screen_width - self.width())/2)), int(((screen_height - self.height())/2)))

	def createToolsDockWidget(self):
		self.dock_tools_view = QDockWidget()
		self.dock_tools_view.setWindowTitle("Edit Tools")
		self.dock_tools_view.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
	
		# 독 위젯안에 모든 위젯을 담는 QWidget 생성
		self.tools_contents = QWidget()

		self.rotate90 = QPushButton("Rotate 90")
		self.rotate90.setMinimumSize(QSize(130, 40))
		self.rotate90.setStatusTip("시계 방향으로 90도 회전")
		self.rotate90.clicked.connect(self.rotateImage90)

		self.rotate180 = QPushButton("Rotate 180")
		self.rotate180.setMinimumSize(QSize(130, 40))
		self.rotate180.setStatusTip("시계 방향으로 180도 회전")
		self.rotate180.clicked.connect(self.rotateImage180)

		self.flipHorizontal = QPushButton("Flip Horizontal")
		self.flipHorizontal.setMinimumSize(QSize(130, 40))
		self.flipHorizontal.setStatusTip("가로 플립")
		self.flipHorizontal.clicked.connect(self.flipImageHorizontal)	

		self.flipVertical = QPushButton("Flip Vertical")
		self.flipVertical.setMinimumSize(QSize(130, 40))
		self.flipVertical.setStatusTip("세로 플립")
		self.flipVertical.clicked.connect(self.flipImageVertical)	
		
		self.resizeHalf = QPushButton('Resize Half')
		self.resizeHalf.setMinimumSize(QSize(130, 40))
		self.resizeHalf.setStatusTip('반으로 줄이기')
		self.resizeHalf.clicked.connect(self.resizeImageHalf)   

		# 푸쉬 버튼을 버티컬 레이아웃에 추가
		dock_v_box = QVBoxLayout()
		dock_v_box.addWidget(self.rotate90)
		dock_v_box.addWidget(self.rotate180)
		dock_v_box.addWidget(self.flipHorizontal)
		dock_v_box.addWidget(self.flipVertical)
		dock_v_box.addWidget(self.resizeHalf)
		dock_v_box.addStretch()

		self.tools_contents.setLayout(dock_v_box)
		self.dock_tools_view.setWidget(self.tools_contents)		
		self.addDockWidget(Qt.RightDockWidgetArea, self.dock_tools_view)
		self.toggle_doc_tools_act = self.dock_tools_view.toggleViewAction()

	def rotateImage90(self):
		if self.image.isNull()==False:
			transform90 = QTransform().rotate(90)
			pixmap = QPixmap(self.image)
			rotated = pixmap.transformed(transform90, mode = Qt.SmoothTransformation)
			self.image_label.setPixmap(rotated.scaled(self.image_label.size(),
				Qt.KeepAspectRatio, Qt.SmoothTransformation))
			self.image = QPixmap(rotated)
			self.image_label.repaint()
		else : 
			pass

	def rotateImage180(self):
		if self.image.isNull()==False:
			transform180 = QTransform().rotate(180)
			pixmap = QPixmap(self.image)
			rotated = pixmap.transformed(transform180, mode = Qt.SmoothTransformation)
			self.image_label.setPixmap(rotated.scaled(self.image_label.size(),
				Qt.KeepAspectRatio, Qt.SmoothTransformation))
			self.image = QPixmap(rotated)
			self.image_label.repaint()
		else : 
			pass

	def flipImageHorizontal(self):
		if self.image.isNull()==False:
			flip_h = QTransform().scale(-1, 1)
			pixmap = QPixmap(self.image)
			flipped = pixmap.transformed(flip_h, mode = Qt.SmoothTransformation)
			self.image_label.setPixmap(flipped.scaled(self.image_label.size(),
				Qt.KeepAspectRatio, Qt.SmoothTransformation))
			self.image = QPixmap(flipped)
			self.image_label.repaint()
		else : 
			pass

	def flipImageVertical(self):
		if self.image.isNull()==False:
			flip_v = QTransform().scale(1, -1)
			pixmap = QPixmap(self.image)
			flipped = pixmap.transformed(flip_v, mode = Qt.SmoothTransformation)
			self.image_label.setPixmap(flipped.scaled(self.image_label.size(),
				Qt.KeepAspectRatio, Qt.SmoothTransformation))
			self.image = QPixmap(flipped)
			self.image_label.repaint()
		else : 
			pass	
	
	def resizeImageHalf(self) :
		if self.image.isNull() == False :
			resize = QTransform().scale(0.5, 0.5)
			pixmap = QPixmap(self.image)
			resized = pixmap.transformed(resize, mode = Qt.SmoothTransformation)
			self.image_label.setPixmap(resized.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
			self.image = QPixmap(resized)
			self.image_label.repaint()
		else :
			pass
	
	def createWidgets(self):			
		self.text_field = QTextEdit()
		self.setCentralWidget(self.text_field)

	def createMenu(self):
		self.open_act = QAction(QIcon('images/open_file.png'), "Open", self)
		self.open_act.setShortcut("Ctrl+O")
		self.open_act.setStatusTip("새로운 이미지 오픈")
		self.open_act.triggered.connect(self.openImage)

		self.save_act = QAction(QIcon('images/save_file.png'), "Save", self)
		self.save_act.setShortcut("Ctrl+S")
		self.save_act.setStatusTip("이미지 저장")
		self.save_act.triggered.connect(self.saveImage)

		self.print_act = QAction(QIcon('images/print.png'), "Print", self)
		self.print_act.setShortcut("Ctrl+P")
		self.print_act.setStatusTip("이미지 출력")
		self.print_act.triggered.connect(self.printImage)	

		self.clear_act = QAction(QIcon('images/clear.png'), "Clear", self)
		self.clear_act.setShortcut("Ctrl+D")
		self.clear_act.setStatusTip("이미지 출력")
		self.clear_act.triggered.connect(self.clearImage)		

		menu_bar = self.menuBar()
		menu_bar.setNativeMenuBar(False)

		file_menu = menu_bar.addMenu("File")
		file_menu.addAction(self.open_act)
		file_menu.addAction(self.save_act)
		file_menu.addAction(self.print_act)
		file_menu.addAction(self.clear_act)

		view_menu = menu_bar.addMenu("View")
		view_menu.addAction(self.toggle_doc_tools_act)

		self.setStatusBar(QStatusBar(self))
		
	def openImage(self):
		image_file, _ =QFileDialog.getOpenFileName(self, 
			"Open Image" ,"",
			"JPG 파일(*.jpeg *.jpg);;BMP파일 (*.bmp);; GIF 파일(*.gif) ")
		if image_file:
			self.image = QPixmap(image_file)
			self.image_label.setPixmap(self.image.scaled(self.image_label.size(),
				Qt.KeepAspectRatio, Qt.SmoothTransformation))
		else : 
			QMessageBox.information(self, "Error", "이미지를 열 수 없습니다.", QMessageBox.Ok)

	def saveImage(self):
		image_file, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
			"JPG 파일(*.jpeg *.jpg);;BMP파일 (*.bmp);; GIF 파일(*.gif) ")
		if image_file and self.image.isNull() == False : 
			self.image.save(image_file)
		else :
			QMessageBox.information(self, "Error", "이미지를 저장할 수 없습니다", QMessageBox.Ok)

	def printImage(self):
		printer = QPrinter()
		printer.setOutputFormat(QPrinter.NativeFormat)

		print_dialog = QPrintDialog(printer)

		if (print_dialog.exec_() == QPrintDialog.Accepted ):
			painter = QPainter()
			painter.begin(printer)
			rect = QRect(painter.viewport())
			size = QSize(self.image_label.pixmap().size())
			size.scale(rect.size(), Qt.KeepAspectRatio)
			painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
			painter.setWindow(self.image_label.pixmap().rect())
			painter.drawPixmap(0,0,self.image_label.pixmap())
			painter.end()

	def clearImage(self):
		self.image_label.clear()
		self.image = QPixmap()

	def createToolBar(self):
		tool_bar = QToolBar("Photo Editor Toolbar")
		tool_bar.setIconSize(QSize(24,24))
		self.addToolBar(tool_bar)

		tool_bar.addAction(self.open_act)
		tool_bar.addAction(self.save_act)
		tool_bar.addAction(self.print_act)
		tool_bar.addAction(self.clear_act)
		
	def photoEditorWidget(self):
		self.image = QPixmap()
		self.image_label = QLabel()
		self.image_label.setAlignment(Qt.AlignCenter)
		self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
		self.setCentralWidget(self.image_label)
	
if __name__ ==  '__main__' :
	app = QApplication(sys.argv)		
	window = PhotoEditor()
	sys.exit(app.exec_())