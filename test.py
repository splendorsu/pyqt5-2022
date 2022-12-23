
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel,QPushButton

class EmptyWindow(QWidget):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 400, 300)
		self.setWindowTitle("안녕하세요") #  창 캡션
		self.showWidget()
		self.show()

	def showWidget(self):
		v_box = QVBoxLayout()
		line_edit = QLineEdit()
		label = QLabel("Test")
		button = QPushButton("Warning!")
		button.setObjectName("Warning")
		# Style 바꾸기
		line_edit.setStyleSheet("""background-color:blue;
			color: rgb(244,160,25);""")
		label.setStyleSheet("""background-color:skyblue;
			color : white;
			border-style: outset;
			border-width: 3px;
			border-radius: 5px;
			font : bold 24px 'Times New Roman';
			qproperty-alignment:AlignCenter""")

		v_box.addWidget(line_edit)
		v_box.addWidget(label)
		v_box.addWidget(button)
		self.setLayout(v_box)

# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv
	# pseudo element
	style_sheet = """
		QPushButton#Warning { 
		background-color : #C92108 ;
		border-radius : 10px;
		padding : 6px;
		color: #FFFFFF;
		}	
		QPushButton#Warning:hover { 
		background-color : green ;
		color : red
		}
		QPushButton#Warning:pressed { 
		background-color : #F4B519 ;
		}	
		"""

	app.setStyleSheet(style_sheet)
	# print(sys.argv)
	window = EmptyWindow()
	sys.exit(app.exec_())