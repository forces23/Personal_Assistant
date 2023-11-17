from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QListView, QPushButton, QVBoxLayout, QWidget, QStyledItemDelegate
from PyQt6.QtGui import QColor, QTextCursor, QKeyEvent, QColor, QFontMetrics, QFont
from PyQt6.QtCore import Qt, QEvent, QAbstractListModel, QMargins, QSize, QPoint
import sys, os
import openai

USER_ME = 0
USER_THEM = 1

BUBBLE_COLORS = {USER_ME: "#0080ff", USER_THEM: "#c8c8c8"}

# BUBBLE_PADDING = QMargins(0, 10, 20, 10)
TEXT_PADDING = QMargins(25, 15, 25, 15)


# Set the google cloud application acredtials 
os.environ['GOOGLE_APPLICATION_CREDENTIALS']="D:\google cloud stuff\jarvis-jenhvc-cdecde3fb66c.json"

# Set your OpenAI API key
api_key = "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"
openai.api_key = api_key


class MessageDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        user, text = index.model().data(index, Qt.ItemDataRole.DisplayRole)

        # textrect = option.rect.marginsRemoved(TEXT_PADDING)
        # bubblerect = textrect.marginsAdded(BUBBLE_PADDING)

        # -- NEW --
        if user == USER_ME:
            BUBBLE_PADDING = QMargins(0, 10, 0, 10)
        else:
            BUBBLE_PADDING = QMargins(0, 10, 0, 10)
        
        # Calculate the bounding rect of the text
        textFlags = Qt.TextFlag.TextWordWrap
        metrics = QFontMetrics(QFont())
        textrect = metrics.boundingRect(option.rect.marginsRemoved(TEXT_PADDING), textFlags, text)

        # Adjust the bubble width based on the text width
        bubblerect = textrect.marginsAdded(BUBBLE_PADDING)
        if user == USER_ME:
            bubblerect.moveLeft(option.rect.right() - textrect.width() - BUBBLE_PADDING.right() - 20)
            textFlags |= Qt.AlignmentFlag.AlignRight  # Align text to the right
        else:
            bubblerect.moveRight(option.rect.left() + textrect.width() + BUBBLE_PADDING.left() + 20)
            textFlags |= Qt.AlignmentFlag.AlignLeft  # Align text to the left
        # -- --- -- 

        # Draw the bubble
        painter.setPen(Qt.PenStyle.NoPen)
        color = QColor(BUBBLE_COLORS[user])
        painter.setBrush(color)
        painter.drawRoundedRect(bubblerect, 10, 10)

        # Draw the triangle pointer
        if user == USER_ME:
            p1 = bubblerect.topRight()
            # textFlags = Qt.TextFlag.TextWordWrap | Qt.AlignmentFlag.AlignRight # Align text to the right
        else:
            p1 = bubblerect.topLeft()
            # textFlags = Qt.TextFlag.TextWordWrap | Qt.AlignmentFlag.AlignLeft # Align text to the left
        painter.drawPolygon(p1 + QPoint(-20, 0), p1 + QPoint(20, 0), p1 + QPoint(0, 20))

        # Draw the text
        painter.setPen(Qt.GlobalColor.black)
        # painter.drawText(textrect, textFlags, text)
        # -- NEW -- 
        painter.drawText(bubblerect, textFlags, text)
        # -- --- -- 

    def sizeHint(self, option, index):
        _, text = index.model().data(index, Qt.ItemDataRole.DisplayRole)
        metrics = QFontMetrics(QFont())
        rect = option.rect.marginsRemoved(TEXT_PADDING)
        rect = metrics.boundingRect(rect, Qt.TextFlag.TextWordWrap, text)
        rect = rect.marginsAdded(TEXT_PADDING)
        return QSize(rect.width(), rect.height())

class MessageModel(QAbstractListModel):
    def __init__(self):
        super(MessageModel, self).__init__()
        self.messages = []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self.messages[index.row()]

    def rowCount(self, index):
        return len(self.messages)

    def add_message(self, who, text):
        print(f"text: {text}")
        if text:
            self.messages.append((who, text))
            self.layoutChanged.emit()

class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()

        # Load the UI Page - added path too
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "chatbot.ui"), self)

        self.chat_history.setItemDelegate(MessageDelegate())

        self.model = MessageModel()
        self.chat_history.setModel(self.model)

        self.submit.pressed.connect(self.send_message)
        self.user_input.installEventFilter(self)


    def send_message(self):
        user_text = self.user_input.toPlainText()
        self.model.add_message(USER_ME, user_text)

        self.user_input.clear()

        # AI chatbot response
        ai_response = " abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890"
        # ai_response = self.chat_with_bot(user_text)
        self.model.add_message(USER_THEM, ai_response)

   
    def eventFilter(self, source, event):
        if source is self.user_input and event.type() == QEvent.Type.KeyPress:
            key_event = event if isinstance(event, QKeyEvent) else QKeyEvent(event)
            if key_event.key() == Qt.Key.Key_Return and key_event.modifiers() == Qt.KeyboardModifier.ShiftModifier:
                cursor = self.user_input.textCursor()
                cursor.insertText("\n")
                return True
            elif key_event.key() == Qt.Key.Key_Return:
                self.send_message()
                return True
        return super().eventFilter(source, event)
    
    def chat_with_bot(self, user_input):
        # print("Hello! I'm your AI chatbot. You can start chatting. Type 'exit' to quit.")
        
        response = self.generate_response(user_input)
        # print("Chatbot:", response['choices'][0]['message']['content'])

        return response['choices'][0]['message']['content']

    def generate_response(self, user_input):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-3.5-turbo" model.
            messages=[
                {"role": "system", "content": "You are Jarvis, a highly intelligent AI assistant, just like in the Marvel movies. "
                                            "You have been assigned to assist the user and address them in a manner similar to how you address Tony Stark."
                                            "The user is MALE."
                                            "Refer to the user as only boss or sir."
                                            "Do not use sir and boss in the same sentence."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.2, # Can only set it in the range of 0.2 - 1. the lower the number the more straight forward the anwser is the higher the number the more creative the anwser is. also lower = less time to generate response
            max_tokens=150
        )
        return response
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec())