# richtext_notepad.py

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, 
	QMessageBox, QTextEdit, QFileDialog, QInputDialog,
	QFontDialog, QColorDialog,
	QLabel, QPushButton, QVBoxLayout, QWidget,)
from PyQt5.QtGui import QIcon, QTextCursor, QColor
from PyQt5.QtCore import Qt
import random

class ChangeIcon(QMainWindow):
	def __init__(self):
		super().__init__()  # QWidget의 기본 생성자 부름
		self.initializeUI()

	def initializeUI(self):
		"""
		윈도우 화면에 출력되는 컨텐츠 초기화
		"""
		self.setGeometry(100, 100, 400, 500) # 가로 400 세로 500
		self.setWindowTitle("Rich Text Notepad") # 창 캡션
		self.setWindowIcon(QIcon("images/banana.png"))
		self.createWidgets()
		self.createMenu()		
		self.show() 
	
	def createWidgets(self):			
		self.text_field = QTextEdit()
		self.setCentralWidget(self.text_field)

	def createMenu(self):

		# 파일 메뉴
		new_act = QAction(QIcon("images/new_file.png"),"New", self)
		new_act.setShortcut("Ctrl+N")
		new_act.triggered.connect(self.clearText)

		open_act = QAction(QIcon("images/open_file.png"),"Open", self)
		open_act.setShortcut("Ctrl+O")
		open_act.triggered.connect(self.openFile)

		save_act = QAction(QIcon("images/save_file.png"),"Save", self)
		save_act.setShortcut("Ctrl+S")
		save_act.triggered.connect(self.saveFile)

		exit_act = QAction(QIcon("images/exit.png"),"Exit", self)
		exit_act.setShortcut("Ctrl+Q")
		exit_act.triggered.connect(self.close)
		
		# 편집 메뉴

		undo_act = QAction(QIcon("images/undo.png"),"Undo", self)
		undo_act.setShortcut("Ctrl+Z")
		undo_act.triggered.connect(self.text_field.undo)

		redo_act = QAction(QIcon("images/redo.png"),"Redo", self)
		redo_act.setShortcut("Ctrl+shift+Z")
		redo_act.triggered.connect(self.text_field.redo)

		cut_act = QAction(QIcon("images/cut.png"),"Cut", self)
		cut_act.setShortcut("Ctrl+X")
		cut_act.triggered.connect(self.text_field.cut)

		copy_act = QAction(QIcon("images/copy.png"),"Copy", self)
		copy_act.setShortcut("Ctrl+C")
		copy_act.triggered.connect(self.text_field.copy)

		paste_act = QAction(QIcon("images/paste.png"),"Paste", self)
		paste_act.setShortcut("Ctrl+V")
		paste_act.triggered.connect(self.text_field.paste)

		find_act = QAction(QIcon("images/find.png"),"Find", self)
		find_act.setShortcut("Ctrl+F")
		find_act.triggered.connect(self.findText)

		# 도구 메뉴
		font_act  = QAction(QIcon("images/font.png"),"Font", self)
		font_act.setShortcut("Ctrl+T")
		font_act.triggered.connect(self.chooseFont)

		color_act  = QAction(QIcon("images/color.png"),"Color", self)
		color_act.setShortcut("Ctrl+Shift+C")
		color_act.triggered.connect(self.chooseFontColor)

		highlight_act  = QAction(QIcon("images/highlight.png"),"Highlight", self)
		highlight_act.setShortcut("Ctrl+Shift+H")
		highlight_act.triggered.connect(self.chooseFontBackgroundColor)

		menu_bar = self.menuBar()
		menu_bar.setNativeMenuBar(False)

		file_menu = menu_bar.addMenu("File")
		file_menu.addAction(new_act)
		file_menu.addSeparator()
		file_menu.addAction(open_act)
		file_menu.addAction(save_act)
		file_menu.addSeparator()
		file_menu.addAction(exit_act)

		edit_menu = menu_bar.addMenu("Edit")
		edit_menu.addAction(undo_act)
		edit_menu.addAction(redo_act)
		edit_menu.addSeparator()
		edit_menu.addAction(cut_act)
		edit_menu.addAction(copy_act)
		edit_menu.addAction(paste_act)
		edit_menu.addSeparator()
		edit_menu.addAction(find_act)

		tool_menu = menu_bar.addMenu("Tool")
		tool_menu.addAction(font_act)
		tool_menu.addAction(color_act)		
		tool_menu.addAction(highlight_act)		

	def chooseFont(self):
		current = self.text_field.currentFont()
		font, ok = QFontDialog.getFont(current, self, 
			options = QFontDialog.DontUseNativeDialog)
		if ok :
			self.text_field.setCurrentFont(font)

	def chooseFontColor(self):
		color = QColorDialog.getColor()
		if color.isValid():
			self.text_field.setTextColor(color)
	
	def chooseFontBackgroundColor(self):
		color = QColorDialog.getColor()
		if color.isValid():
			self.text_field.setTextBackgroundColor(color)


	def findText(self):
		find_text, ok = QInputDialog.getText(self, 
			"Search Text", "Find:")

		extra_selections = []
		if ok and not self.text_field.isReadOnly():
			# 커서를 텍스트 에딧의 처음에 둔다
			self.text_field.moveCursor(QTextCursor.Start)
			color = QColor(Qt.yellow)
			# 텍스트가 있는지 조사

			while (self.text_field.find(find_text)):
				# 찾은 텍스트에 마킹을 하기 위해 ExtraSelection 사용
				selection = QTextEdit.ExtraSelection()
				selection.format.setBackground(color)

				# 선택된 커서를 설정
				selection.cursor = self.text_field.textCursor()
				extra_selections.append(selection)

			#텍스트 에딧 위젯에 하이라이트
			self.text_field.setExtraSelections(extra_selections)

	def clearText(self):
		answer = QMessageBox.question(self, "Clear Text",
		 "텍스트를 지우시겠습니까?", 
		 QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes )
		if answer == QMessageBox.Yes :
			self.text_field.clear()
		else :
			pass	

	def openFile(self):
		file_name , _ = 	QFileDialog.getOpenFileName(self, "Open File",
			"", "HTML 파일(*.html);;텍스트 파일(*.txt)")
		if file_name :
			with open(file_name, "r", encoding = 'utf-8') as f:
				input_text = f.read()
			self.text_field.setText(input_text)
		else : 
			QMessageBox.information(self, "Error", "파일을 열 수 없습니다." , QMessageBox.Ok)

	def saveFile(self):
		file_name, _ = QFileDialog.getSaveFileName(self, "Save File",
			"", "HTML 파일(*.html);;텍스트 파일(*.txt)")
		if file_name.endswith('.txt') :
			save_text = self.text_field.toPlainText()
			with open(file_name, "w", encoding = 'utf-8') as f:
				f.write(save_text)
		elif file_name.endswith(".html"):
			save_text = self.text_field.toHtml()
			with open(file_name, "w", encoding = 'utf-8') as f:
				f.write(save_text)
		else : 
			QMessageBox.information(self, "Error", "파일을 열 수 없습니다." , QMessageBox.Ok)



if __name__ ==  '__main__' :
	app = QApplication(sys.argv)		
	window = ChangeIcon()
	sys.exit(app.exec_())