# notepad_mv.py

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
	QTextEdit, QMessageBox, QFileDialog, QHBoxLayout, QVBoxLayout)

from PyQt5.QtCore import QObject, pyqtSignal

class Model(QObject):
	error = pyqtSignal(str)

	def save(self, filename, content):
		error = ''
		if filename :
			try:
				with open(filename , 'w', encoding = 'utf-8') as f:
					f.write(content)

			except Exceptrion as e :
				error = f'파일 저장 에러 : {e}'
		else :
			error = "파일 이름이 없습니다."
		if error :
			self.error.emit(error)

class View(QWidget):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 300, 400) # 창 위치 지정
		self.setWindowTitle("메모장") # 창 캡션
		self.notepadWidgets()
		self.show() 

	def notepadWidgets(self):
		new_button = QPushButton("New", self)
		# new_button.move(10, 20)
		new_button.clicked.connect(self.clearText)

		save_button = QPushButton("Save", self)
		# save_button.move(100, 20)
		save_button.clicked.connect(self.saveText)

		top_h_box = QHBoxLayout()
		top_h_box.addStretch(1)
		top_h_box.addWidget(new_button)
		top_h_box.setSpacing(10)
		top_h_box.addWidget(save_button)
		top_h_box.addStretch(1)

		self.text_entry = QTextEdit(self)
		# self.text_entry.move(10, 60)
		# self.text_entry.resize(280, 300)
		main_h_box = QHBoxLayout()
		main_h_box.addWidget(self.text_entry)

		v_box = QVBoxLayout()
		v_box.addLayout(top_h_box)
		v_box.addLayout(main_h_box)

		self.setLayout(v_box)

	def clearText(self):
		answer = QMessageBox.question(self, "Clear Text", "텍스트를 지우시겠습니까?", QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes )
		if answer == QMessageBox.Yes :
			self.text_entry.clear()
		else :
			pass			

	def saveText(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog # option 기능 추가하는 방법
		notepad_text = self.text_entry.toPlainText()
		file_name, _ = QFileDialog.getSaveFileName(self, "파일 저장", "", "모든 파일(*.*);; 텍스트 파일(*.txt)", options = options)

		if file_name :
			with open(file_name, 'w', encoding = 'utf-8') as f:
				f.write(notepad_text)

# 프로그램 실행
if __name__ == '__main__':
	app = QApplication(sys.argv) # sys.argv
	# print(sys.argv)
	window = View()
	sys.exit(app.exec_())