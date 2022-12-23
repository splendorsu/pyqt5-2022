import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QCoreApplication

class ButtonWindow(QWidget):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 400, 400)
		self.setWindowTitle("PyQt5_PushBotton Widget")
		self.displayButton()
		self.show()

	def displayButton(self):
		self.name_label = QLabel(self)
		self.name_label.setText("Push the Button")
		self.name_label.move(60, 30)

		button = QPushButton(self)
		button.setText("Click")
		button.clicked.connect(self.buttonClicked)
		button.move(80, 70)

	def buttonClicked(self):
		print("Hello")
		self.name_label.setText("Who are you?") # 위에서 지정한 문구 변경


# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv
	# print(sys.argv)
	window = ButtonWindow()
	sys.exit(app.exec_())