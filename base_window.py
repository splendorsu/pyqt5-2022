# test.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget

class EmptyWindow(QWidget):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 400, 300)
		self.setWindowTitle("안녕하세요") # 창 캡션
		self.show()

# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv
	# print(sys.argv)
	window = EmptyWindow()
	sys.exit(app.exec_())