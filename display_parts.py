# displays_parts.py

import sys, csv
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
	QTextEdit, QMessageBox, QFileDialog, QHBoxLayout, QVBoxLayout, QTableView)
from PyQt5.QtGui import QStandardItem, QStandardItemModel

from PyQt5.QtCore import QObject, pyqtSignal

class DisplayPart(QWidget):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 450, 300) # 창 위치 지정
		self.setWindowTitle("부품") # 창 캡션
		self.setupParts()
		self.show() 

	def setupParts(self):
		self.model = QStandardItemModel()

		table_view = QTableView()
		table_view.SelectionMode(3)
		table_view.setModel(self.model)

		self.model.setRowCount(3)
		self.model.setColumnCount(4)

		self.loadCSVFile()

		v_box = QVBoxLayout()
		v_box.addWidget(table_view)

		self.setLayout(v_box)


	def loadCSVFile(self):
		file_name = "files/parts.csv"

		with open(file_name, 'r') as f:
			reader = csv.reader(f)
			header_labels = next(reader)
			self.model.setHorizontalHeaderLabels(header_labels)
			for i , row  in enumerate(csv.reader(f)):
				items = [QStandardItem(item) for item in row]
				self.model.insertRow(i, items)


# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv
	# print(sys.argv)
	window = DisplayPart()
	sys.exit(app.exec_())