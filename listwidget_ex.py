# listwidget_ex.py
import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
	QListWidget, QPushButton, QListWidgetItem, QHBoxLayout, QVBoxLayout, QInputDialog)
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon


class DangunGui(QWidget):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 400, 300)
		self.setWindowTitle("당근") # 창 캡션

		self. setupWidget()

		self.show()

	def setupWidget(self):
		self.list_widget = QListWidget()
		self.list_widget.setAlternatingRowColors(True)
		self.list_widget.setIconSize(QSize(200,150))

		dangun_list = ["노트20","충전기","아이폰13프로","소니","샤오미","삼성","폴더폰"]

		for item in dangun_list:
			icon_path = "images/note20.jpg"
			icon = QIcon(icon_path)
			list_item = QListWidgetItem()
			list_item.setIcon(icon)
			list_item.setText(item)
			size = QSize()
			size.setHeight(100)
			size.setWidth(400)
			list_item.setSizeHint(size)
			self.list_widget.addItem(list_item)

		add_button = QPushButton("Add")
		add_button.clicked.connect(self.addListItem)

		remove_button = QPushButton("Remove")
		remove_button.clicked.connect(self.removeListItem)		

		right_v_box  =QVBoxLayout()
		right_v_box.addWidget(add_button)
		right_v_box.addWidget(remove_button)

		h_box = QHBoxLayout()
		h_box.addWidget(self.list_widget)
		h_box.addLayout(right_v_box)

		self.setLayout(h_box)

	def removeListItem(self):
		row = self.list_widget.currentRow()
		self.list_widget.takeItem(row)		

	def addListItem(self):
		text, ok = QInputDialog.getText(self, "New Item", "Add Item : ")
		if ok and text != "" :
			list_item = QListWidgetItem()
			list_item.setText(text)
			image, ok = QInputDialog.getText(self, "New Image", "New Image Path : ")
			if ok and image != "":
				list_item.setIcon(QIcon(image))
			else :
				list_item.setIcon(QIcon("images/note20.jpg"))
			size = QSize()
			size.setHeight(100)
			size.setWidth(400)
			list_item.setSizeHint(size)				
			self.list_widget.addItem(list_item)		

# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv
	# print(sys.argv)
	window = DangunGui()
	sys.exit(app.exec_())