## menu.py
class Menu:
    def __init__(self):
        self.difficulty_levels = ["easy", "medium", "hard"]
        self.difficulty = None

    def get_difficulty_levels(self):
        """
        Get the available difficulty levels.
        """
        return self.difficulty_levels

    def set_difficulty(self, difficulty):
        """
        Set the difficulty level.
        """
        if difficulty in self.difficulty_levels:
            self.difficulty = difficulty
        else:
            raise ValueError("Invalid difficulty level")
