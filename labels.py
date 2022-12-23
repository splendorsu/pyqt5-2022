import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QFont

class HelloWorldWindow(QWidget):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 400, 400)
		self.setWindowTitle("PyQt5_TestBoard")
		self.displayLabels()
		self.show()

	def displayLabels(self):
		text = QLabel(self)
		text.setText("안녕하세요 메시!") # Label에 문구 작성하기
		text.move(110, 15)
		text.setFont(QFont('Arial', 20))

		images = "images/messi.jpg"
		profile_image = "images/ariel.jpg"
		try : 
			with open(images) :
				messi_image = QLabel(self)
				pixmap = QPixmap(images) # Label에 이미지 삽입하기
				messi_image.setPixmap(pixmap)
				messi_image.move(50, 50)
		except FileNotFoundError : 
			print("Error : No image in path!")
		try : 
			with open(profile_image) :
				user_image = QLabel(self)
				pixmap = QPixmap(profile_image) # Label에 이미지 삽입하기
				user_image.setPixmap(pixmap)
				user_image.move(150, 200)
		except FileNotFoundError : 
			print("Error : No image in path!")


# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv
	# print(sys.argv)
	window = HelloWorldWindow()
	sys.exit(app.exec_())