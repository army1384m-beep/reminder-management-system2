from dataclasses import dataclass
from base_reminder import Reminder

@dataclass
class SimpleReminder(Reminder):
    
    def remind(self) -> str:
        return f"It is time: {self.title}"
    
    def __str__(self) -> str:
        return f"SimpleReminder: {self.title}"