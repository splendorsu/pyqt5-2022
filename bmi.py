import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QCheckBox, QLineEdit
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QCoreApplication, Qt

class TestWindow(QWidget):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 400, 250)
		self.setWindowTitle("BMI Calculator")
		self.displayWidgets()
		self.show()

	def displayWidgets(self):
		QLabel("Enter your height and weight", self).move(100,10)

		height_label = QLabel("Height (cm) : " , self)
		height_label.move(20,50)
		self.height_entry = QLineEdit(self)
		self.height_entry.setAlignment(Qt.AlignLeft)
		self.height_entry.move(130,50)
		self.height_entry.resize(200,20)

		weight_label = QLabel("Weight (cm) : " , self)
		weight_label.move(20,100)
		self.weight_entry = QLineEdit(self)
		self.weight_entry.setAlignment(Qt.AlignLeft)
		self.weight_entry.move(130,100)
		self.weight_entry.resize(200,20)	

		self.enter_button = QPushButton('Enter', self)
		self.enter_button.clicked.connect(self.CalculateEntries)
		self.enter_button.move(100,150)

		self.clear_button = QPushButton('Clear', self)
		self.clear_button.clicked.connect(self.clearEntries)
		self.clear_button.move(210,150)

		self.bmi_label = QLabel("Your BMI : - ", self)
		self.bmi_label.move(100,200)
		self.bmi_label.resize(230,20)	

	def CalculateEntries(self) :
		height = self.height_entry.text()
		weight = self.weight_entry.text()
		bmi = round(float(weight) / pow((float(height)/100), 2), 2)
		self.bmi_label.setText(f"Your BMI : {bmi} ")

	def clearEntries(self):
		sender = self.sender()
		if sender.text() == 'Clear':
			self.height_entry.clear()
			self.weight_entry.clear()
			self.bmi_label.setText(f"Your BMI : - ")

# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv
	window = TestWindow()
	sys.exit(app.exec_())
