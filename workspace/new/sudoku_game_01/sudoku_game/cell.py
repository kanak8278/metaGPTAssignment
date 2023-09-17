## cell.py
class Cell:
    def __init__(self, value: int, editable: bool):
        self.value = value
        self.editable = editable

    def get_value(self) -> int:
        """
        Get the value of the cell.
        """
        return self.value

    def set_value(self, value: int) -> None:
        """
        Set the value of the cell.
        """
        self.value = value

    def is_editable(self) -> bool:
        """
        Check if the cell is editable.
        """
        return self.editable
