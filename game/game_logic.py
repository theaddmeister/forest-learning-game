from questions import QUESTIONS

class GameLogic:
    def __init__(self):
        self.characters = {
            'boy': {
                'name': 'Tommy',
                'gender': 'boy',
                'position': 0,  # 0 = house, 1-4 = checkpoints, 5 = village
                'color': 'blue'
            },
            'girl': {
                'name': 'Sarah',
                'gender': 'girl',
                'position': 0,
                'color': 'pink'
            }
        }
        self.current_player = 'boy'
        self.current_question_index = 0
        
    def get_current_player(self):
        """Get the current player's data"""
        return self.characters[self.current_player]
    
    def get_current_question(self):
        """Get the question for the current checkpoint"""
        player = self.get_current_player()
        position = player['position']
        
        if position < len(QUESTIONS):
            return QUESTIONS[position]
        return None
    
    def check_answer(self, answer):
        """Check if the answer is correct"""
        question = self.get_current_question()
        if question:
            return answer == question['answer'].lower()
        return False
    
    def move_player(self):
        """Move the current player to the next checkpoint"""
        player = self.get_current_player()
        if player['position'] < 4:
            player['position'] += 1
            return True
        return False
    
    def next_player(self):
        """Switch to the next player"""
        self.current_player = 'girl' if self.current_player == 'boy' else 'boy'
    
    def get_game_state(self):
        """Get the current game state"""
        return {
            'boy_position': self.characters['boy']['position'],
            'girl_position': self.characters['girl']['position'],
            'current_player': self.current_player
        }