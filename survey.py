# 절대위치 레이아웃
# 박스 레이아웃
# QBoxLayout(가로정렬 Horizontal, 세로정렬 Vertical)
# QFormLayOut(폼 작성)
# 그리드 레이아웃
# QGridLayout(x,y 좌표로 배치)

# QSpinBox
# ComboBox

# survey.py

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QButtonGroup,
 QCheckBox, QLineEdit, QMessageBox, QCheckBox, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QCoreApplication, Qt

# QLineEdit : 1줄만 입력 가능
# QTextEdit : 여러줄 입력 가능

class Survey(QWidget):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 400, 230) # 창 위치 지정
		self.setWindowTitle("설문조사") # 창 캡션
		self.surveyWidgets()
		self.show() 

	def surveyWidgets(self):
		# Title 
		title = QLabel("구로구 호텔")
		title.setFont(QFont("Arial", 12))
		sub_title = QLabel("오늘 저희 서비스에 만족하셨습니까?")
		sub_title.setFont(QFont('Arial', 10))		
		sub_title.setAlignment(Qt.AlignCenter)

		h_box_title = QHBoxLayout()
		h_box_title.addStretch()
		h_box_title.addWidget(title)
		h_box_title.addStretch()

		# h_box_subtitle = QHBoxLayout()
		# h_box_subtitle.addStretch()
		# h_box_subtitle.addWidget(sub_title)
		# h_box_subtitle.addStretch()

		ratings = ["불만족", "보통", "만족"]
		h_box_rating = QHBoxLayout()
		h_box_rating.setSpacing(70)
		h_box_rating.addStretch()
		for rating in ratings:
			rate_label = QLabel(rating)
			rate_label.setFont(QFont('Arial', 10))		
			h_box_rating.addWidget(rate_label)
		h_box_rating.addStretch()			

		h_box_cb = QHBoxLayout()
		rating_bg = QButtonGroup(self)
		h_box_cb.setSpacing(80)
		h_box_cb.addStretch()	
		for cb_rate in range(len(ratings)):
			rating_cb = QCheckBox(str(cb_rate), self)		
			rating_bg.addButton(rating_cb)
			h_box_cb.addWidget(rating_cb)
		h_box_cb.addStretch()
		rating_bg.buttonClicked.connect(self.checkboxClicked)

		summit_button = QPushButton("제출")
		summit_button.setFont(QFont("Arial", 12))
		summit_button.clicked.connect(self.close)

		v_box = QVBoxLayout()
		v_box.addStretch(1)
		v_box.addLayout(h_box_title)
		v_box.addWidget(sub_title)
		# v_box.addLayout(h_box_subtitle)
		v_box.addStretch(1)
		v_box.addLayout(h_box_rating)
		v_box.addLayout(h_box_cb)
		v_box.addStretch(1)
		v_box.addWidget(summit_button)
		v_box.addStretch(2)

		self.setLayout(v_box)

	def checkboxClicked(self, cb) :
		print(f"{cb.text()} selected")


# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv
	# print(sys.argv)
	window = Survey()
	sys.exit(app.exec_())