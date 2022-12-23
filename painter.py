# painter.py
import sys, os
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QAction,
	 QLabel, QToolBar, QStatusBar, QToolTip, QColorDialog, QFileDialog)
from PyQt5.QtGui import (QPainter, QPainterPath, QPixmap, QIcon, 
	QColor, QBrush, QPen, QFont, QPolygon, QLinearGradient)
from PyQt5.QtCore import Qt, QPoint, QRect, QSize

class Canvas(QLabel):
	def __init__(self, parent):
		super().__init__(parent)
		width , height = 900, 600
		self.parent = parent
		self.parent.setFixedSize(width, height)

		pixmap = QPixmap(width, height)
		pixmap.fill(Qt.white)
		self.setPixmap(pixmap)

		self.mouse_track_label = QLabel()
		self.setMouseTracking(True)

		self.antialiasing_status = False
		self.eraser_selected = False

		self.last_mouse_pos = QPoint()
		self.drawing = False
		self.pen_color = Qt.black
		self.pen_width = 2 

	def mouseMoveEvent(self, event):
		mouse_pos = event.pos()
		if (event.buttons() and Qt.LeftButton) and self.drawing :
			self.mouse_pos = event.pos()
			self.drawOnCanvas(mouse_pos)
		self.mouse_track_label.setVisible(True)
		sb_text = f"마우스 좌표 : {mouse_pos.x()}, {mouse_pos.y()}"
		self.mouse_track_label.setText(sb_text)
		self.parent.status_bar.addWidget(self.mouse_track_label)

	def drawOnCanvas(self, points):
		painter = QPainter(self.pixmap())
		
		if self.antialiasing_status:
			painter.setRenderHint(QPainter.Antialiasing)

		if self.eraser_selected ==False:
			pen = QPen(QColor(self.pen_color), self.pen_width)
			painter.setPen(pen)
			painter.drawLine(self.last_mouse_pos, points)
			self.last_mouse_pos = points

		elif self.eraser_selected :
			eraser = QRect(points.x(), points.y(), 12, 12)
			painter.eraseRect(eraser)
			
		painter.end()
		self.update()

	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.last_mouse_pos = event.pos()
			self.drawing = True

	def mouseReleaseEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.drawing = False
		elif self.eraser_selected == True:
			self.eraser_selected= False

	def paintEvent(self, event):
		painter = QPainter(self)
		# target_rect = QRect() 
		target_rect = event.rect()
		painter.drawPixmap(target_rect, self.pixmap(), target_rect)

	def newCanvas(self):
		self.pixmap().fill(Qt.white)
		self.update()
		
	def saveFile(self):
		file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "",
			"PNG 파일 (*.png)")
		if file_name :
			self.pixmap().save(file_name, "png")

	def selectTool(self, tool_name):
		if tool_name == "pencil":
			self.eraser_selected = False
			self.pen_width = 2

		elif tool_name == "marker":
			self.eraser_selected = False
			self.pen_width = 8

		elif tool_name == "eraser":
			self.eraser_selected = True

		elif tool_name == "color":
			self.eraser_selected = False
			color = QColorDialog.getColor()
			if color.isValid():
				self.pen_color = color

class PainterWindow(QMainWindow):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setMinimumSize(700,600)
		self.setWindowTitle("Painter") # 창 캡션
		QToolTip.setFont(QFont("Helvetica", 12))
		
		self.createCanvas() # drawing 하는 영역 생성
		self.createMenu() # 메뉴 부분 생성
		self.createToolbar() # 툴바 생성

		self.show()

	def createCanvas(self):
		self.canvas = Canvas(self)
		self.setCentralWidget(self.canvas)

	def createMenu(self):
		new_act = QAction("New Canvas", self)
		new_act.setShortcut("Cntl+N")
		new_act.triggered.connect(self.canvas.newCanvas)

		save_canvas_act = QAction("Save Canvas", self)
		save_canvas_act.setShortcut("Cntl+S")
		save_canvas_act.triggered.connect(self.canvas.saveFile)

		anti_al_act= QAction("Antialiasing", self, checkable = True)
		anti_al_act.triggered.connect(self.toggleAntialias)

		menu_bar = self.menuBar()
		menu_bar.setNativeMenuBar(False)

		file_menu = menu_bar.addMenu("File")
		file_menu.addAction(new_act)
		file_menu.addAction(save_canvas_act)

		tool_menu = menu_bar.addMenu("Tool")
		tool_menu.addAction(anti_al_act)

		self.status_bar = QStatusBar()
		self.setStatusBar(self.status_bar)

	def toggleAntialias(self, state):
		if state :
			self.canvas.antialiasing_status = True
		else :
			self.canvas.antialiasing_status = False

	def createToolbar(self):		
		tool_bar = QToolBar("Painting Toolbar")
		tool_bar.setIconSize(QSize(24,24))
		self.addToolBar(Qt.LeftToolBarArea, tool_bar)
		tool_bar.setMovable(False)

		pencil_act = QAction(QIcon("images/pencil.png"), "Pencil", tool_bar)
		pencil_act.setToolTip("연필")
		pencil_act.triggered.connect(lambda: self.canvas.selectTool("pencil"))

		marker_act = QAction(QIcon("images/marker.png"), "Marker", tool_bar)
		marker_act.setToolTip("마커")
		marker_act.triggered.connect(lambda: self.canvas.selectTool("marker"))
		
		eraser_act = QAction(QIcon("images/eraser.png"), "Eraser", tool_bar)
		eraser_act.setToolTip("지우개")
		eraser_act.triggered.connect(lambda: self.canvas.selectTool("eraser"))

		color_act = QAction(QIcon("images/color.png"), "Color", tool_bar)
		color_act.setToolTip("컬러")
		color_act.triggered.connect(lambda: self.canvas.selectTool("color"))

		tool_bar.addAction(pencil_act)
		tool_bar.addAction(marker_act)
		tool_bar.addAction(eraser_act)
		tool_bar.addAction(color_act)		

	def paintEvent(self,event):
		painter = QPainter()
		painter.begin(self)
		painter.setRenderHint(QPainter.Antialiasing)

		painter.end()


# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv
	# print(sys.argv)
	window = PainterWindow()
	sys.exit(app.exec_())