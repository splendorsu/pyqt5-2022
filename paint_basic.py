# paint_basic.py
import sys
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.QtGui import (QPainter, QPainterPath, QColor, QBrush, QPen, QFont, QPolygon, QLinearGradient)
from PyQt5.QtCore import Qt, QPoint


class Drawing(QWidget):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setFixedSize(600,600)
		self.setWindowTitle("QPainter Basic") # 창 캡션
		
		self.black = "#1000000"
		self.blue = "#2041F1"
		self.green = "#12A708"
		self.purple = "#6512F0"
		self.red = "E00C0C"
		self.orange = "#FF930A"

		self.show()

	def paintEvent(self,event):
		painter = QPainter()
		painter.begin(self)
		painter.setRenderHint(QPainter.Antialiasing)

		self.drawPoints(painter)
		self.drawLines(painter)
		self.drawText(painter)
		self.drawRect(painter)
		self.drawCircle(painter)

		painter.end()

	def drawPoints(self, painter):
		pen = QPen(QColor(self.black))
		
		for i in range(1,9) : 
			pen.setWidth(i * 2)
			painter.setPen(pen)
			painter.drawPoint(i* 20 , i*20)

	def drawLines(self, painter):
		pen = QPen(QColor(self.black), 2)
		painter.setPen(pen)
		painter.drawLine(230,20,230,180)

		pen.setStyle(Qt.DashLine)
		painter.setPen(pen)
		painter.drawLine(260,20,260,180)

		pen.setStyle(Qt.DotLine)
		painter.setPen(pen)
		painter.drawLine(290,20,290,180)

		blue_pen = QPen(QColor(self.blue),4)
		blue_pen.setStyle(Qt.DashDotLine)
		painter.setPen(blue_pen)
		painter.drawLine(320,20,320,180)

	def drawText(self, painter):
		text = "안녕하세요"
		pen = QPen(QColor(self.red))
		painter.setFont(QFont("Helvetica", 15 )) # 고딕체
		painter.setPen(pen)
		painter.drawText(420,110,text)

	def drawRect(self, painter):
		pen = QPen(QColor(self.black))
		brush = QBrush(QColor(Qt.green))
		painter.setPen(pen)
		painter.setBrush(brush)

		painter.drawRect(20,220,80,80)

	def drawCircle(self, painter):

		height , width = self.height(), self.width()
		center_x, center_y = height/2, width/2
		radius_x, radius_y = 60, 60

		pen =  QPen(Qt.black, 2, Qt.SolidLine)
		brush = QBrush(Qt.darkMagenta)
		painter.setPen(pen)
		painter.setBrush(brush)		

		painter.drawEllipse(QPoint(int(center_x), int(center_y)), radius_x, radius_y)


# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv
	# print(sys.argv)
	window = Drawing()
	sys.exit(app.exec_())