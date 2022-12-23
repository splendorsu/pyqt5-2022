# age_check.py

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import  Qt, pyqtSignal, QObject

class SendSignal(QObject):
	change_age = pyqtSignal(int)

class SignalWindow(QWidget):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 300, 200)
		self.setWindowTitle("당신의 나이") # 창 캡션
		self.ageDefine()
		self.show()

	def ageDefine(self):
		age_label = QLabel("당신의 나이 : ")
		self.age_input = QLineEdit()
		self.age_result = QLabel("")

		h_box = QHBoxLayout()		
		h_box.addWidget(age_label)
		h_box.addWidget(self.age_input)
		h_box.addStretch(2)		
		
		v_box = QVBoxLayout()
		v_box.addStretch(1)
		v_box.addLayout(h_box)
		v_box.addWidget(self.age_result)
		v_box.addStretch(1)

		self.setLayout(v_box)

		self.sig = SendSignal()
		self.age_input.textChanged.connect(self.ageCheck) # 1번 줄
		self.sig.change_age.connect(self.ageCheck2) # 2번 줄

		# self.sig.change_age.emit()

	def ageCheck2(self, age): # 1번 줄에서 emit 된 값을 시그널로 받아서 
		print(age) 
		if age < 20 :
			value = "어림"
		elif age >= 20 : 
			value = "청년"
		elif age >= 30 : 
			value = "장년"
		elif age >= 50 : 
			value = "중년"
		else : 
			value = "노년"
		self.age_result.setText(f"당신은 {value}")

	def ageCheck(self):
		try : 
			age = int(self.age_input.text())
			self.sig.change_age.emit(age) # 1번줄에서 textchanged된 시그널로 입력된 값을 age로 내보냄
		except:
			age = 0		

# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv
	# print(sys.argv)
	window = SignalWindow()
	sys.exit(app.exec_())