# 절대위치 레이아웃
# 박스 레이아웃
# QBoxLayout(가로정렬 Horizontal, 세로정렬 Vertical)
# QFormLayOut(폼 작성)
# 그리드 레이아웃
# QGridLayout(x,y 좌표로 배치)

# QSpinBox
# ComboBox

# spin_combo_boxes.py

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
	QPushButton, QButtonGroup, QCheckBox, QLineEdit, QMessageBox, 
	QCheckBox, QComboBox, QSpinBox, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QCoreApplication, Qt

# QLineEdit : 1줄만 입력 가능
# QTextEdit : 여러줄 입력 가능

class SelectItems(QWidget):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 300, 200) # 창 위치 지정
		self.setWindowTitle("런치") # 창 캡션
		self.ItemsAndPrices()
		self.show() 

	def ItemsAndPrices(self):
		select_comment = QLabel("메뉴 2가지 선택")
		select_comment.setFont(QFont("Arial", 16))
		select_comment.setAlignment(Qt.AlignCenter)

		self.sum_comment = QLabel("전체 금액 : ")
		self.sum_comment.setFont(QFont("Arial", 16))
		self.sum_comment.setAlignment(Qt.AlignRight)

		# 음식 목록
		lunch_list = ["삶은 계란", "토스트", "요구르트","사과","커피","바나나","오렌지","와플","빵","파스타"]
		select_item1 = QComboBox()
		select_item1.addItems(lunch_list)
		select_item1.addItem("라면")

		select_item2 = QComboBox()
		select_item2.addItems(lunch_list)

		self.price_sb1 = QSpinBox()
		self.price_sb1.setRange(0,10000)
		self.price_sb1.setSingleStep(500)
		self.price_sb1.setPrefix("""\\""")
		self.price_sb1.valueChanged.connect(self.calcTotal)

		self.price_sb2 = QSpinBox()
		self.price_sb2.setRange(0,10000)
		self.price_sb2.setSingleStep(500)
		self.price_sb2.setPrefix("""\\""")
		self.price_sb2.valueChanged.connect(self.calcTotal)

		h_box_select1 = QHBoxLayout()
		h_box_select1.addStretch()
		h_box_select1.addWidget(select_item1)
		h_box_select1.addWidget(self.price_sb1)
		h_box_select1.addStretch()

		h_box_select2 = QHBoxLayout()
		h_box_select2.addStretch()
		h_box_select2.addWidget(select_item2)
		h_box_select2.addWidget(self.price_sb2)
		h_box_select2.addStretch()

		v_box = QVBoxLayout()
		v_box.addStretch(1)
		v_box.addWidget(select_comment)
		v_box.addStretch(1)
		v_box.addLayout(h_box_select1)
		v_box.addLayout(h_box_select2)
		v_box.addStretch(1)
		v_box.addWidget(self.sum_comment)
		v_box.addStretch(2)

		self.setLayout(v_box)

	def calcTotal(self) :
		total_price = int(self.price_sb1.value()) + int(self.price_sb2.value())
		self.sum_comment.setText(f"전체 금액 : {total_price}")


# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv
	# print(sys.argv)
	window = SelectItems()
	sys.exit(app.exec_())
