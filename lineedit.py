import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QCheckBox, QLineEdit
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QCoreApplication, Qt

class EntryWindow(QWidget):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 400, 200)
		self.setWindowTitle("PyQt5_CheckBox Widget")
		self.displayWidgets()
		self.show()

	def displayWidgets(self):
		QLabel("Enter Your name:", self).move(80,10)
		name_label = QLabel("Name : " , self)
		name_label.move(70,50)

		self.name_entry = QLineEdit(self)
		self.name_entry.setAlignment(Qt.AlignLeft)
		self.name_entry.move(130,50)
		self.name_entry.resize(200,20)

		self.clear_button = QPushButton('Clear', self)
		self.clear_button.clicked.connect(self.clearEntries)
		self.clear_button.move(160,110)

	def clearEntries(self):
		sender = self.sender()
		if sender.text() == 'Clear':
			self.name_entry.clear()


# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv
	# print(sys.argv)
	window = EntryWindow()
	sys.exit(app.exec_())