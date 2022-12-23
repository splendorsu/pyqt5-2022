# phone.py

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QTextEdit,
	QPushButton, QButtonGroup, QCheckBox, QLineEdit, QMessageBox, QDoubleSpinBox,
	QComboBox, QSpinBox, QHBoxLayout,  QVBoxLayout, QGridLayout, QFormLayout)
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
		self.setGeometry(100, 100, 600, 400) # 창 위치 지정
		self.setWindowTitle("Todo List") # 창 캡션
		self.phoneWidgets()
		self.show() 

	def phoneWidgets(self):
		title = QLabel("휴대폰 월 할부금 구하기")
		title.setFont(QFont("Arial", 24))
		title.setAlignment(Qt.AlignCenter)

		pay_money_title = QLabel("할부원금 : ")
		pay_money_title.setFont(QFont("Ariel", 16))
		pay_money_title.setAlignment(Qt.AlignLeft)
		self.pay_money = QLineEdit(self)
		self.pay_money.setPlaceholderText("원")

		pay_month_title = QLabel("할부개월수 : ")
		pay_month_title.setFont(QFont("Ariel", 16))
		pay_month_title.setAlignment(Qt.AlignLeft)
		self.pay_month = QLineEdit(self)
		self.pay_month.setPlaceholderText("개월")

		pay_rate_title = QLabel("할부수수료(년이율 %) : ")
		pay_rate_title.setFont(QFont("Ariel", 16))
		pay_rate_title.setAlignment(Qt.AlignLeft)
		self.pay_rate = QDoubleSpinBox(self)

		cal_button = QPushButton("계산")
		cal_button.clicked.connect(self.CalculateMoney)
		cal_button.setFont(QFont("Ariel", 18))

		self.result = QLabel("월 할부금 : ", self)
		self.result.setFont(QFont("Ariel", 20))
		self.result.setAlignment(Qt.AlignCenter)

		form = QFormLayout()
		form.addRow(title)
		form.addRow(pay_money_title, self.pay_money)
		form.addRow(pay_month_title, self.pay_month)
		form.addRow(pay_rate_title, self.pay_rate)
		form.addRow(cal_button)
		form.addRow(self.result)

		self.setLayout(form)


	def CalculateMoney(self):
		p = int(self.pay_money.text())
		n = int(self.pay_month.text()) 
		r = float(self.pay_rate.value()) / 1200 
		result_cal = int(p * ((r * (pow((1 + r), n))  / (pow((1 + r), n) - 1) )))
		self.result.setText(f"월 할부금 : {result_cal} 원")

# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv
	# print(sys.argv)
	window = AppForm()
	sys.exit(app.exec_())
