from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QLineEdit, QMessageBox)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QColor, QPalette
from graphics import ForestCanvas
from game_logic import GameLogic

class ForestLearningGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.game_logic = GameLogic()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Forest Learning Game")
        self.setGeometry(100, 100, 1200, 800)
        
        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        
        # Game canvas
        self.canvas = ForestCanvas(self.game_logic)
        main_layout.addWidget(self.canvas, 3)
        
        # Right panel for questions and controls
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        
        # Current player label
        self.player_label = QLabel()
        self.player_label.setFont(QFont('Arial', 14, QFont.Weight.Bold))
        right_layout.addWidget(self.player_label)
        
        # Question label
        self.question_label = QLabel()
        self.question_label.setFont(QFont('Arial', 12))
        self.question_label.setWordWrap(True)
        right_layout.addWidget(self.question_label)
        
        # Answer input
        self.answer_input = QLineEdit()
        self.answer_input.setFont(QFont('Arial', 11))
        self.answer_input.returnPressed.connect(self.submit_answer)
        right_layout.addWidget(self.answer_input)
        
        # Submit button
        submit_btn = QPushButton("Submit Answer")
        submit_btn.setFont(QFont('Arial', 11))
        submit_btn.clicked.connect(self.submit_answer)
        right_layout.addWidget(submit_btn)
        
        # Status label
        self.status_label = QLabel()
        self.status_label.setFont(QFont('Arial', 10))
        self.status_label.setWordWrap(True)
        right_layout.addWidget(self.status_label)
        
        # Reset button
        reset_btn = QPushButton("New Game")
        reset_btn.setFont(QFont('Arial', 11))
        reset_btn.clicked.connect(self.reset_game)
        right_layout.addWidget(reset_btn)
        
        right_layout.addStretch()
        main_layout.addWidget(right_panel, 1)
        
        self.update_display()
        
    def update_display(self):
        """Update the question and player information display"""
        current_player = self.game_logic.get_current_player()
        self.player_label.setText(f"Current Player: {current_player['name']}")
        
        # Set player color
        if current_player['gender'] == 'boy':
            self.player_label.setStyleSheet("color: blue;")
        else:
            self.player_label.setStyleSheet("color: pink;")
        
        question = self.game_logic.get_current_question()
        if question:
            self.question_label.setText(f"Question: {question['text']}")
        
        self.answer_input.clear()
        self.answer_input.setFocus()
        
        # Update status
        boy_pos = self.game_logic.characters['boy']['position']
        girl_pos = self.game_logic.characters['girl']['position']
        self.status_label.setText(f"Boy at checkpoint: {boy_pos}\nGirl at checkpoint: {girl_pos}")
        
        self.canvas.update()
        
    def submit_answer(self):
        """Check the submitted answer"""
        answer = self.answer_input.text().strip().lower()
        
        if not answer:
            QMessageBox.warning(self, "Input Error", "Please enter an answer!")
            return
        
        is_correct = self.game_logic.check_answer(answer)
        
        if is_correct:
            if self.game_logic.move_player():
                # Check if game is won
                current_player = self.game_logic.get_current_player()
                if current_player['position'] >= 4:
                    winner = current_player['name']
                    QMessageBox.information(self, "Congratulations!", 
                                          f"{winner} has reached the village and won the game!")
                    self.reset_game()
                    return
            
            QMessageBox.information(self, "Correct!", "Great job! Moving to the next checkpoint.")
            self.game_logic.next_player()
        else:
            QMessageBox.warning(self, "Incorrect", 
                              f"Sorry, that's not correct. Try again on your next turn!\nCorrect answer: {self.game_logic.get_current_question()['answer']}")
            self.game_logic.next_player()
        
        self.update_display()
        
    def reset_game(self):
        """Reset the game"""
        self.game_logic = GameLogic()
        self.update_display()