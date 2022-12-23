# 절대위치 레이아웃
# 박스 레이아웃
# QBoxLayout(가로정렬 Horizontal, 세로정렬 Vertical)
# QFormLayOut(폼 작성)
# 그리드 레이아웃
# QGridLayout(x,y 좌표로 배치)

# QSpinBox
# ComboBox

# application.py

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QTextEdit,
	QPushButton, QButtonGroup, QCheckBox, QLineEdit, QMessageBox, 
	QCheckBox, QComboBox, QSpinBox, QHBoxLayout, QVBoxLayout, QFormLayout)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QCoreApplication, Qt

# QLineEdit : 1줄만 입력 가능
# QTextEdit : 여러줄 입력 가능

class AppForm(QWidget):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 300, 200) # 창 위치 지정
		self.setWindowTitle("헤어컷 예약 신청") # 창 캡션
		self.formWidgets()
		self.show() 

	def formWidgets(self):
		title = QLabel("이름 : ")
		title.setFont(QFont("Arial", 18))
		title.setAlignment(Qt.AlignLeft)
		
		name = QLineEdit()
		address = QLineEdit()
		mobile_num = QLineEdit()
		mobile_num.setInputMask("000-0000-0000;")

		age_label = QLabel("나이 : ")
		age = QSpinBox()
		age.setRange(1,110)

		height_label = QLabel("키 : ")
		height = QLineEdit()
		height.setPlaceholderText("cm")
		weight_label = QLabel("몸무게 : ")
		weight = QLineEdit()
		weight.setPlaceholderText("kg")

		gender = QComboBox()
		gender.addItems(["남", "여"])

		hair = QTextEdit()
		hair.setPlaceholderText("최대한 자세히 작성 바랍니다.")

		hours = QSpinBox()
		hours.setRange(1, 12)
		minutes = QComboBox()
		minutes.addItems([":00", ":15",":30",":45"])
		ampm = QComboBox()
		ampm.addItems(["AM","PM"])

		summit_button = QPushButton("예약하기")
		summit_button.clicked.connect(self.close)

		h_box_info = QHBoxLayout()
		h_box_info.setSpacing(10)
		h_box_info.addWidget(age_label)
		h_box_info.addWidget(age)
		h_box_info.addWidget(height_label)
		h_box_info.addWidget(height)
		h_box_info.addWidget(weight_label)
		h_box_info.addWidget(weight)

		h_box_time = QHBoxLayout()
		h_box_time.setSpacing(10)
		h_box_time.addWidget(hours)
		h_box_time.addWidget(minutes)
		h_box_time.addWidget(ampm)

		app_form_layout = QFormLayout()
		app_form_layout.addRow(title)
		app_form_layout.addRow("이름 : ", name)
		app_form_layout.addRow("주소 : ", address)
		app_form_layout.addRow("전화번호 : " , mobile_num )
		app_form_layout.addRow(h_box_info)
		app_form_layout.addRow("성별 : ", gender)
		app_form_layout.addRow("머리결 상태", hair)
		app_form_layout.addRow("희망시간 : ", h_box_time)
		app_form_layout.addRow(summit_button)

		self.setLayout(app_form_layout)

	def calcTotal(self) :
		total_price = int(self.price_sb1.value()) + int(self.price_sb2.value())
		self.sum_comment.setText(f"전체 금액 : {total_price}")


# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv
	# print(sys.argv)
	window = AppForm()
	sys.exit(app.exec_())
