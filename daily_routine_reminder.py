from dataclasses import dataclass, field
from base_reminder import Reminder

@dataclass
class DailyRoutineReminder(Reminder):
    daily_repeat: bool = True
    
    def remind(self) -> str:
        status ="Active daily repetition" if self.daily_repeat else "Daily repeat disabled"
        return f"{self.title} ){status}( :Routine Daily"
    
    def __str__(self):
        return f"DailyRoutineReminder: {self.title}"