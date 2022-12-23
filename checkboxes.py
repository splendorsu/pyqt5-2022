import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QCheckBox
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QCoreApplication, Qt

class CheckBoxWindow(QWidget):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 400, 400)
		self.setWindowTitle("PyQt5_CheckBox Widget")
		self.displayCheckBoxes()
		self.show()

	def displayCheckBoxes(self):
		header_label = QLabel(self)
		header_label.setText("근무가능 시간대 (가능한 시간대 모두 체크)")
		header_label.move(10,10)
		header_label.resize(300,20)
		header_label.setWordWrap(True)

		cb_morning = QCheckBox("8 am ~ 2 pm", self)
		cb_morning.move(20,40)
		cb_morning.stateChanged.connect(self.printToTerminal)
		cb_morning.toggle()		

		cb_after = QCheckBox("1 pm ~ 8 pm", self)
		cb_after.move(20,60)
		cb_after.stateChanged.connect(self.printToTerminal)

		cb_night = QCheckBox("7 pm ~ 3 am ", self)
		cb_night.move(20,80)
		cb_night.stateChanged.connect(self.printToTerminal)

	def printToTerminal(self, state):
		sender = self.sender()
		if state == Qt.Checked:
			print(f"""Selected Working Time : {sender.text()}""")
		else :
			print(f"""Unselected Working Time : {sender.text()}""")


# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv
	# print(sys.argv)
	window = CheckBoxWindow()
	sys.exit(app.exec_())