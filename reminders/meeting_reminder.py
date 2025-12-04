from dataclasses import dataclass, field
from .ID_generator import id_generator
from typing import List

@dataclass
class MeetingReminder:

    
    title: str  
    time: str  
    participants: List[str] = field(default_factory=list)  
    id_reminder: int = field(init=False) 
    
    def __post_init__(self):
        self.id_reminder = id_generator.generate_id()
    
    def remind(self) -> str:
        people = "، ".join(self.participants)
        return f"{self.title} → people : {people} :Meeting Reminder"
    
    def __str__(self) -> str:
        return f"MeetingReminder: {self.title}"