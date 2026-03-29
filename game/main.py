import sys
from PyQt6.QtWidgets import QApplication
from game_window import ForestLearningGame

def main():
    app = QApplication(sys.argv)
    game = ForestLearningGame()
    game.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()