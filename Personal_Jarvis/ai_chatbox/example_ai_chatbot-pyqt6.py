from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QLineEdit, QPushButton, QWidget
from PyQt6.QtGui import QTextCursor, QTextBlockFormat, QTextCharFormat, QColor
from PyQt6.QtCore import Qt

class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chatbot")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.chat_history = QTextEdit(self)
        self.chat_history.setReadOnly(True)
        self.layout.addWidget(self.chat_history)

        self.user_input = QLineEdit(self)
        self.user_input.returnPressed.connect(self.send_message)
        self.layout.addWidget(self.user_input)

        self.send_button = QPushButton("Send", self)
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)

        # Set font and color for user and AI messages
        font = QTextCharFormat()
        font.setFontFamily("Arial")
        font.setFontPointSize(16)

        user_color = QColor(0, 128, 255)  # Green color for user messages
        ai_color = QColor(200, 200, 200)  # Gray color for AI messages

        self.chat_history.setCurrentCharFormat(font)
        self.user_color = user_color
        self.ai_color = ai_color

        self.chat_history.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.user_input.setPlaceholderText("Type a message...")

    def send_message(self):
        user_text = self.user_input.text()
        self.add_message(f'You: {user_text}', self.user_color)
        self.user_input.clear()

        # Simulate AI chatbot response (replace this with your AI logic)
        ai_response = "This is the AI response.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        self.add_message(f'AI: {ai_response}', self.ai_color)

    def add_message(self, message, color):
        cursor = self.chat_history.textCursor()

        if cursor.atBlockStart():
            cursor.insertBlock()
            cursor.movePosition(QTextCursor.MoveOperation.NoMove, QTextCursor.MoveMode.KeepAnchor)

        format = cursor.charFormat()
        format.setForeground(color)
        cursor.mergeCharFormat(format)

        # Add bubble-style background
        bubble_style = 'background-color: #f0f0f0; border-radius: 10px; padding: 10px;'
        formatted_message = f'<div style="{bubble_style}">{message}</div>'
        cursor.insertHtml(formatted_message)

        format = cursor.blockFormat()
        format.setAlignment(Qt.AlignmentFlag.AlignLeft)
        cursor.setBlockFormat(format)
        cursor.clearSelection()

        self.chat_history.setTextCursor(cursor)
        self.chat_history.verticalScrollBar().setValue(self.chat_history.verticalScrollBar().maximum())

if __name__ == "__main__":
    app = QApplication([])
    window = ChatWindow()
    window.show()
    app.exec()
