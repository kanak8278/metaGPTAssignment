## text.py
class Text:
    def __init__(self, text: str, size: int, color: str, font: str):
        self.text = text
        self.size = size
        self.color = color
        self.font = font

    def render(self) -> pygame.Surface:
        """
        Render the text as a pygame surface.
        """
        font = pygame.font.Font(self.font, self.size)
        text_surface = font.render(self.text, True, pygame.Color(self.color))
        return text_surface
