from dataclasses import dataclass, field
from .ID_generator import id_generator

@dataclass
class DailyRoutineReminder:
    title: str  
    time: str   
    daily_repeat: bool = True 
    id_reminder: int = field(init=False)  
    
    def __post_init__(self):
        self.id_reminder = id_generator.generate_id()
    
    def remind(self) -> str:
        status = "Active daily repetition" if self.daily_repeat else "Daily repeat deactivate"
        return f"{self.title} ){status}( :Daily Routine Reminder"
    
    def __str__(self) -> str:
        return f"DailyRoutineReminder: {self.title}"