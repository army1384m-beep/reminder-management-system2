from dataclasses import dataclass, field
from typing import List
from base_reminder import Reminder

@dataclass
class MeetingReminder(Reminder):
    participants: List[str] = field(default_factory=list)
    
    def remind(self) -> str:
        people = "، ".join(self.participants)
        return f"{self.title} → people : {people} :Reminder Meeting"
    
    def __str__(self):
        return f"MeetingReminder: {self.title}"